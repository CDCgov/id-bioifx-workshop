#!/usr/bin/env bash
# Full build pipeline: extract text → Jekyll build → search pages → Pagefind index
# Usage: ./scripts/build.sh [--serve]
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

# Activate venv if present
if [[ -d .venv ]]; then
  source .venv/bin/activate
fi

echo "==> Extracting text from local documents..."
python scripts/extract_local.py

echo "==> Building Jekyll site..."
bundle exec jekyll build

echo "==> Generating search pages for embedded content..."
python scripts/build_search_pages.py

echo "==> Building Pagefind index..."
npx -y pagefind@1.5.2 --site _site

echo "==> Build complete."

if [[ "${1:-}" == "--serve" ]]; then
  echo "==> Starting local server (http://127.0.0.1:4000)..."
  bundle exec jekyll serve --skip-initial-build --no-watch
fi
