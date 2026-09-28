# Personal Content System

Learn → Build → Solve → Document → Teach → Repurpose → Grow

| Folder | What lives there |
| --- | --- |
| `pillars/` | One file per pillar: purpose, audience, ordered roadmap. Each line is `#NN Title · MODE · needs #..` — the post's content mode and the earlier posts it builds on. Pillars 06 Building and 07 For Business have no roadmap |
| `prompts/master-content-prompt.md` | The prompt every post is generated from |
| `linkedin-skills-bundle.txt` | **Derived** — both skills in one paste-able file. Never edit; run `./build-bundle.sh` |
| `generated/drafts/<pillar>/` | Every post, one file each. `MODE:` must match the roadmap; no roadmap number may be skipped. Its `STATUS:` line (draft → approved → scheduled → published) is the source of truth |
| `generated/quiz/` | Bonus `DSA QUIZ` posts |
| `published/queue.md` | **Generated** posting plan — run `python3 scripts/build_queue.py`, never edit |
| `published/linkedin.md` | Hand-kept log of what went live, with each post's numbers after 7 days. No script writes it |
| `published/report.md` | **Generated** — what works, by pillar, mode and format. Run `python3 scripts/report.py` |
| `sources/inbox.md` | Capture daily ideas here |
| `sources/project-log.md` | Raw notes every two weeks on real projects — the only source for BUILDING posts |
| `sources/apps.md` | My own apps — the only source for FOR BUSINESS PRODUCT posts |
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
3. If the post is `FORMAT: VISUAL`, make the image from the HEADLINE + LAYOUT lines (visual skill). If `LAYOUT: CAROUSEL`, make one slide per `SLIDES:` line and post a PDF on LinkedIn, the images on Instagram. `FORMAT: TEXT` posts go out as words only.
4. Post it.
5. Add a row to `published/linkedin.md` and set the post's `STATUS:` to `published`.
6. Run `python3 scripts/build_queue.py` so it leaves the queue.
7. Seven days later, fill that row's numbers from LinkedIn analytics and run `python3 scripts/report.py`.

## Weekly schedule (5 posts, rotating through 7 pillars)
Seven pillars are the content inventory; five posts a week (Mon–Fri) is what
goes out. Each posting day takes the next pillar in this order:

DSA → AI Engineering → Software Engineering → Building → System Architecture → For Business → Dev Growth

Change the pace in `scripts/build_queue.py` (`POSTS_PER_WEEK`) or for one run
with `--per-week 3..7`.

Rebuild the queue after adding or publishing posts: `python3 scripts/build_queue.py`
(it starts from the next Monday; pass a date to override).

## Asking for more
"Generate the next 5 DSA posts using prompts/master-content-prompt.md"
