SERIES:    SYSTEM ARCHITECTURE #09
TITLE:     Database Replication and Read Replicas
PILLAR:    System Design & Architecture — for mid-levels preparing for interviews, seniors for the lag trade-off
LEVEL:     INTERMEDIATE
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  One database writes. Many databases read.
LAYOUT:    FLOW
STATUS:    draft
---
Your app servers scale out easily. Your single database does not. It becomes the bottleneck.

What is it?
Replication means keeping copies of the same database on more than one server. The copies are called replicas.

In the common setup, one primary database takes all writes. It sends every change to read replicas, which serve read queries.

Think of a teacher writing on the main board. Students copy it into their notebooks. Everyone can read a notebook, but only the teacher writes on the board.

Why do we need it?
Most apps read far more than they write. Think of a feed: many views, few posts. Replicas spread those reads. They also give you a standby copy if the primary fails.

Key properties
→ Writes go to the primary only
→ Reads can go to any replica
→ Replication lag: replicas can be a little behind the primary
→ Asynchronous replication is faster but can lose recent writes on failure. Synchronous is safer but slows every write
→ Failover: promoting a replica to primary when the primary dies

Where is it used?
PostgreSQL streaming replication, MySQL replication, Amazon RDS and Aurora read replicas, MongoDB replica sets.

When to use it / when not to
Use it: read-heavy apps, or when you need a hot standby.
Not enough: when writes are the bottleneck. Replicas copy every write, so they do not reduce write load.

Example: the lag trap
1. A user updates their profile name. The write goes to the primary.
2. The page reloads and reads from a replica.
3. The replica has not caught up yet.
4. The user sees their old name and thinks the save failed.
Fix: read-your-writes. Send a user's reads to the primary for a short time after they write.

Comparison
Replication: full copies of all data. Scales reads.
Sharding: each server holds only part of the data. Scales writes.

[PERSONAL: one line on a replication-lag bug or failover you handled]

Takeaway: Replicas scale reads, not writes, and they are always a little behind.

Next: your database is at 90% CPU. What do you try first?

#SystemDesign #Databases #PostgreSQL #SoftwareArchitecture #Scalability
