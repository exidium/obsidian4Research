#!/usr/bin/env bash
# Local transcription on Apple Silicon. Media never leaves the machine.
#   transcribe.sh <media-file> <out-dir> [model] [language]
# Prints the path of the Whisper JSON on the last line.
set -euo pipefail
media="${1:?media file}"; out="${2:?output dir}"
model="${3:-mlx-community/whisper-large-v3-turbo}"
lang="${4:-}"
command -v ffmpeg >/dev/null || { echo "ffmpeg missing: brew install ffmpeg" >&2; exit 2; }
command -v mlx_whisper >/dev/null || { echo "mlx_whisper missing: uv tool install mlx-whisper" >&2; exit 2; }
mkdir -p "$out"
base="$(basename "${media%.*}")"
wav="$out/$base.16k.wav"
ffmpeg -y -loglevel error -i "$media" -ac 1 -ar 16000 -vn "$wav"
args=(--model "$model" --output-format json --output-dir "$out" --verbose False)
[ -n "$lang" ] && args+=(--language "$lang")
mlx_whisper "$wav" "${args[@]}"
rm -f "$wav"
echo "$out/$base.json"
