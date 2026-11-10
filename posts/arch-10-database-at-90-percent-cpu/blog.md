---
title: "Database at 90% CPU? Fix the query before the architecture"
description: "Your database is at 90% CPU and launch is next week. What to try first, in order: measure, index, cache, read replicas, scale up, and only then shard."
date: 2027-01-27
series: "System Architecture"
seriesNumber: 10
slug: arch-10-database-at-90-percent-cpu
tags: [system-design, databases, postgresql, performance]
cover: cover.png
---

Your app is slow at peak. The app servers behind the load balancer sit at 30% CPU. The single database sits at 90%. A big launch is next week.

What would you try first?

![Fix the query before the architecture](slide-01.png)

## The situation

![Three app servers at 30% CPU, the one database at 90%](slide-02.png)

The app servers are mostly idle: they are waiting on the database. So the slow part is not your app code. Start where the CPU is.

## Step 0: measure

![pg_stat_statements output sorted by total time, with one slow orders query on top](slide-03.png)

Find which queries use the CPU. PostgreSQL has **pg_stat_statements**, an extension that counts every query: how often it ran and how much time it used in total. MySQL has the slow query log.

Sort by total time, which is calls times average time. The query that runs most often is not always the problem; one slow query can use more CPU than a fast one called far more often. Guessing wastes a week.

Then try these, in this order. Cheapest and safest first.

## 1. Fix slow queries and add indexes

![No index: read all 5 million rows. Index on user_id: jump straight to one user's rows](slide-04.png)

An **index** is a sorted lookup the database keeps next to a table, like the index at the back of a book. Without one, the database reads every row to find a match.

- **Before:** find one user's orders by scanning 5 million rows.
- **After:** an index on `user_id` jumps straight to their few rows.

Also look for **N+1 queries**: 1 query for a list, then 1 more for each item. For a list of 100 orders, that is 101 trips to the database instead of one.

Why first: it is often the biggest win, for a small code change. The cost is small but real: every index makes writes a little slower and uses disk, so add the ones your queries use.

## 2. Cache hot reads

![1,000 page reads a minute: Redis answers 999, the database sees 1](slide-05.png)

The same product page is read 1,000 times a minute. Put it in **Redis**, a store that keeps data in memory, with a **TTL** (time to live): how long a cached copy is used before it expires. With a 60-second TTL, most of those reads never reach the database.

Cost: cached data can be stale. If the price changes, some users see the old price until the copy expires. Cache only data that is allowed to be a little old.

## 3. Add read replicas

![The app sends writes to the primary and reads to two replicas; the primary copies every change to them](slide-06.png)

If most of the load is reads you cannot cache, send them to **read replicas**: copies of the database that only answer reads. The primary takes every write and sends each change to the replicas.

Cost: **replication lag**. A user saves a new address, the next page reads from a replica, and shows the old one for a moment. And replicas do not help write load: every write still lands on the primary.

## 4. Scale the database up

![Scale up: a bigger machine, no code change. Shard: split the data, weeks of work](slide-07.png)

Move to a machine with more CPU and RAM. No code change, and it buys time.

Cost: money, and there is a biggest machine.

## 5. Only then, shard

Split the data across several databases. Each piece, a **shard**, holds some of the rows: users A to H on one database, I to P on the next. It is the last step for a reason: it takes weeks of work, and the complexity stays forever.

## What I would NOT do first

![More app servers still hit the one database; four shards with no index each scan all their rows](slide-08.png)

- **Shard right away.** It takes weeks and adds permanent complexity. If the real cause was a missing index, you now have four shards each scanning all of their rows.
- **Add more app servers.** The load balancer spreads traffic across them, but they all hit the same database. More servers can mean more connections and more load.

## Common mistake

Treating "database at 90%" as an architecture problem. It is often one query.

![Often it is just one query: measure, fix the query, cache, replicas, scale up, shard](slide-09.png)

## Keep in mind when your database runs hot

- Sort queries by total time, not by the slowest single call.
- Check the query plan (EXPLAIN) before and after an index.
- Every index slows writes a little. Add only the ones you use.
- Cache only data that is allowed to be a little old.
- Read your own fresh writes from the primary, not a replica.

**In one line:** fix the query before you fix the architecture.

## Next in the series

Sharding, for when steps 1 to 4 have truly run out.
