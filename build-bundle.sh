#!/usr/bin/env bash
# Regenerate linkedin-skills-bundle.txt from skills/ — the bundle is derived,
# never edited by hand. Edit skills/*.skill.md, then run this.
set -euo pipefail
cd "$(dirname "$0")"
{
cat <<'HDR'
You are operating under two skill files that define how LinkedIn content is
written and designed for Muhammad Sarmad. Read both in full before responding.
Follow them as instructions, not as background reading.

Every request starts with a keyword:
  COPY    -> post text only
  VISUAL  -> the image, or the HTML that renders it
  FULL    -> both, text first   (this is the default if no keyword given)

Images are produced by writing HTML/CSS and screenshotting it, never by an image
model — see section 0b of skill 2. The arrangement is chosen from the content's
shape (section 1b) and the rendering variant from section 1a.

==============================================================================
SKILL 1 OF 2 — LINKEDIN CONTENT  (source file: linkedin-content.skill.md)
==============================================================================

HDR
cat skills/linkedin-content.skill.md
printf '\n==============================================================================\nSKILL 2 OF 2 — LINKEDIN VISUAL SYSTEM  (source file: linkedin-visual.skill.md)\n==============================================================================\n\n'
cat skills/linkedin-visual.skill.md
} > linkedin-skills-bundle.txt
echo "linkedin-skills-bundle.txt rebuilt ($(wc -l < linkedin-skills-bundle.txt) lines)"
