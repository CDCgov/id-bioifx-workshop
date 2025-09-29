#!/usr/bin/env bash
# Convert Markdown files to DOCX using pandoc.
# Usage:
#   scripts/md2docx.sh file1.md file2.md ...
#   scripts/md2docx.sh -a              # convert all markdown (excluding _site, node_modules, vendor)
# Options:
#   -o DIR          Output directory (created if missing)
#   -t TEMPLATE     Reference DOCX (pandoc --reference-doc)
#   -a              All markdown files
#   -f              Force overwrite existing .docx
#   -h              Help
#
# Examples:
#   scripts/md2docx.sh README.md
#   scripts/md2docx.sh -o exports -a
#   scripts/md2docx.sh -t reference.docx index.md
#
# Requires: pandoc
set -euo pipefail

force=0
all=0
out_dir=""
reference=""

die(){ echo "Error: $*" >&2; exit 1; }

have(){ command -v "$1" >/dev/null 2>&1; }

usage(){ grep '^# ' "$0" | sed 's/^# \{0,1\}//'; exit 0; }

while getopts ":o:t:afh" opt; do
  case "$opt" in
    o) out_dir="$OPTARG" ;;
    t) reference="$OPTARG" ;;
    a) all=1 ;;
    f) force=1 ;;
    h) usage ;;
    :) die "Option -$OPTARG requires an argument" ;;
    \?) die "Unknown option -$OPTARG" ;;
  esac
done
shift $((OPTIND-1))

have pandoc || die "pandoc not found. Install: brew install pandoc"

# Collect files
files=()
if [[ $all -eq 1 ]]; then
  while IFS= read -r -d '' f; do
    files+=("$f")
  done < <(find . -type f -name '*.md' \
      -not -path './_site/*' \
      -not -path './node_modules/*' \
      -not -path './vendor/*' \
      -not -name 'Gemfile.lock' -print0)
else
  if [[ $# -lt 1 ]]; then
    die "No input files provided (use -a for all or list specific .md files)"
  fi
  for f in "$@"; do
    [[ -f $f ]] || die "Input not found: $f"
    [[ ${f##*.} == md ]] || die "Not markdown: $f"
    files+=("$f")
  done
fi

[[ ${#files[@]} -gt 0 ]] || die "No markdown files matched"

# Prepare output dir
if [[ -n $out_dir ]]; then
  mkdir -p "$out_dir"
fi

convert(){
  local src="$1"
  local base
  base=$(basename "${src%.md}")
  local dest
  if [[ -n $out_dir ]]; then
    dest="$out_dir/$base.docx"
  else
    dest="${src%.md}.docx"
  fi
  if [[ -f $dest && $force -ne 1 ]]; then
    echo "Skip (exists): $dest" >&2
    return 0
  fi
  local cmd=(pandoc "$src" -f markdown -t docx -o "$dest")
  if [[ -n $reference ]]; then
    [[ -f $reference ]] || die "Reference docx not found: $reference"
    cmd+=(--reference-doc="$reference")
  fi
  # You can tweak metadata mapping here if needed
  echo "-> $dest"
  "${cmd[@]}"
}

echo "Converting ${#files[@]} file(s)..." >&2
for f in "${files[@]}"; do
  convert "$f"
done

echo "Done."
