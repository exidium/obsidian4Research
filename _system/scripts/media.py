#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml", "pillow"]
# ///
"""Recordings, clips and reels for the research vault.

Media never enters git. Recordings, clips and reels live under _raw/<project>/ (gitignored). In production,
_raw/<project> is the OneDrive-synced SharePoint study folder (or a symlink to it), so the same relative path
works for everyone who has access, and people without access see a pointer and a checksum, not the file.

  media.py frame <S-id> <hh:mm:ss>                      still frame to _raw/<project>/frames/ (find what to blur)
  media.py link  <S-id> <file> [--url URL] [--redact x,y,w,h[:label] ...]
                                                        attach a recording to a source note (moves it into _raw/<project>/)
  media.py clip  <H-id> [--whole] [--context] [--allow-internal] [--force]
                                                        cut the highlight's moment, blur the source's redact regions,
                                                        burn pseudonymised captions, stamp provenance
  media.py reel  <I-id> [--context] [--force]           title card + one clip per cited highlight, as one video
  media.py check [project]                              are recordings present and unchanged?

Internal participants (participant_type internal-*) never get voice or video in a clip: the clip is a text card
with the quote, unless --allow-internal is given (for the research team's own use only).

Run with uv, which installs Pillow and PyYAML on first use: uv run _system/scripts/media.py ..."""
from __future__ import annotations

import argparse, hashlib, json, re, shutil, subprocess, sys, tempfile, textwrap
from datetime import date, datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vaultlib import DIRS, NOTE_DIRS, read_note, write_note, vault_root, wikilink_target  # noqa: E402

W, H, FPS = 1280, 720, 25
ENC_V = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "22", "-pix_fmt", "yuv420p", "-r", str(FPS)]
ENC_A = ["-c:a", "aac", "-b:a", "128k", "-ar", "44100", "-ac", "2"]
TURN_RE = re.compile(r"^\[(\d{2}):(\d{2}):(\d{2})\]\s+\*\*(.+?):\*\*\s+(.*?)\s*\^(s\d{4}-\d{4})\s*$", re.S)


# ---------------------------------------------------------------- small helpers

def die(msg: str):
    sys.exit(f"media.py: {msg}")


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode:
        die(f"{cmd[0]} failed:\n{p.stderr[-2000:]}")
    return p


def hms(t: float, frac: bool = False) -> str:
    t = max(0.0, t)
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{s:04.1f}" if frac else f"{int(h):02d}:{int(m):02d}:{int(s):02d}"


def secs(s: str) -> float:
    parts = [float(x) for x in str(s).split(":")]
    while len(parts) < 3:
        parts.insert(0, 0.0)
    return parts[0] * 3600 + parts[1] * 60 + parts[2]


def duration(path: Path) -> float:
    p = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", str(path)])
    return float(json.loads(p.stdout)["format"]["duration"])


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def find_note(root: Path, folder: str, note_id: str) -> Path:
    for d in NOTE_DIRS:
        base = root / d
        if base.exists():
            hits = sorted(base.glob(f"*/{DIRS.get(folder, folder)}/{note_id}*.md"))
            hits = [h for h in hits if h.stem == note_id or h.stem.startswith(note_id + " ")]
            if hits:
                return hits[0]
    die(f"{note_id} not found in {folder}/")


def media_dir(root: Path, project: str, sub: str = "") -> Path:
    d = root / "_raw" / project / sub
    d.mkdir(parents=True, exist_ok=True)
    return d


def rel(root: Path, p: Path) -> str:
    return p.resolve().relative_to(root.resolve()).as_posix() if p.resolve().is_relative_to(root.resolve()) else str(p)


def provenance(root: Path, action: str, target: str):
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with (root / "_system" / "provenance.log").open("a", encoding="utf-8") as f:
        f.write(f"{stamp}\tresearch-clip\t{action}\t{target}\tffmpeg\n")


def embed_after(body: str, anchor_re: str, line: str) -> str:
    """Insert an embed line after the first line matching anchor_re, unless it is already there."""
    if line in body:
        return body
    lines = body.split("\n")
    for i, l in enumerate(lines):
        if re.match(anchor_re, l):
            lines[i + 1:i + 1] = ["", line]
            return "\n".join(lines)
    return f"{line}\n\n{body}"


# ---------------------------------------------------------------- transcript

