#!/usr/bin/env bash
# Render every card template to visuals/renders/ at 1080x1080 @2x.
#   ./render.sh              → all variants
#   ./render.sh variant-c    → one variant
set -euo pipefail
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
mkdir -p visuals/renders
for dir in templates/${1:-variant-*}/; do
  v=$(basename "$dir"); [ "$v" = "_archived-split" ] && continue
  letter=${v#variant-}
  for f in "$dir"*.html; do
    [ -e "$f" ] || continue
    out="visuals/renders/${letter}-$(basename "$f" .html).png"
    "$CHROME" --headless --disable-gpu --hide-scrollbars \
      --force-device-scale-factor=2 --window-size=1080,1080 \
      --screenshot="$PWD/$out" --virtual-time-budget=1500 \
      "file://$PWD/$f" >/dev/null 2>&1
    echo "  $out"
  done
done

# Post cards in visuals/week-*/ link straight to templates/<variant>/base.css,
# so they re-render with any change to a variant.
for f in visuals/week-*/*.html; do
  [ -e "$f" ] || continue
  "$CHROME" --headless --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=2 --window-size=1080,1080 \
    --screenshot="$PWD/${f%.html}.png" --virtual-time-budget=1500 \
    "file://$PWD/$f" >/dev/null 2>&1
  echo "  ${f%.html}.png"
done
