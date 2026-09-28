#!/usr/bin/env bash
# Render every card template to visuals/renders/ at 1080x1080 @2x, then every
# post's images from posts/<post>/src/:
#   src/1.html, src/2.html …   → posts/<post>/1.png, 2.png … (1080x1080)
#   src/slide-01.html …        → posts/<post>/slide-01.png … (1080x1350) + carousel.pdf
#   ./render.sh                         → all variants + post cards
#   ./render.sh variant-c               → one variant (post cards still render)
#   CHROME=/path/to/chrome ./render.sh  → use a specific browser binary
set -euo pipefail
cd "$(dirname "$0")"

find_chrome() {
  if [ -n "${CHROME:-}" ]; then echo "$CHROME"; return; fi
  for c in google-chrome google-chrome-stable chromium chromium-browser; do
    command -v "$c" >/dev/null 2>&1 && { command -v "$c"; return; }
  done
  for c in "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
           "/Applications/Chromium.app/Contents/MacOS/Chromium"; do
    [ -x "$c" ] && { echo "$c"; return; }
  done
  echo "render.sh: no Chrome/Chromium found — set CHROME=/path/to/chrome" >&2
  exit 1
}
CHROME_BIN=$(find_chrome)

render() {  # render <html> <png> [height]
  local html=$1 png=$2 h=${3:-1080} log
  rm -f "$png"
  log=$("$CHROME_BIN" --headless --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=2 --window-size=1080,$h \
    --screenshot="$PWD/$png" --virtual-time-budget=1500 \
    "file://$PWD/$html" 2>&1) || true
  if [ ! -s "$png" ]; then
    echo "render.sh: FAILED $html" >&2
    echo "$log" | tail -5 >&2
    exit 1
  fi
  echo "  $png"
}

mkdir -p visuals/renders
for dir in templates/${1:-variant-*}/; do
  v=$(basename "$dir")
  letter=${v#variant-}
  for f in "$dir"*.html; do
    [ -e "$f" ] || continue
    render "$f" "visuals/renders/${letter}-$(basename "$f" .html).png"
  done
done

# Post images link straight to templates/<variant>/base.css, so they
# re-render with any change to a variant or to templates/theme.css.
for f in posts/*/src/[0-9]*.html; do
  [ -e "$f" ] || continue
  post=${f%/src/*}
  render "$f" "$post/$(basename "${f%.html}").png"
done

# Carousel decks: src/slide-NN.html → slide-NN.png at 1080x1350, then
# carousel.pdf — one page per slide, the PNGs as-is (LinkedIn document post).
for post in posts/*/; do
  [ -e "${post}src/slide-01.html" ] || continue
  deck="${post}.deck.html"
  printf '<!doctype html><html><head><meta charset="utf-8"><style>@page{size:1080px 1350px;margin:0}*{margin:0}img{display:block;width:1080px;height:1350px;break-after:page}</style></head><body>' > "$deck"
  for f in "${post}"src/slide-[0-9][0-9].html; do
    png="${post}$(basename "${f%.html}").png"
    render "$f" "$png" 1350
    printf '<img src="%s">' "$(basename "$png")" >> "$deck"
  done
  printf '</body></html>' >> "$deck"
  pdf="${post}carousel.pdf"
  "$CHROME_BIN" --headless --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$PWD/$pdf" "file://$PWD/$deck" >/dev/null 2>&1 || true
  rm -f "$deck"
  [ -s "$pdf" ] || { echo "render.sh: FAILED $pdf" >&2; exit 1; }
  echo "  $pdf"
done
