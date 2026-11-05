#!/usr/bin/env bash
# Installs a pre-commit hook that blocks commits containing emails, phone numbers, or participant names.
set -euo pipefail
root="$(git rev-parse --show-toplevel)"
hook="$root/.git/hooks/pre-commit"
cat > "$hook" <<'HOOK'
#!/bin/sh
if git diff --cached --name-only | grep -q '^_raw/'; then
  echo "pre-commit: refusing to commit files under _raw/" >&2; exit 1
fi
python3 _system/scripts/scan_pii.py --staged || { echo "pre-commit: identity leak suspected, commit blocked" >&2; exit 1; }
HOOK
chmod +x "$hook"
echo "installed $hook"
