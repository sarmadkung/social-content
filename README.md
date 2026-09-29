# Personal Content System

Learn → Build → Solve → Document → Teach → Repurpose → Grow

| Folder | What lives there |
| --- | --- |
| `pillars/` | One file per pillar: purpose, audience, ordered roadmap. Each line is `#NN Title · MODE · needs #..` — the post's content mode and the earlier posts it builds on. Pillars 06 Building and 07 For Business have no roadmap |
| `prompts/master-content-prompt.md` | The prompt every post is generated from |
| `linkedin-skills-bundle.txt` | **Derived** — both skills in one paste-able file. Never edit; run `./build-bundle.sh` |
| `generated/drafts/<pillar>/` | Every post, one file each. `MODE:` must match the roadmap. Drafts follow roadmap order: a number cannot be skipped once a later post exists (later roadmap topics show in the queue as "write" slots). Its `STATUS:` line (draft → approved → scheduled → published) is the source of truth |
| `generated/quiz/` | Bonus `DSA QUIZ` posts |
| `posts/<post>/` | **Generated** ready-to-post folder, made only for posts you prepare (`/create-post` or `python3 scripts/build_posts.py <post>`): `post.md` (LinkedIn text) + `1.png`, `2.png` … (images in order, shared by every platform), `dailydev.md` + `cover.png` (daily.dev), `instagram.md` (Instagram caption), `x.md` (X thread). Image sources in `src/`. `posts/README.md` counts every post and says which are ready |
| `published/queue.md` | **Generated** posting plan — run `python3 scripts/build_queue.py`, never edit |
| `published/linkedin.md` | Hand-kept log of what went live, with each post's numbers after 7 days. No script writes it |
| `published/report.md` | **Generated** — what works, by pillar, mode and format. Run `python3 scripts/report.py` |
| `sources/inbox.md` | Capture daily ideas here |
| `sources/project-log.md` | Raw notes every two weeks on real projects — the only source for BUILDING posts |
| `sources/apps.md` | My own apps — the only source for FOR BUSINESS PRODUCT posts |
| `skills/` | The portable skill files — content, visual, and the index/template |
| `templates/theme.css` | Every colour and font token — change brand colours here only |
| `templates/variant-a…d/` | Layout CSS + example cards (series read `· Example`) for the four variants |
| `visuals/renders/` | Rendered template examples |
| `visuals/VARIANTS.md` | Which variant to reach for, and why |
| `render.sh` | Re-render templates and every `posts/*/src/` image; `CHROME=/path ./render.sh` to pick a browser |
| `scripts/validate.py` | Check posts and templates against the rules — run before committing |
| `archive/` | Old versions kept for reference, not in use |
| `build-bundle.sh` | Rebuild the bundle from `skills/` after editing a skill |

## Daily flow
1. Open `posts/README.md` (or `published/queue.md`) and take today's post.
2. Fill or delete any `[PERSONAL: ...]` line in the draft. Verify each `[FACT_CHECK: ...]` claim (fix or cut it if wrong), then delete the marker. Re-run `python3 scripts/build_queue.py`.
3. If the post is `FORMAT: VISUAL` and has no images yet, make them in `posts/<post>/src/` (visual skill) and run `./render.sh`. A carousel is `slide-01.html` …, posted as `carousel.pdf` on LinkedIn, the PNGs on Instagram. `FORMAT: TEXT` posts go out as words only.
4. Post it: on LinkedIn paste `posts/<post>/post.md` and attach `1.png`, `2.png` … in order; on Instagram post the same images as a carousel with `instagram.md` as the caption; on daily.dev use `dailydev.md` with `cover.png`; on X post `x.md` as a thread, attaching the images each post names. `post.md` is the draft minus the sections the images show; the draft itself is never trimmed.
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
