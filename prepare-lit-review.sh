#!/usr/bin/env bash
# Prepare ./lit-review for rendering. Quarto skips README.md files, so each
# one becomes index.md (its folder's landing page) and links to it are rewritten.
#
# Locally, pass the path to your lit-review checkout to copy it in first:
#   ./prepare-lit-review.sh ../lit-review
# In CI, lit-review is already checked out at ./lit-review.
set -euo pipefail
cd "$(dirname "$0")"

if [ $# -ge 1 ]; then
  [ -L lit-review ] && rm lit-review
  rsync -a --delete --exclude .git "$1"/ lit-review/
fi

find lit-review -name README.md -not -path '*/_*' | while read -r f; do
  mv "$f" "$(dirname "$f")/index.md"
done
find lit-review -name '*.md' -not -path '*/_*' -exec sed -i.bak -E 's#\(([^)]*/)?README\.md\)#(\1index.md)#g' {} +
find lit-review -name '*.md.bak' -delete

# Home page status (also re-run by the pre-render hook)
python3 scripts/status.py
