#!/usr/bin/env bash
# Regenerate linkedin-skills-bundle.txt from skills/ — the bundle is derived,
# never edited by hand. Edit skills/*.skill.md, then run this.
set -euo pipefail
cd "$(dirname "$0")"
{
cat <<'HDR'
You are operating under two skill files that define how LinkedIn content is
written and designed for Muhammad Sarmad. Read both in full before responding
and follow them as instructions. This header adds nothing of its own: request
keywords, post format and visual rules are all defined inside the skills below.

==============================================================================
SKILL 1 OF 2 — LINKEDIN CONTENT  (source file: skills/linkedin-content.skill.md)
==============================================================================

HDR
cat skills/linkedin-content.skill.md
printf '\n==============================================================================\nSKILL 2 OF 2 — LINKEDIN VISUAL SYSTEM  (source file: skills/linkedin-visual.skill.md)\n==============================================================================\n\n'
cat skills/linkedin-visual.skill.md
} > linkedin-skills-bundle.txt
echo "linkedin-skills-bundle.txt rebuilt ($(wc -l < linkedin-skills-bundle.txt) lines)"
