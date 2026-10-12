#!/usr/bin/env bash
# Build posts/<post>/carousel.pdf — the LinkedIn document post that shows as a
# swipeable carousel (images attached directly show as a grid, not a swipe).
# One page per image, the PNGs as-is, in posting order:
#   slide-01.png, slide-02.png …  (carousel decks, 1080x1350), else
#   0.png, 1.png, 2.png …         (feed images, 1080x1080; 0 = feed cover)
# carousel.pdf is a build output: git-ignored, rebuilt from the PNGs.
# The PDF's title metadata comes from carousel-title.txt in the post folder —
# the same line you type into LinkedIn's "document title" box on upload.
#   scripts/carousel_pdf.sh                    → every post with images
#   scripts/carousel_pdf.sh posts/ai-01-ai-foundations [...]
#   CHROME=/path/to/chrome scripts/carousel_pdf.sh
set -euo pipefail
cd "$(dirname "$0")/.."

find_chrome() {
  if [ -n "${CHROME:-}" ]; then echo "$CHROME"; return; fi
  for c in google-chrome google-chrome-stable chromium chromium-browser; do
    command -v "$c" >/dev/null 2>&1 && { command -v "$c"; return; }
  done
  for c in "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
           "/Applications/Chromium.app/Contents/MacOS/Chromium"; do
    [ -x "$c" ] && { echo "$c"; return; }
  done
  echo "carousel_pdf.sh: no Chrome/Chromium found — set CHROME=/path/to/chrome" >&2
  exit 1
}
CHROME_BIN=$(find_chrome)

if [ $# -gt 0 ]; then posts=("$@"); else posts=(posts/*/); fi

for post in "${posts[@]}"; do
  post=${post%/}
  if ls "$post"/slide-[0-9][0-9].png >/dev/null 2>&1; then
    w=1080; h=1350
    imgs=$(cd "$post" && ls slide-[0-9][0-9].png)
  elif ls "$post"/[0-9]*.png >/dev/null 2>&1; then
    w=1080; h=1080
    imgs=$(cd "$post" && ls [0-9]*.png | grep -E '^[0-9]+\.png$' | sort -n)
  else
    continue
  fi
  deck="$post/.deck.html"
  title=$(head -1 "$post/carousel-title.txt" 2>/dev/null \
          | sed 's/&/\&amp;/g; s/</\&lt;/g; s/>/\&gt;/g')
  [ -n "$title" ] || echo "carousel_pdf.sh: $post has no carousel-title.txt" >&2
  printf '<!doctype html><html><head><meta charset="utf-8"><title>%s</title><style>' "$title" > "$deck"
  printf '@page{size:%spx %spx;margin:0}*{margin:0}img{display:block;width:%spx;height:%spx;break-after:page}</style></head><body>' "$w" "$h" "$w" "$h" >> "$deck"
  for img in $imgs; do printf '<img src="%s">' "$img" >> "$deck"; done
  printf '</body></html>' >> "$deck"
  pdf="$post/carousel.pdf"
  rm -f "$pdf"
  "$CHROME_BIN" --headless --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$PWD/$pdf" "file://$PWD/$deck" >/dev/null 2>&1 || true
  rm -f "$deck"
  [ -s "$pdf" ] || { echo "carousel_pdf.sh: FAILED $pdf" >&2; exit 1; }
  echo "  $pdf ($(echo $imgs | wc -w | tr -d ' ') pages)"
done
