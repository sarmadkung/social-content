SERIES:    SYSTEM ARCHITECTURE #05
TITLE:     Caching and CDNs: Where to Cache, and When to Forget
PILLAR:    System Design & Architecture — for juniors learning the basics, mid-levels for interviews, seniors who care about invalidation
LEVEL:     INTERMEDIATE
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  The fastest request is one you skip
LAYOUT:    ANATOMY
VISUALS:   1 = Where can you cache data? · 2 = How does cache-aside read and update data? · 3 = How do you stop a cache serving wrong data? · 4 = How does a CDN serve a file from nearby? · 5 = Takeaway · rest = text
STATUS:    draft
---
Your database answers the same question 1,000 times a minute. The answer changes once a day.
Your server is in Virginia. A user in Karachi loads your site. Every image crosses the planet, and they wait.

Two problems, one idea: keep a copy closer to where it is needed.

What is a cache?
A cache is a small, fast store that keeps copies of data you read often, so you do not fetch it from the slow source every time.
Think of keeping a water bottle on your desk. You do not walk to the kitchen for every sip. But sometimes you need to refill it.

Why do we need it?
Databases and remote APIs are slow compared to memory. Reading from memory takes well under a millisecond. A database query over the network often takes several milliseconds or more. Caching cuts load and speeds up responses.

[FACT_CHECK: Reading from memory takes well under a millisecond; a database query over the network often takes several ms or more → published latency numbers (e.g. 'Latency Numbers Every Programmer Should Know') and database benchmarks]

Key properties
→ Hit: the data was in the cache. Miss: it was not, so go to the source
→ TTL (time to live): how long an entry stays before it expires
→ Eviction: what gets removed when the cache is full. LRU (least recently used) is common
→ Staleness: a cache can serve old data. This is the real cost

Where can you cache data?
• Browser: images, CSS, scripts
• CDN: static files near users
• App server: in-memory, per server
• Shared cache: Redis or Memcached, used by all servers
• Database: its own internal buffer cache
Takeaway: every layer between the user and the data can keep a copy.

How does cache-aside read and update data?
Cache-aside is the most common pattern:
1. App checks Redis for "user:42".
2. Hit? Return it.
3. Miss? Read from the database.
4. Save it in Redis with a TTL.
5. On update, write the database, then delete the cache key.
Takeaway: read through the cache, write to the database, then drop the stale copy.

[FACT_CHECK: Cache-aside is the most common caching pattern → Redis docs / AWS caching best-practices whitepaper]

How do you stop a cache serving wrong data?
Invalidation means removing or updating cached data when the source changes. It is hard because two copies now exist, and they can disagree.
Common options: short TTLs, delete-on-write, or versioned keys like "user:42:v7".
Takeaway: caching is easy; knowing when cached data is wrong is the actual job.

[PERSONAL: one line on a stale-cache bug you have seen in production]

When to cache / when not to
Use it: data read far more often than it changes.
Avoid it: data that must always be exact, like a bank balance at payment time.

The CDN: a cache near your users
A CDN (Content Delivery Network) is a group of servers spread around the world. Each one keeps copies of your files, and each user is served from the nearest one.
Think of a store chain. You do not ship every order from one central warehouse. You stock local branches, so customers buy nearby.

Why do we need it?
Data cannot travel faster than light, and real networks are slower. Far users see higher latency (the delay before a response). One origin server (your main server) also gets overloaded by every download.

How does a CDN serve a file from nearby?
1. User requests logo.png.
2. DNS sends them to the nearest edge server.
3. Edge has it (cache hit)? Return it right away.
4. No (cache miss)? Fetch it from the origin once.
5. Store it at the edge. The next nearby user gets it fast.
→ Edge servers: CDN servers placed close to users, in many cities
→ Caches static files: images, video, CSS, JavaScript
→ Offloads your origin: most requests never reach your server
→ Uses TTLs and cache headers to decide how long files stay
Takeaway: a CDN is a cache that lives near your users, not near your servers.

[FACT_CHECK: DNS sends users to the nearest edge server → CDN routing docs (some CDNs, e.g. Cloudflare, route by anycast rather than DNS)]

It also absorbs traffic spikes, and many CDNs also help block DDoS attacks (floods of fake traffic).

[FACT_CHECK: Many CDNs also help block DDoS attacks → Cloudflare / Akamai / CloudFront DDoS protection docs]

Where is it used?
Cloudflare, Akamai, Amazon CloudFront, Fastly. Netflix runs its own CDN, Open Connect, to deliver video.

[FACT_CHECK: Netflix runs its own CDN, Open Connect, to deliver video → Netflix Open Connect site (openconnect.netflix.com)]

When to use a CDN / when not to
Use it: public files that many users download, or users spread across countries.
Less useful: private, per-user data that changes on every request.

Comparison: CDN vs an app cache like Redis
A CDN caches whole files near users.
Redis caches data near your servers.
They solve different distances.

Watch out: what caching breaks
→ Stale data → a user sees an old profile after saving → delete the key on write, keep TTLs short.
→ Old files at the edge → you deploy a new app.js, but users still get the old one → put a version or hash in the file name, like app.3f9a.js.

[PERSONAL: one line on a CDN caching issue or win from a real project]

Keep in mind before you add a cache
→ Decide how stale each piece of data may be before you cache it.
→ Give every entry a TTL, even when you also delete on write.
→ Never cache per-user private data at a shared CDN edge.

Takeaway
The fastest request is one you skip: a cache near your servers, a CDN near your users.
The real job is knowing when the copy is wrong.

Next: your database is at 90% CPU. What do you try first?

#SystemDesign #Caching #CDN #Redis #Performance
