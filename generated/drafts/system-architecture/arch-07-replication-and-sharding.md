SERIES:    SYSTEM ARCHITECTURE #07
TITLE:     Replication and Sharding: Copy the Data, Then Split It
PILLAR:    System Design & Architecture — for mid-levels in design interviews, juniors who have only ever used one database, seniors for the lag trade-off
LEVEL:     INTERMEDIATE
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Replication copies the data. Sharding splits it.
LAYOUT:    FLOW
VISUALS:   1 = How do read replicas share the load? · 2 = Why does a user see their old data after saving? · 3 = How does a shard know which rows it owns? · 4 = What does sharding cost you? · 5 = Takeaway · rest = text
STATUS:    draft
---
Your app servers scale out easily. Your single database does not. It becomes the bottleneck.

You fixed the slow queries, cached the hot reads and bought a bigger machine (#06). It is still not enough.
Now you have two moves left: copy the database, or split it.

Part 1: replication
Replication means keeping copies of the same database on more than one server. The copies are called replicas.
In the common setup, one primary database takes all writes. It sends every change to read replicas, which serve read queries.
Think of a teacher writing on the main board. Students copy it into their notebooks. Everyone can read a notebook, but only the teacher writes on the board.

Why do we need it?
Most apps read far more than they write. Think of a feed: many views, few posts. Replicas spread those reads. They also give you a standby copy if the primary fails.

How do read replicas share the load?
→ Writes go to the primary only
→ Reads can go to any replica
→ Replication lag: replicas can be a little behind the primary
→ Asynchronous replication is faster but can lose recent writes on failure. Synchronous is safer but slows every write
→ Failover: promoting a replica to primary when the primary dies
Takeaway: replicas scale reads, not writes, and they are always a little behind.

Where is it used?
PostgreSQL streaming replication, MySQL replication, Amazon RDS and Aurora read replicas, MongoDB replica sets.

Why does a user see their old data after saving?
The lag trap:
1. A user updates their profile name. The write goes to the primary.
2. The page reloads and reads from a replica.
3. The replica has not caught up yet.
4. The user sees their old name and thinks the save failed.
Fix: read-your-writes. Send a user's reads to the primary for a short time after they write.
Takeaway: right after a write, read from the primary, not a replica.

[PERSONAL: one line on a replication-lag bug or failover you handled]

When replication is not enough
Use it: read-heavy apps, or when you need a hot standby.
Not enough: when writes are the bottleneck. Replicas copy every write, so they do not reduce write load. They also do not fix a table too big for one machine.

Part 2: sharding
Sharding splits one logical table across several machines. Each shard holds a different slice of the rows, and something up front decides which shard owns a given row.
That decision is the whole design.

Why do we need it?
Because vertical scaling ends. There is a biggest machine you can rent, and it costs more than several smaller ones.

[FACT_CHECK: The biggest rentable machine costs more than several smaller ones → cloud pricing pages (e.g. AWS EC2 on-demand pricing for the largest vs smaller instances)]

How does a shard know which rows it owns?
Hash the key: shard = hash(user_id) % 4. Spreads evenly, no hot shard. But adding a fifth shard remaps almost every key, which is why real systems use consistent hashing instead of plain modulo.
Range the key: shard 1 holds A–F, shard 2 G–M. Range queries stay on one shard. But sign up a celebrity whose name starts with S and that shard melts.
Directory: a lookup table says where each key lives. Total control, and one more thing that can be down.
Takeaway: the rule that maps a key to a shard decides what is easy and what melts.

[FACT_CHECK: Real systems use consistent hashing instead of plain modulo → docs of sharded systems (e.g. Cassandra/DynamoDB use consistent hashing; others like Redis Cluster or Vitess use fixed slots or ranges)]

What does sharding cost you?
→ Cross-shard joins stop being free, and often stop being possible
→ Transactions across two shards need two-phase commit, or a redesign
→ Every query now needs the shard key, or it fans out to all shards
→ Rebalancing is a migration, under load, with no downtime allowed
Takeaway: sharding is the change you cannot easily undo.

Comparison: replication vs sharding
Replication: full copies of all data. Scales reads.
Sharding: each server holds only part of the data. Scales writes.

The honest rule
Shard last. Index properly, cache what repeats, add read replicas, archive cold rows, buy a bigger machine — in that order. Sharding is the change you cannot easily undo, so it should be the one you make when the others have run out.

Keep in mind before you copy or split a database
→ Send a user's reads to the primary right after they write.
→ Pick a shard key that every hot query already filters on.
→ Use consistent hashing or fixed slots, not plain modulo.
→ Plan rebalancing before the first shard fills, not after.

Takeaway
Replication copies the data and scales reads, always a little behind.
Sharding splits the data and scales writes, at a cost you keep forever. Shard last.

What made you shard, and what did you wish you had done first?

Next: message queues and pub/sub: why not every task should happen inside the request.

#SystemDesign #Databases #Sharding #PostgreSQL #Scalability
