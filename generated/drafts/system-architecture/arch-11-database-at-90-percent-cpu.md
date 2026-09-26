SERIES:    SYSTEM ARCHITECTURE #11
TITLE:     Your Database Is at 90% CPU. What Do You Try First?
PILLAR:    System Design & Architecture — for mid-levels in interviews and on call, seniors who get asked "should we shard?"
LEVEL:     INTERMEDIATE
MODE:      SCENARIO
FORMAT:    VISUAL
HEADLINE:  Fix the query before the architecture
LAYOUT:    FLOW
STATUS:    draft
---
Your app is slow at peak. The app servers behind the load balancer sit at 30% CPU. The single database sits at 90%. A big launch is next week.

What would you try first?

Step 0: measure
Find which queries use the CPU. PostgreSQL has pg_stat_statements. MySQL has the slow query log. Guessing wastes a week.

Then try these, in this order. Cheapest and safest first.

1. Fix slow queries and add indexes
An index is a sorted lookup, like the index at the back of a book. Without one, the database reads every row to find a match.
Before: find one user's orders by scanning 5 million rows.
After: an index on user_id jumps straight to their few rows.
Also look for N+1 queries: 1 query for a list, then 1 more for each item.
Why first: often the biggest win, for a small code change.

2. Cache hot reads
The same product page is read 1,000 times a minute. Put it in Redis with a TTL (time to live). Most of those reads never reach the database.
Cost: cached data can be stale.

3. Add read replicas
If most of the load is reads you cannot cache, send them to replicas.
Cost: replication lag. And replicas do not help write load.

4. Scale the database up
Move to a machine with more CPU and RAM. No code change, and it buys time.
Cost: money, and there is a biggest machine.

5. Only then, shard
Split the data across several databases. It is the last step for a reason.

What I would NOT do first
→ Shard right away. It takes weeks and adds permanent complexity. If the real cause was a missing index, you now have four shards each scanning every row.
→ Add more app servers. The load balancer spreads traffic across them, but they all hit the same database. More servers can mean more connections and more load.

Common mistake
Treating "database at 90%" as an architecture problem. It is often one query.

[PERSONAL: one line on a database CPU spike you traced to a single query or missing index]

Takeaway: Fix the query before you fix the architecture.

Next: sharding, for when steps 1 to 4 have truly run out.

#SystemDesign #Databases #PostgreSQL #Performance #SoftwareArchitecture
