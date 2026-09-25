# Personal Content System

Learn → Build → Solve → Document → Teach → Repurpose → Grow

| Folder | What lives there |
| --- | --- |
| `pillars/` | One file per pillar: purpose, audience, ordered topic roadmap |
| `prompts/master-content-prompt.md` | The prompt every post is generated from |
| `linkedin-skills-bundle.txt` | **Derived** — both skills in one paste-able file. Never edit; run `./build-bundle.sh` |
| `generated/drafts/<pillar>/` | Ready-to-post drafts, one file per post |
| `generated/approved/` | Move a draft here after you edit it |
| `published/linkedin.md` | Posting queue and log |
| `sources/inbox.md` | Capture daily ideas here |
| `skills/` | The portable skill files — content, visual, and the index/template |
| `templates/variant-a…d/` | HTML + CSS that render the four card variants |
| `visuals/renders/` | Rendered PNGs, ready to upload |
| `visuals/VARIANTS.md` | Which variant to reach for, and why |
| `render.sh` | Re-render every template to `visuals/renders/` |
| `build-bundle.sh` | Rebuild the bundle from `skills/` after editing a skill |

## Daily flow
1. Open `published/linkedin.md`, take the next unticked post.
2. Fill any `[PERSONAL: ...]` markers with your real experience.
3. Generate the image from the HEADLINE + LAYOUT lines (visual skill).
4. Post, tick it, add the date.

## Weekly schedule (5 posts, one per pillar)
| Day | Pillar |
| --- | --- |
| Mon | DSA |
| Tue | AI Engineering |
| Wed | Software Engineering |
| Thu | System Architecture |
| Sun | Dev Growth |

Rebuild the queue after adding drafts: `python3 scripts/build_queue.py`

## Asking for more
"Generate the next 5 DSA posts using prompts/master-content-prompt.md"