def turns(body: str) -> list[dict]:
    out = []
    for para in re.split(r"\n\s*\n", body):
        m = TURN_RE.match(para.strip())
        if m:
            h, mi, s, speaker, text, block = m.groups()
            out.append({"t": int(h) * 3600 + int(mi) * 60 + int(s), "speaker": speaker.strip(), "text": " ".join(text.split()), "block": block})
    return out


def _words(s: str) -> list[str]:
    return [w for w in re.split(r"[^\w']+", s.lower()) if w]


def quote_fraction(block_text: str, quote: str) -> tuple[float, float] | None:
    """Where the quote sits in the turn, as fractions of its spoken length (character-weighted)."""
    bw, qw = _words(block_text), _words(quote)
    if not qw:
        return None
    for i in range(len(bw) - len(qw) + 1):
        if bw[i:i + len(qw)] == qw:
            cum = [0]
            for w in bw:
                cum.append(cum[-1] + len(w) + 1)
            return cum[i] / cum[-1], cum[i + len(qw)] / cum[-1]
    return None


def silences(rec: Path, a: float, b: float, min_d: float = 0.25) -> list[tuple[float, float]]:
    """Silent stretches inside [a, b], in recording time."""
    p = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-ss", f"{a:.2f}", "-to", f"{b:.2f}", "-i", str(rec),
                        "-vn", "-af", f"silencedetect=n=-38dB:d={min_d}", "-f", "null", "-"], capture_output=True, text=True)
    starts = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", p.stderr)]
    ends = [float(x) for x in re.findall(r"silence_end: (-?[\d.]+)", p.stderr)]
    ends += [b - a] * (len(starts) - len(ends))
    return [(a + max(0.0, s_), a + e) for s_, e in zip(starts, ends)]


def speech_end(rec: Path, a: float, b: float) -> float:
    """End of speech inside [a, b]: the start of trailing silence, if any."""
    sil = silences(rec, a, b, 0.45)
    if sil and sil[-1][1] >= b - 0.2:
        return min(b, max(a + 0.5, sil[-1][0]))
    return b


def voiced_at(a: float, b: float, pauses: list[tuple[float, float]], frac: float) -> float:
    """Recording time at which `frac` of the speech in [a, b] has been spoken, skipping pauses."""
    segs, t = [], a
    for ps, pe in pauses:
        if ps > t:
            segs.append((t, min(ps, b)))
        t = max(t, pe)
    if t < b:
        segs.append((t, b))
    total = sum(e - s_ for s_, e in segs) or 1.0
    want = frac * total
    for s_, e in segs:
        if want <= e - s_:
            return s_ + want
        want -= e - s_
    return b


WHISPER = shutil.which("mlx_whisper") or str(Path.home() / ".local/bin/mlx_whisper")


def align_quote(rec: Path, a: float, b: float, quote: str) -> tuple[float, float] | None:
    """(first word start, last word end, safe start, safe end) from local Whisper word timestamps on [a, b].
    Safe edges pad into silence but never into the neighbouring words. None if Whisper is unavailable or no match."""
    qw = _words(quote)
    if not qw or not Path(WHISPER).exists():
        return None
    with tempfile.TemporaryDirectory() as tmp:
        wav = Path(tmp) / "turn.wav"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{a:.2f}", "-to", f"{b:.2f}", "-i", str(rec),
                        "-vn", "-ac", "1", "-ar", "16000", str(wav)], check=True)
        p = subprocess.run([WHISPER, str(wav), "--model", "mlx-community/whisper-large-v3-turbo", "--word-timestamps", "True",
                            "--output-format", "json", "--output-dir", tmp, "--verbose", "False"], capture_output=True, text=True)
        js = Path(tmp) / "turn.json"
        if p.returncode or not js.exists():
            return None
        ww = [(w2, float(w["start"]), float(w["end"]))
              for seg in json.loads(js.read_text())["segments"] for w in seg.get("words", []) for w2 in _words(w["word"])[:1]]
    if not ww:
        return None
    k = min(4, len(qw))
    words = [w for w, _, _ in ww]
    score = lambda win, ref: sum(x == y for x, y in zip(win, ref))
    i = max(range(len(ww)), key=lambda n: (score(words[n:n + k], qw[:k]), -n))
    j = max(range(i, len(ww)), key=lambda n: (score(words[max(i, n - k + 1):n + 1], qw[-k:]), -abs(n - i - len(qw))))
    if score(words[i:i + k], qw[:k]) < max(1, k - 1) or score(words[max(i, j - k + 1):j + 1], qw[-k:]) < max(1, k - 1):
        return None
    lo = ww[i - 1][2] + 0.03 if i > 0 else ww[i][1] - 0.2
    hi = ww[j + 1][1] - 0.03 if j + 1 < len(ww) else ww[j][2] + 0.3
    return a + ww[i][1], a + ww[j][2], a + max(lo, ww[i][1] - 0.2), a + min(hi, ww[j][2] + 0.3)


