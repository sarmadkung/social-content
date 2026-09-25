# Portable Skill Library

Model-agnostic skills. Each file is one skill, written so it can be handed to
any AI model — Claude Code, ChatGPT, Gemini, a local model — without editing.

## How to use

**ChatGPT / any chat model** — open the skill file, click **Raw**, copy the
whole thing into the conversation, then state your task. The raw URL can also be
pasted directly for models that fetch links.

**Claude Code** — save a skill as `~/.claude/skills/<name>/SKILL.md` and invoke
it with `/<name>`, or paste the file inline like any other model.

**As a system prompt** — drop the body (everything below the front matter) into
the system prompt / custom-instructions field.

## Index

| Skill | What it does | When to use it |
| --- | --- | --- |
| `linkedin-content.skill.md` | Content system for Muhammad Sarmad's LinkedIn — positioning, three pillars, series, tone | Writing, planning, or reviewing a LinkedIn post |
| `linkedin-visual.skill.md` | Visual system for LinkedIn images — locked dark identity, four variants, per-pillar accent | Generating a post image, code graphic, or carousel |
| `TEMPLATE.skill.md` | Blank skill scaffold | Writing a new skill |

## Writing a new skill

Copy `TEMPLATE.skill.md`, name the file `<kebab-case-name>.skill.md`, fill it
in, and add a row to the index above.

Rules that keep a skill portable:

1. Write instructions, not conversation — the model is the reader.
2. Name the trigger explicitly ("use this when ...") so any harness can route.
3. Never assume a specific tool exists; describe the *action*, and list tools as
   optional accelerators.
4. Keep steps numbered and imperative.
5. Put examples last — models weight the end of a prompt heavily.




