#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Build a source note (transcript with stable block IDs) from a transcript file.

Accepts: Whisper JSON (mlx_whisper --output-format json), .srt, .vtt (incl. Teams <v Name>),
Dovetail markdown export ("**Name (m:ss):** text"), or plain .txt/.md with "Speaker: text"
paragraphs and optional leading [hh:mm:ss].

  build_source.py --input FILE --project 2026_demo-fluxbench --participant P-001 \
      [--source-id S-0004] [--date 2026-10-14] [--entry-type interview] [--methodology user-interview] \
      [--participant-type external-customer] [--role "RF engineer"] [--interviewer P-000] [--rally-id X] \
      [--title "[Interview] P-001 - 14 Oct 2026"] [--language en] [--origin _raw/...] [--transcriber mlx-whisper/large-v3-turbo] \
      [--speaker-map "Jane Doe=P-001,Moderator=Interviewer"] [--gap 2.0] [--max-chars 700]

Names in speaker labels that are not mapped are replaced by Speaker-1, Speaker-2 … and reported,
so a name never lands in the vault by accident.
"""
import argparse, json, re, subprocess, sys
from datetime import date
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from vaultlib import vault_root, write_note, DIRS

ap = argparse.ArgumentParser()
ap.add_argument("--input", required=True)
ap.add_argument("--project", required=True)
ap.add_argument("--participant", required=True)
ap.add_argument("--source-id")
ap.add_argument("--date", default=str(date.today()))
ap.add_argument("--entry-type", default="interview", choices=["interview","workshop","feedback","survey","test","observation","demo","diary"])
ap.add_argument("--methodology", default="user-interview", choices=["user-interview","usability-test","workshop","survey","guerilla-testing","demo","card-sorting","diary-study"])
ap.add_argument("--participant-type", default="external-customer", choices=["external-customer","internal-stakeholder","internal-engineer"])
ap.add_argument("--role", default="")
ap.add_argument("--interviewer", default="P-000")
ap.add_argument("--rally-id", default="")
ap.add_argument("--title")
ap.add_argument("--language", default="en")
ap.add_argument("--origin", default="")
ap.add_argument("--transcriber", default="manual")
ap.add_argument("--duration-min", type=int)
ap.add_argument("--speaker-map", default="")
ap.add_argument("--gap", type=float, default=2.0)
ap.add_argument("--max-chars", type=int, default=700)
ap.add_argument("--dry-run", action="store_true")
a = ap.parse_args()

root = vault_root()
proj_dir = root / "10 Projects" / a.project
if not proj_dir.exists():
    sys.exit(f"project folder not found: {proj_dir}")
sid = a.source_id or subprocess.check_output([sys.executable, str(Path(__file__).parent / "next_id.py"), "source"], text=True).strip()
sid_l = sid.replace("-", "").lower()

smap = {}
for pair in filter(None, a.speaker_map.split(",")):
    k, v = pair.split("=", 1)
    smap[k.strip().lower()] = v.strip()
SAFE = re.compile(r"^(interviewer|moderator|facilitator|observer|note|p-\d{3}|speaker-\d+)$", re.I)
unmapped = {}

def map_speaker(name):
    if not name:
        return None
    n = name.strip()
    if n.lower() in smap:
        return smap[n.lower()]
    if SAFE.match(n):
        return n[0].upper() + n[1:] if n.lower() == "interviewer" else n
    if n not in unmapped:
        unmapped[n] = f"Speaker-{len(unmapped) + 1}"
    return unmapped[n]

def ts(sec):
    sec = int(sec); return f"[{sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d}]"

def parse_ts(s):
    h, m, rest = s.replace(",", ".").split(":"); return int(h) * 3600 + int(m) * 60 + float(rest)

# ---- parse into cues: (start_sec|None, speaker|None, text)
src = Path(a.input)
raw = src.read_text(encoding="utf-8", errors="replace")
cues = []
if src.suffix.lower() == ".json":
    for s in json.loads(raw)["segments"]:
        cues.append((float(s["start"]), float(s["end"]), None, s["text"].strip()))
elif src.suffix.lower() in (".srt", ".vtt"):
    for block in re.split(r"\n\s*\n", raw.strip()):
        lines = [l for l in block.splitlines() if l.strip()]
        if not lines or lines[0].startswith(("WEBVTT", "NOTE")):
            continue
        tl = next((l for l in lines if "-->" in l), None)
        if not tl:
            continue
        start, end = [parse_ts(x.strip().split(" ")[0]) for x in tl.split("-->")]
        text = " ".join(lines[lines.index(tl) + 1:])
        spk = None
        m = re.match(r"<v\s+([^>]+)>(.*?)(</v>)?$", text)
        if m:
            spk, text = m.group(1), m.group(2)
        else:
            m = re.match(r"([^:]{1,40}):\s+(.*)", text)
            if m:
                spk, text = m.group(1), m.group(2)
        cues.append((start, end, spk, text.strip()))
elif re.search(r"^\*\*[^*]+ \(\d+:\d{2}(?::\d{2})?\):\*\* ", raw, re.M):   # Dovetail export (line-based)
    SPK = re.compile(r"^\*\*(.+?) \((\d+):(\d{2})(?::(\d{2}))?\):\*\*\s*(.*)")
    NOTE = re.compile(r"^\*\*Unknown speaker:\*\*\s*(.*)")
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith(("[AudioVideo", "#### Transcript", "[Audio", "[Video")):
            continue
        m = SPK.match(line)
        if m:
            h, mi, se = (int(m.group(2)), int(m.group(3)), int(m.group(4))) if m.group(4) else (0, int(m.group(2)), int(m.group(3)))
            cues.append([h * 3600 + mi * 60 + se, None, m.group(1), m.group(5).strip()]); continue
        m = NOTE.match(line)
        if m:
            cues.append([None, None, "Note", m.group(1).strip().replace("\\[", "[").replace("\\]", "]")]); continue
        if cues:
            cues[-1][3] = (cues[-1][3] + " " + line).strip()      # continuation line of the previous turn
        else:
            cues.append([None, None, None, line])
else:
    for para in re.split(r"\n\s*\n", raw.strip()):
        text = " ".join(l.strip() for l in para.splitlines())
        start = None
        m = re.match(r"\[(\d{1,2}:\d{2}:\d{2})\]\s*(.*)", text)
        if m:
            start, text = parse_ts(m.group(1)), m.group(2)
        spk = None
        m = re.match(r"\*{0,2}([^:*]{1,40}?)\*{0,2}:\s+(.*)", text)
        if m:
            spk, text = m.group(1), m.group(2)
        cues.append((start, start, spk, text))

# ---- group cues into paragraphs
paras = []  # [start, speaker, text]
for start, end, spk, text in cues:
    spk = map_speaker(spk)
    if paras and start is not None and paras[-1][3] is not None:
        last = paras[-1]
        same_spk = (spk == last[1])
        close = (start - last[3]) < a.gap
        if same_spk and close and len(last[2]) + len(text) < a.max_chars:
            last[2] += " " + text; last[3] = end; continue
    paras.append([start, spk, text, end])

lines = []
for i, (start, spk, text, _) in enumerate(paras, 1):
    head = (ts(start) + " ") if start is not None else ""
    who = f"**{spk}:** " if spk else ""
    lines.append(f"{head}{who}{text} ^{sid_l}-{i:04d}")
transcript = "\n\n".join(lines)

duration = a.duration_min
if duration is None and paras and paras[-1][3]:
    duration = int(round(paras[-1][3] / 60))

from datetime import date as _d
pretty = _d.fromisoformat(a.date).strftime("%d %b %Y")
fm = {
    "type": "source", "source_id": sid, "project": a.project,
    "title": a.title or f"[{a.entry_type.capitalize()}] {a.participant} - {pretty}",
    "entry_type": a.entry_type, "methodology": a.methodology,
    "participant": a.participant, "participant_type": a.participant_type, "role": a.role, "software_used": [],
    "interviewer": a.interviewer, "rally_id": a.rally_id, "date": a.date,
    "duration_min": duration, "language": a.language, "origin": a.origin or str(src),
    "transcriber": a.transcriber, "speakers_inferred": False, "redacted": False, "ris_status": "raw",
}
body = f"\n## Summary\n-\n\n## Transcript\n{transcript}\n"
out = proj_dir / DIRS["sources"] / f"{sid}.md"
if a.dry_run:
    print(body[:1500]); sys.exit()
out.parent.mkdir(parents=True, exist_ok=True)
if out.exists():
    sys.exit(f"refusing to overwrite existing source {out}")
write_note(out, fm, body)
print(f"wrote {out.relative_to(root)}  paragraphs={len(paras)}  duration_min={duration}")
if unmapped:
    print("WARNING unmapped speaker names were replaced; add them to --speaker-map and re-run if needed:")
    for k, v in unmapped.items():
        print(f"  {v}  <-  (name withheld, {len(k)} chars)")
