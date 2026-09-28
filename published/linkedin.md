# Published Log

The record of what actually went live. Kept by hand — no script writes this file.
When a post goes live:
1. Add a row here with the date, series and link. Leave the numbers blank.
2. Set the post's `STATUS:` line to `published`.
3. Re-run `python3 scripts/build_queue.py` so it leaves the queue.
4. Seven days later, copy the numbers from LinkedIn's post analytics into the
   row (Impressions, Reactions, Comments, Reposts, Saves, Followers gained).
5. Run `python3 scripts/report.py` to see what works, by pillar, mode and format.

The Series cell must match the post's `SERIES:` line exactly (e.g. `DSA SERIES #01`),
so the report can join each row to its draft.

| Date | Series | Title | Link | Impressions | Reactions | Comments | Reposts | Saves | Followers | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
