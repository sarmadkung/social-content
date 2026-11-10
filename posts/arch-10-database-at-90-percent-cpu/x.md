Your app is slow at peak. App servers at 30% CPU. The one database at 90%. Big launch next week.

What do you try first?

Not sharding. Here is the order, cheapest and safest first.
[images: slide-01, slide-02]
---
Step 0: measure.

Find which queries use the CPU: pg_stat_statements in PostgreSQL, the slow query log in MySQL.

Sort by total time, not by call count. Guessing wastes a week.
[images: slide-03]
---
1. Fix slow queries and add indexes.

No index on user_id: scan 5 million rows to find one user's orders. With one: jump straight to their few rows.

Often the biggest win, for a small change.
[images: slide-04]
---
2. Cache hot reads (cost: stale data)
3. Read replicas for reads you can't cache (cost: lag, no help for writes)
4. Scale the database up (cost: money, a biggest machine)
5. Only then, shard
[images: slide-05, slide-06, slide-07]
---
Not first: more app servers. They all hit the same one database, with more connections.

Not first: sharding. If the cause was a missing index, four shards each still scan all their rows.
[images: slide-08, slide-09]
---
"Database at 90%" is often one query, not an architecture problem.

Fix the query before you fix the architecture.

Next: sharding, for when steps 1 to 4 have truly run out.

#SystemDesign #PostgreSQL
