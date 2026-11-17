#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml", "pillow"]
# ///
"""DEMO ONLY: make a synthetic video call recording from a fictional source note, so the clip and reel
pipeline can be shown without any real interview. Never use on a real project.

  demo_recording.py <S-id> [--plate "Name · Company"] [--voice Samantha]
                    [--interviewer "Sam Reyes · UX Research"] [--interviewer-voice Daniel]

The name plate defaults to name · company from the Rally export in _raw/rally/participants.json, so no name
needs to appear on a command line or in a file under git. Speech is macOS `say`, placed at each turn's transcript timestamp (sped up when a turn would overrun the
next one), so the transcript's timestamps are true for the video. The participant's tile carries a
fictional name plate, which is what the redact region in the demo blurs.

Writes _raw/<project>/<S-id>.mp4 and prints the media.py link command to attach it."""
from __future__ import annotations

import argparse, subprocess, sys, tempfile, wave
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vaultlib import read_note, vault_root  # noqa: E402
from media import FPS, H, W, _pil, find_note, font, media_dir, rel, run, turns  # noqa: E402

RATE = 22050
TILE_Y, TILE_W, TILE_H = 86, 590, 440
TILES = {"left": 40, "right": 650}
PURPLE = (98, 100, 167)


def say(text: str, voice: str, wpm: int, out: Path, txt: Path) -> float:
    txt.write_text(text, encoding="utf-8")
    run(["say", "-v", voice, "-r", str(wpm), "-f", str(txt), "-o", str(out), "--data-format=LEI16@22050"])
    with wave.open(str(out)) as w:
        return w.getnframes() / w.getframerate()


def frame(path: Path, active: str | None, plates: dict, title: str):
    Image, ImageDraw, _ = _pil()
    img = Image.new("RGB", (W, H), (32, 32, 34))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 52], fill=(24, 24, 26))
    d.ellipse([20, 18, 36, 34], fill=(220, 50, 50))
    d.text((48, 14), f"Recording · {title}", font=font("Medium", 20), fill=(230, 230, 230))
    note = "Synthetic demo recording · fictional people"
    fn = font("Regular", 16)
    d.text((W - 20 - fn.getlength(note), 18), note, font=fn, fill=(150, 150, 155))
    for side, x in TILES.items():
        name = plates[side]
        d.rounded_rectangle([x, TILE_Y, x + TILE_W, TILE_Y + TILE_H], radius=12, fill=(45, 45, 48))
        if side == active:
            d.rounded_rectangle([x - 3, TILE_Y - 3, x + TILE_W + 3, TILE_Y + TILE_H + 3], radius=14, outline=PURPLE, width=5)
        cx, cy, r = x + TILE_W // 2, TILE_Y + TILE_H // 2 - 20, 78
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 103, 185) if side == "right" else (90, 92, 110))
        initials = "".join(p[0] for p in name.split("·")[0].split()[:2]).upper()
        fi = font("SemiBold", 64)
        d.text((cx - fi.getlength(initials) / 2, cy - 40), initials, font=fi, fill=(255, 255, 255))
        fp = font("Medium", 20)
        pw = int(fp.getlength(name)) + 24
        d.rounded_rectangle([x + 12, TILE_Y + TILE_H - 46, x + 12 + pw, TILE_Y + TILE_H - 12], radius=6, fill=(20, 20, 22))
        d.text((x + 24, TILE_Y + TILE_H - 42), name, font=fp, fill=(240, 240, 240))
    img.save(path)
    fp = font("Medium", 20)
    return {side: (x + 12, TILE_Y + TILE_H - 46, int(fp.getlength(plates[side])) + 24, 34) for side, x in TILES.items()}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source")
    ap.add_argument("--plate", help="fictional participant name plate; default: name · company from _raw/rally/participants.json")
    ap.add_argument("--voice", default="Samantha")
    ap.add_argument("--interviewer", default="Sam Reyes · UX Research")
    ap.add_argument("--interviewer-voice", default="Daniel")
    a = ap.parse_args()

    root = vault_root(Path(__file__).resolve().parent)
    sp = find_note(root, "sources", a.source)
    fm, body = read_note(sp)
    if not str(fm.get("project", "")).startswith("2026_demo"):
        sys.exit("demo_recording.py only runs on the fictional demo project")
    ts = turns(body)
    if not ts:
        sys.exit(f"{a.source}: no timestamped turns")
    out = media_dir(root, fm["project"]) / f"{a.source}.mp4"
    if not a.plate:
        import json
        rows = json.loads((root / "_raw" / "rally" / "participants.json").read_text(encoding="utf-8"))["participants"]
        r = next((x for x in rows if x["participant_id"] == fm.get("participant")), None)
        if not r:
            sys.exit(f"{fm.get('participant')} not in the Rally export; pass --plate")
        a.plate = f"{r['name']} · {r['company'].split('(internal) ')[-1]}"

    with tempfile.TemporaryDirectory(dir=media_dir(root, fm["project"])) as tmp:
        tmp = Path(tmp)
        clips = []
        for k, t in enumerate(ts):
            voice = a.interviewer_voice if t["speaker"] == "Interviewer" else a.voice
            gap = (ts[k + 1]["t"] - t["t"] - 0.4) if k + 1 < len(ts) else 999
            wav, wpm = tmp / f"l{k:03d}.wav", 180
            dur = say(t["text"], voice, wpm, wav, tmp / "t.txt")
            if dur > gap:
                wpm = min(330, int(wpm * dur / gap) + 6)
                dur = say(t["text"], voice, wpm, wav, tmp / "t.txt")
                if dur > gap:
                    print(f"  warning: {t['block']} runs {dur - gap:.1f}s into the next turn", file=sys.stderr)
            clips.append((t["t"], wav, dur))

        total = clips[-1][0] + clips[-1][2] + 1.5
        pcm = bytearray(int(total * RATE) * 2)
        for start, wav, _ in clips:
            with wave.open(str(wav)) as w:
                data = w.readframes(w.getnframes())
            off = int(start * RATE) * 2
            pcm[off:off + len(data)] = data[: len(pcm) - off]
        with wave.open(str(tmp / "audio.wav"), "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE); w.writeframes(bytes(pcm))

        plates = {"left": a.interviewer, "right": a.plate}
        title = "FluxBench onboarding interview"
        boxes = frame(tmp / "none.png", None, plates, title)
        frame(tmp / "left.png", "left", plates, title)
        frame(tmp / "right.png", "right", plates, title)
        segs = [("none", ts[0]["t"])]
        for k, t in enumerate(ts):
            end = ts[k + 1]["t"] if k + 1 < len(ts) else total
            segs.append(("left" if t["speaker"] == "Interviewer" else "right", end - t["t"]))
        lst = "".join(f"file '{tmp / (s + '.png')}'\nduration {d:.3f}\n" for s, d in segs) + f"file '{tmp / (segs[-1][0] + '.png')}'\n"
        (tmp / "video.txt").write_text(lst, encoding="utf-8")
        run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(tmp / "video.txt"),
             "-i", str(tmp / "audio.wav"), "-vf", f"fps={FPS},format=yuv420p", "-c:v", "libx264", "-tune", "stillimage",
             "-crf", "23", "-c:a", "aac", "-b:a", "96k", "-shortest", "-movflags", "+faststart", str(out)])

    x, y, w, h = boxes["right"]
    print(rel(root, out))
    print(f"uv run _system/scripts/media.py link {a.source} {rel(root, out)} --redact {x - 4},{y - 4},{w + 8},{h + 8}:name-plate")


if __name__ == "__main__":
    main()
