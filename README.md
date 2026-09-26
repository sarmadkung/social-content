# Personal Content System

Learn → Build → Solve → Document → Teach → Repurpose → Grow

| Folder | What lives there |
| --- | --- |
| `pillars/` | One file per pillar: purpose, audience, ordered topic roadmap |
| `prompts/master-content-prompt.md` | The prompt every post is generated from |
| `linkedin-skills-bundle.txt` | **Derived** — both skills in one paste-able file. Never edit; run `./build-bundle.sh` |
| `generated/drafts/<pillar>/` | Every post, one file each. Its `STATUS:` line (draft → approved → scheduled → published) is the source of truth |
| `generated/quiz/` | Bonus `DSA QUIZ` posts |
| `published/queue.md` | **Generated** posting plan — run `python3 scripts/build_queue.py`, never edit |
| `published/linkedin.md` | Hand-kept log of what went live. No script writes it |
| `sources/inbox.md` | Capture daily ideas here |
| `skills/` | The portable skill files — content, visual, and the index/template |
| `templates/theme.css` | Every colour and font token — change brand colours here only |
| `templates/variant-a…d/` | Layout CSS + example cards (series read `· Example`) for the four variants |
| `visuals/renders/` | Rendered PNGs, ready to upload |
| `visuals/VARIANTS.md` | Which variant to reach for, and why |
| `render.sh` | Re-render templates and post cards; `CHROME=/path ./render.sh` to pick a browser |
| `scripts/validate.py` | Check posts and templates against the rules — run before committing |
| `archive/` | Old versions kept for reference, not in use |
| `build-bundle.sh` | Rebuild the bundle from `skills/` after editing a skill |

## Daily flow
1. Open `published/queue.md` and take today's post.
2. Fill or delete any `[PERSONAL: ...]` line.
3. If the post is `FORMAT: VISUAL`, make the image from the HEADLINE + LAYOUT lines (visual skill). `FORMAT: TEXT` posts go out as words only.
4. Post it.
5. Add a row to `published/linkedin.md` and set the post's `STATUS:` to `published`.
6. Run `python3 scripts/build_queue.py` so it leaves the queue.

## Weekly schedule (5 posts, one per pillar)
| Day | Pillar |
| --- | --- |
| Mon | DSA |
| Tue | AI Engineering |
| Wed | Software Engineering |
| Thu | System Architecture |
| Sun | Dev Growth |

Rebuild the queue after adding or publishing posts: `python3 scripts/build_queue.py`
(it starts from the next Monday; pass a date to override).

## Asking for more
"Generate the next 5 DSA posts using prompts/master-content-prompt.md"
