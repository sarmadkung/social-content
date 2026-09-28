#!/usr/bin/env bash
# Render every card template to visuals/renders/ at 1080x1080 @2x,
# then every post card in visuals/week-*/, then every carousel deck in
# visuals/week-*/<post>/ (1080x1350 slides + one PDF for LinkedIn).
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

# Post cards in visuals/week-*/ link straight to templates/<variant>/base.css,
# so they re-render with any change to a variant or to templates/theme.css.
for f in visuals/week-*/*.html; do
  [ -e "$f" ] || continue
  render "$f" "${f%.html}.png"
done

# Carousel decks: visuals/week-*/<post>/NN.html → NN.png at 1080x1350,
# then <post>.pdf — one page per slide, the PNGs as-is (LinkedIn document post).
for dir in visuals/week-*/*/; do
  [ -e "$dir"01.html ] || continue
  deck="$dir.deck.html"
  printf '<!doctype html><html><head><meta charset="utf-8"><style>@page{size:1080px 1350px;margin:0}*{margin:0}img{display:block;width:1080px;height:1350px;break-after:page}</style></head><body>' > "$deck"
  for f in "$dir"[0-9][0-9].html; do
    render "$f" "${f%.html}.png" 1350
    printf '<img src="%s">' "$(basename "${f%.html}.png")" >> "$deck"
  done
  printf '</body></html>' >> "$deck"
  pdf="${dir%/}/$(basename "$dir").pdf"
  "$CHROME_BIN" --headless --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$PWD/$pdf" "file://$PWD/$deck" >/dev/null 2>&1 || true
  rm -f "$deck"
  [ -s "$pdf" ] || { echo "render.sh: FAILED $pdf" >&2; exit 1; }
  echo "  $pdf"
done