def snap(est: float, edges: list[float], before: float, after: float) -> float | None:
    """The pause edge closest to an estimated time, within [est - before, est + after]."""
    near = [e for e in edges if est - before <= e <= est + after]
    return min(near, key=lambda e: abs(e - est)) if near else None


# ---------------------------------------------------------------- drawing (Pillow)

def _pil():
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        die("Pillow is missing. Run with uv: uv run _system/scripts/media.py ...")
    return Image, ImageDraw, ImageFont


def font(weight: str, size: int):
    _, _, ImageFont = _pil()
    dirs = [Path.home() / "Library/Fonts", Path("/Library/Fonts"), Path("/System/Library/Fonts/Supplemental")]
    for d in dirs:
        for name in (f"Barlow-{weight}.otf", f"Barlow-{weight}.ttf"):
            if (d / name).exists():
                return ImageFont.truetype(str(d / name), size)
    for d in dirs:
        if (d / "Arial.ttf").exists():
            return ImageFont.truetype(str(d / "Arial.ttf"), size)
    return ImageFont.load_default(size)


def wrap_px(text: str, f, width: int) -> list[str]:
    lines, cur = [], ""
    for w in text.split():
        nxt = f"{cur} {w}".strip()
        if cur and f.getlength(nxt) > width:
            lines.append(cur)
            cur = w
        else:
            cur = nxt
    if cur:
        lines.append(cur)
    return lines


def caption_png(path: Path, speaker: str, lines: list[str]):
    Image, ImageDraw, _ = _pil()
    fl, ft = font("SemiBold", 22), font("Medium", 30)
    img = Image.new("RGBA", (W, 136), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    tw = max([ft.getlength(l) for l in lines] + [fl.getlength(speaker)])
    x0 = int((W - tw) / 2) - 22
    d.rounded_rectangle([x0, 4, W - x0, 132], radius=10, fill=(0, 0, 0, 185))
    d.text((x0 + 22, 12), speaker, font=fl, fill=(120, 190, 255, 255))
    for i, l in enumerate(lines):
        d.text((x0 + 22, 44 + i * 40), l, font=ft, fill=(255, 255, 255, 255))
    img.save(path)


def stamp_png(path: Path, text: str):
    Image, ImageDraw, _ = _pil()
    f = font("Medium", 18)
    tw = int(f.getlength(text)) + 36
    img = Image.new("RGBA", (tw, 32), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, tw - 1, 31], radius=6, fill=(0, 0, 0, 170))
    d.text((12, 5), text, font=f, fill=(230, 230, 230, 255))
    img.save(path)
    return tw


def card_png(path: Path, kicker: str, title: str, lines: list[str], footer: str):
    """ADI-ish title card: dark blue, Barlow."""
    Image, ImageDraw, _ = _pil()
    img = Image.new("RGB", (W, H), (0, 50, 92))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 14, H], fill=(0, 103, 185))
    fk, ftit, fl, ff = font("SemiBold", 24), font("Medium", 48), font("Regular", 28), font("Regular", 20)
    y = 120
    d.text((90, y), kicker.upper(), font=fk, fill=(140, 190, 235))
    y += 56
    for l in wrap_px(title, ftit, W - 200)[:4]:
        d.text((90, y), l, font=ftit, fill=(255, 255, 255))
        y += 62
    y += 24
    for raw in lines:
        for l in wrap_px(raw, fl, W - 200)[:6]:
            d.text((90, y), l, font=fl, fill=(205, 215, 230))
            y += 40
    d.text((90, H - 70), footer, font=ff, fill=(158, 161, 174))
    img.save(path)


def card_clip(png: Path, out: Path, seconds: float):
    run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-framerate", str(FPS), "-t", f"{seconds:.2f}", "-i", str(png),
         "-f", "lavfi", "-t", f"{seconds:.2f}", "-i", "anullsrc=r=44100:cl=stereo",
         *ENC_V, "-tune", "stillimage", *ENC_A, "-shortest", "-movflags", "+faststart", str(out)])


# ---------------------------------------------------------------- commands

