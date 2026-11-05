#!/usr/bin/env bash
# provenance.sh <skill> <action> <target-id> [model]
set -euo pipefail
root="$(cd "$(dirname "$0")/../.." && pwd)"
printf '%s\t%s\t%s\t%s\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "${1:?skill}" "${2:?action}" "${3:?target}" "${4:-claude-fable-5-1}" >> "$root/_system/provenance.log"
