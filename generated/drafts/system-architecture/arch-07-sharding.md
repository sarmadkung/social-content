SERIES:    SYSTEM ARCHITECTURE #07
TITLE:     Sharding: when one database stops being enough
PILLAR:    System Design & Architecture — for mid-levels in design interviews and juniors who have only ever used one database
HEADLINE:  Replication copies the data. Sharding splits it.
LAYOUT:    FLOW
VARIANT:   A (shapes)
---
Read replicas fix read load. They do not fix a table too big for one machine, and they do nothing for write load — every replica still writes every row.

What is it?
Sharding splits one logical table across several machines. Each shard holds a different slice of the rows, and something up front decides which shard owns a given row.

That decision is the whole design.

Hash the key — shard = hash(user_id) % 4. Spreads evenly, no hot shard. But adding a fifth shard remaps almost every key, which is why real systems use consistent hashing instead of plain modulo.

Range the key — shard 1 holds A–F, shard 2 G–M. Range queries stay on one shard. But sign up a celebrity whose name starts with S and that shard melts.

Directory — a lookup table says where each key lives. Total control, and one more thing that can be down.

Why do we need it?
Because vertical scaling ends. There is a biggest machine you can rent, and it costs more than several smaller ones.

What it costs you
→ Cross-shard joins stop being free, and often stop being possible
→ Transactions across two shards need two-phase commit, or a redesign
→ Every query now needs the shard key, or it fans out to all shards
→ Rebalancing is a migration, under load, with no downtime allowed

The honest rule
Shard last. Index properly, cache what repeats, add read replicas, archive cold rows, buy a bigger machine — in that order. Sharding is the change you cannot easily undo, so it should be the one you make when the others have run out.

What made you shard, and what did you wish you had done first?