def cmd_frame(root: Path, a):
    src = find_note(root, "sources", a.source)
    fm, _ = read_note(src)
    rec = root / str(fm.get("recording") or "")
    if not fm.get("recording") or not rec.exists():
        die(f"{a.source} has no local recording (run link first, or sync the study folder)")
    out = media_dir(root, fm["project"], "frames") / f"{a.source}_{a.at.replace(':', '')}.png"
    run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(secs(a.at)), "-i", str(rec), "-frames:v", "1", str(out)])
    p = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", str(rec)])
    print(out)
    print(f"recording size {p.stdout.strip()} (redact regions use these pixel coordinates)")


def cmd_link(root: Path, a):
    src = find_note(root, "sources", a.source)
    fm, body = read_note(src)
    f = Path(a.file).expanduser()
    if not f.exists():
        die(f"no such file: {f}")
    dest_dir = media_dir(root, fm["project"])
    dest = dest_dir / f"{a.source}{f.suffix.lower()}"
    if f.resolve() != dest.resolve():
        if dest.exists():
            die(f"{rel(root, dest)} already exists; move it away first")
        shutil.move(str(f), dest)
    regions = []
    for r in a.redact or []:
        box, _, label = r.partition(":")
        try:
            x, y, w, h = (int(v) for v in box.split(","))
        except ValueError:
            die(f"bad --redact {r!r}; want x,y,w,h[:label]")
        regions.append({"x": x, "y": y, "w": w, "h": h, "label": label or "redact"})
    fm["recording"] = rel(root, dest)
    if a.url:
        fm["recording_url"] = a.url
    fm["recording_sha256"] = sha256(dest)
    fm["recording_duration"] = hms(duration(dest))
    if regions or "redact_regions" not in fm:
        fm["redact_regions"] = regions
    write_note(src, fm, body)
    provenance(root, "link", a.source)
    print(f"{a.source}: {fm['recording']} ({fm['recording_duration']}, sha256 {fm['recording_sha256'][:12]}…, {len(fm['redact_regions'])} redact region(s))")


def _clip_window(rec: Path, ts: list[dict], i: int, quote: str, whole: bool, rec_dur: float):
    """(start, end, [(speaker, text, a, b)]) in recording time for turn i."""
    turn = ts[i]
    nxt = ts[i + 1]["t"] if i + 1 < len(ts) else rec_dur
    s_end = speech_end(rec, turn["t"], nxt)
    a, b, text = turn["t"], s_end, turn["text"]
    fr = None if whole else quote_fraction(turn["text"], quote)
    if fr and (fr[1] - fr[0]) < 0.85:
        exact = align_quote(rec, turn["t"], s_end, quote)
        if exact:
            return max(turn["t"], exact[2]), min(nxt, exact[3]), [(turn["speaker"], quote, exact[0], exact[1])]
        pauses = silences(rec, turn["t"], s_end, 0.15)
        est_a, est_b = voiced_at(turn["t"], s_end, pauses, fr[0]), voiced_at(turn["t"], s_end, pauses, fr[1])
        sa = snap(est_a, [e for _, e in pauses], 1.5, 1.5)
        sb = snap(est_b, [st for st, _ in pauses], 1.5, 1.5)
        a = max(turn["t"], sa - 0.1 if sa is not None else est_a - 0.4)
        b = min(nxt, sb + 0.15 if sb is not None else est_b + 0.6, s_end + 0.3)
        text = quote
    return a, b, [(turn["speaker"], text, a, b)]


def _captions(pieces, t0: float) -> list[tuple[str, list[str], float, float]]:
    """Split each spoken piece into two-line captions, timed by character share. Times relative to t0."""
    ft = font("Medium", 30)
    out = []
    for speaker, text, a, b in pieces:
        lines = wrap_px(text, ft, W - 220)
        chunks = [lines[k:k + 2] for k in range(0, len(lines), 2)]
        total = sum(len(" ".join(c)) for c in chunks) or 1
        t = a
        for c in chunks:
            d = (b - a) * len(" ".join(c)) / total
            out.append((speaker, c, t - t0, t - t0 + d))
            t += d
    return out


def _is_internal(fm: dict) -> bool:
    return str(fm.get("participant_type", "")).startswith("internal")


