TITLE: Database at 90% CPU? Fix the query before the architecture
COVER: cover.png
---

Your app is slow at peak. The app servers sit at 30% CPU. The single database sits at 90%. A big launch is next week. What do you try first?

**Step 0: measure.** Find which queries use the CPU. PostgreSQL has pg_stat_statements; MySQL has the slow query log. Sort by total time, not by how often a query runs. Guessing wastes a week.

Then go in this order, cheapest and safest first:

1. **Fix slow queries and add indexes.** Without an index on `user_id`, finding one user's orders scans 5 million rows. With one, the database jumps straight to their few rows. Also look for N+1 queries. Often the biggest win, for a small change.
2. **Cache hot reads.** A product page read 1,000 times a minute goes in Redis with a TTL. Cost: cached data can be stale.
3. **Add read replicas** for reads you cannot cache. Cost: replication lag, and no help for writes.
4. **Scale the database up.** More CPU and RAM, no code change. Cost: money, and there is a biggest machine.
5. **Only then, shard.** It takes weeks and adds permanent complexity.

**Not first:** sharding (four shards with a missing index each still scan all their rows) or more app servers (they all hit the same database, with more connections).

"Database at 90%" is often one query, not an architecture problem.
