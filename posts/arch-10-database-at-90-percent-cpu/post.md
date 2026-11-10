> ⚠ NOT READY — resolve these, then delete this block:
> - [PERSONAL: one line on a database CPU spike you traced to a single query or missing index]

---

Your app is slow at peak.

The app servers sit at 30% CPU. The single database sits at 90%. A big launch is next week.

What would you try first?

Most of us reach for the big fix: shard the database, or add more servers. Both take time, and neither helps if the real cause is one slow query.

The slides walk through it in order, cheapest and safest first:

0. Measure: find the query that uses the CPU
1. Fix slow queries and add the missing index
2. Cache hot reads
3. Read replicas for reads you can't cache
4. Scale the database up
5. Only then, shard

And what I would not do first, and why.

Treating "database at 90%" as an architecture problem is the common mistake. It is often one query.

Fix the query before you fix the architecture.

Next: sharding, for when steps 1 to 4 have truly run out.

#SystemDesign #Databases #PostgreSQL #Performance #SoftwareArchitecture
