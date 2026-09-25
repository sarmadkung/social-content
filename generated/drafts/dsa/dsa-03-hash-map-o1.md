SERIES:    DSA SERIES #03
TITLE:     Why a Hash Map Lookup Is O(1) — and When It Isn't
PILLAR:    DSA & Problem Solving — for students and juniors who use Map daily but never looked inside
HEADLINE:  Hash the key, jump to the bucket
LAYOUT:    FLOW
---
Last post, a hash map turned Two Sum from O(n²) into O(n).

But why is a lookup O(1) at all? And when does it stop being O(1)?

What is it?
A hash map keeps key-value pairs in an array of slots called buckets. A hash function turns a key into a number. That number tells you which bucket to open.
Think of a coat check. You get ticket 42. Later, nobody searches every hook. They walk straight to hook 42.

Why do we need it?
Without hashing, finding a key means checking items one by one. That is O(n): the work grows with n, the number of items. With hashing, you compute the bucket and jump.

Key properties
→ Get, set, delete: O(1) on average.
→ Worst case: O(n), when many keys land in one bucket.
→ Two keys in one bucket is a collision. Collisions are normal, not bugs.
→ Load factor = items ÷ buckets. When it gets too high, the table grows and moves every key. That one step is O(n), but spread over all inserts it is O(1) each ("amortised").

Where is it used?
• JavaScript Map and Set, Python dict, Java HashMap
• Hash indexes in databases
• In-memory caches and key-value stores
• Symbol tables inside compilers

When to use it / when not to
Use it: you need "have I seen this?" or "what belongs to this key?" fast.
Not: you need sorted order or ranges, like "all users aged 20 to 30".

Example / Steps (looking up "cat")
1. hash("cat") gives a big number.
2. That number % bucket count picks a bucket, say bucket 3.
3. Check the few keys inside bucket 3.
4. Found it? Return the value.

Step 3 is the catch. A bad hash sends every key to bucket 3. Now step 3 checks all n keys. That is the O(n) worst case.

The senior detail: attackers can send keys that all collide and slow a server down. This is called hash flooding. So many runtimes use a random seed in their hash function. Java 8+ also turns a crowded bucket into a tree, so that bucket costs O(log n) instead of O(n).

Takeaway: O(1) is an average, not a promise. It holds because a good hash spreads keys evenly.

Next: Big-O in plain English — what it measures, and what it ignores.

#DataStructures #Algorithms #HashMap #CodingInterviews #SoftwareEngineering
