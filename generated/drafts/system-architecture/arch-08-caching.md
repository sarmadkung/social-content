SERIES:    SYSTEM ARCHITECTURE #08
TITLE:     Caching: Where to Cache, and When to Forget
PILLAR:    System Design & Architecture — for juniors learning the basics, seniors who care about invalidation
LEVEL:     INTERMEDIATE
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  The fastest request is one you skip
LAYOUT:    ANATOMY
STATUS:    draft
---
Your database answers the same question 1,000 times a minute. The answer changes once a day.

What is it?
A cache is a small, fast store that keeps copies of data you read often, so you do not fetch it from the slow source every time.

Think of keeping a water bottle on your desk. You do not walk to the kitchen for every sip. But sometimes you need to refill it.

Why do we need it?
Databases and remote APIs are slow compared to memory. Reading from memory takes well under a millisecond. A database query over the network often takes several milliseconds or more. Caching cuts load and speeds up responses.

Key properties
→ Hit: the data was in the cache. Miss: it was not, so go to the source
→ TTL (time to live): how long an entry stays before it expires
→ Eviction: what gets removed when the cache is full. LRU (least recently used) is common
→ Staleness: a cache can serve old data. This is the real cost

Where to cache
• Browser: images, CSS, scripts
• CDN: static files near users
• App server: in-memory, per server
• Shared cache: Redis or Memcached, used by all servers
• Database: its own internal buffer cache

When to use it / when not to
Use it: data read far more often than it changes.
Avoid it: data that must always be exact, like a bank balance at payment time.

Steps: cache-aside (the most common pattern)
1. App checks Redis for "user:42".
2. Hit? Return it.
3. Miss? Read from the database.
4. Save it in Redis with a TTL.
5. On update, write the database, then delete the cache key.

Cache invalidation
Invalidation means removing or updating cached data when the source changes. It is hard because two copies now exist, and they can disagree.
Common options: short TTLs, delete-on-write, or versioned keys like "user:42:v7".

[PERSONAL: one line on a stale-cache bug you have seen in production]

Takeaway: Caching is easy. Knowing when cached data is wrong is the actual job.

Next: CDNs, caching moved close to your users.

#SystemDesign #Caching #Redis #SoftwareArchitecture #Performance