def build_clip(root: Path, hl_id: str, whole=False, context=False, allow_internal=False, force=False) -> tuple[Path, dict, dict]:
    hp = find_note(root, "highlights", hl_id)
    hfm, hbody = read_note(hp)
    sid = wikilink_target(hfm.get("source"))
    sp = find_note(root, "sources", sid)
    sfm, sbody = read_note(sp)
    project = sfm["project"]
    out = media_dir(root, project, "clips") / f"{hl_id}.mp4"
    ts = turns(sbody)
    idx = next((k for k, t in enumerate(ts) if t["block"] == hfm.get("block")), None)
    if idx is None:
        die(f"{hl_id}: block {hfm.get('block')} has no timestamped turn in {sid}")
    internal = _is_internal(sfm) and not allow_internal

    if out.exists() and not force:
        return out, hfm, sfm

    with tempfile.TemporaryDirectory(dir=media_dir(root, project)) as tmp:
        tmp = Path(tmp)
        if internal:
            quote = hfm.get("quote") or ts[idx]["text"]
            secs_ = min(14.0, max(5.0, len(quote) / 14))
            card_png(tmp / "card.png", f"{hfm.get('participant')} · internal participant", f"“{quote}”",
                     [], f"{sid} @ {hms(ts[idx]['t'])} · voice and video withheld (internal interview policy)")
            card_clip(tmp / "card.png", out, secs_)
            kind, start, end = "text-card", ts[idx]["t"], ts[idx]["t"]
        else:
            rec = root / str(sfm.get("recording") or "")
            if not sfm.get("recording") or not rec.exists():
                die(f"{sid} has no local recording; run `media.py link {sid} <file>` or sync the study folder")
            rec_dur = duration(rec)
            start, end, pieces = _clip_window(rec, ts, idx, hfm.get("quote") or "", whole or context, rec_dur)
            if context and idx > 0 and ts[idx - 1]["speaker"] != ts[idx]["speaker"]:
                q = ts[idx - 1]
                q_end = speech_end(rec, q["t"], ts[idx]["t"])
                pieces = [(q["speaker"], q["text"], q["t"], q_end)] + pieces
                start = q["t"]
            start, end = max(0.0, start), min(rec_dur, end)
            dur = end - start

            inputs = ["-ss", f"{start:.3f}", "-to", f"{end:.3f}", "-i", str(rec)]
            graph, last = [], "0:v"
            for k, r in enumerate(sfm.get("redact_regions") or []):
                graph.append(f"[{last}]split=2[b{k}][s{k}];[s{k}]crop={r['w']}:{r['h']}:{r['x']}:{r['y']},gblur=sigma=14[g{k}];"
                             f"[b{k}][g{k}]overlay={r['x']}:{r['y']}[r{k}]")
                last = f"r{k}"
            graph.append(f"[{last}]scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps={FPS}[v0]")
            last, n = "v0", 1
            for k, (speaker, lines, a, b) in enumerate(_captions(pieces, start)):
                png = tmp / f"cap{k:03d}.png"
                caption_png(png, speaker, lines)
                inputs += ["-i", str(png)]
                graph.append(f"[{last}][{n}:v]overlay=0:{H - 136 - 22}:enable='between(t,{max(0, a):.2f},{b:.2f})'[c{k}]")
                last, n = f"c{k}", n + 1
            stamp = f"{hfm.get('participant')} · {sid} @ {hms(ts[idx]['t'])} · {hl_id} · pseudonymised"
            sw = stamp_png(tmp / "stamp.png", stamp)
            inputs += ["-i", str(tmp / "stamp.png")]
            graph.append(f"[{last}][{n}:v]overlay={W - sw - 14}:12[v]")
            graph.append(f"[0:a]aformat=sample_rates=44100:channel_layouts=stereo,afade=t=in:d=0.15,afade=t=out:st={max(0, dur - 0.35):.2f}:d=0.35[a]")
            run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", ";".join(graph),
                 "-map", "[v]", "-map", "[a]", *ENC_V, *ENC_A, "-movflags", "+faststart", str(out)])
            kind = "video"

    hfm["clip"] = rel(root, out)
    hfm["clip_kind"] = kind
    hfm["clip_start"] = hms(start, frac=True)
    hfm["clip_end"] = hms(end, frac=True)
    hbody = embed_after(hbody, r"^!\[\[S-\d{4}#", f"![[{rel(root, out)}]]")
    write_note(hp, hfm, hbody)
    provenance(root, "clip", hl_id)
    return out, hfm, sfm


def cmd_clip(root: Path, a):
    out, hfm, _ = build_clip(root, a.highlight, a.whole, a.context, a.allow_internal, force=True)
    print(f"{a.highlight}: {rel(root, out)} ({hfm['clip_kind']}, {hfm['clip_start']}–{hfm['clip_end']}, {duration(out):.1f}s)")


def cmd_reel(root: Path, a):
    ip = find_note(root, "insights", a.insight)
    ifm, ibody = read_note(ip)
    project = ifm["project"]
    hl_ids = [wikilink_target(h) for h in ifm.get("highlights") or []]
    if not hl_ids:
        die(f"{a.insight} cites no highlights")
    out = media_dir(root, project, "reels") / f"{a.insight}.mp4"
    with tempfile.TemporaryDirectory(dir=media_dir(root, project)) as tmp:
        tmp = Path(tmp)
        parts, people, internal = [], set(), 0
        title = re.sub(r"^Insight:\s*", "", ifm.get("title") or a.insight)
        for k, h in enumerate(hl_ids):
            clip, hfm, sfm = build_clip(root, h, context=a.context, force=a.force)
            people.add(hfm.get("participant"))
            internal += _is_internal(sfm)
            card_png(tmp / f"t{k}.png", f"Evidence {k + 1} of {len(hl_ids)} · {hfm.get('participant')}",
                     hfm.get("title") or h, [], f"{h} · {wikilink_target(hfm.get('source'))} @ {hfm.get('clip_start', '')[:8]}")
            card_clip(tmp / f"t{k}.png", tmp / f"t{k}.mp4", 2.2)
            parts += [tmp / f"t{k}.mp4", clip]
        lines = [f"{len(hl_ids)} moments from {len(people)} participants · evidence: {ifm.get('evidence_level', 'n/a')}"]
        if internal:
            lines.append(f"{internal} from internal interviews, shown as text only.")
        card_png(tmp / "intro.png", f"Insight {a.insight.rsplit('-', 1)[-1]} · {project}", title, lines,
                 f"Pseudonymised reel generated {date.today().isoformat()} from the research vault. Every clip is stamped with its source and timestamp.")
        card_clip(tmp / "intro.png", tmp / "intro.mp4", 4.0)
        lst = tmp / "list.txt"
        lst.write_text("".join(f"file '{p.resolve()}'\n" for p in [tmp / "intro.mp4", *parts]), encoding="utf-8")
        run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), *ENC_V, *ENC_A,
             "-movflags", "+faststart", str(out)])
    ifm["reel"] = rel(root, out)
    ifm["reel_duration"] = hms(duration(out))
    ibody = embed_after(ibody, r"^# ", f"![[{rel(root, out)}]]")
    write_note(ip, ifm, ibody)
    provenance(root, "reel", a.insight)
    print(f"{a.insight}: {rel(root, out)} ({ifm['reel_duration']}, {len(hl_ids)} clips, {len(people)} participants)")


def cmd_check(root: Path, a):
    bad = 0
    for d in NOTE_DIRS:
        for p in sorted((root / d).glob(f"{a.project or '*'}/{DIRS['sources']}/S-*.md")):
            fm, _ = read_note(p)
            if not fm.get("recording"):
                continue
            f = root / fm["recording"]
            if not f.exists():
                print(f"{fm['source_id']}: no local copy of {fm['recording']} (sync the study folder if you have access)")
            elif fm.get("recording_sha256") and sha256(f) != fm["recording_sha256"]:
                print(f"{fm['source_id']}: CHANGED since it was linked: {fm['recording']}")
                bad += 1
            else:
                print(f"{fm['source_id']}: ok {fm['recording']} ({fm.get('recording_duration')})")
    sys.exit(1 if bad else 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("frame"); p.add_argument("source"); p.add_argument("at")
    p = sub.add_parser("link"); p.add_argument("source"); p.add_argument("file"); p.add_argument("--url"); p.add_argument("--redact", action="append")
    p = sub.add_parser("clip"); p.add_argument("highlight"); p.add_argument("--whole", action="store_true")
    p.add_argument("--context", action="store_true"); p.add_argument("--allow-internal", action="store_true")
    p = sub.add_parser("reel"); p.add_argument("insight"); p.add_argument("--context", action="store_true"); p.add_argument("--force", action="store_true")
    p = sub.add_parser("check"); p.add_argument("project", nargs="?")
    a = ap.parse_args()
    root = vault_root(Path(__file__).resolve().parent)
    {"frame": cmd_frame, "link": cmd_link, "clip": cmd_clip, "reel": cmd_reel, "check": cmd_check}[a.cmd](root, a)


if __name__ == "__main__":
    main()
