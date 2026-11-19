SERIES:    DSA SERIES #04
TITLE:     How Hash Maps Work: Why Lookup Is O(1), When It Isn't, and Set vs Map
PILLAR:    DSA & Problem Solving — for students and juniors who use Map and Set daily but never looked inside
LEVEL:     BEGINNER
MODE:      WHY
FORMAT:    VISUAL
HEADLINE:  Hash the key, jump to the bucket
LAYOUT:    FLOW
VISUALS:   1 = How does a hash map find a key in one step? · 2 = When does a hash map stop being O(1)? · 3 = Should you use a Set or a Map? · 4 = Why use a Map instead of a plain object? · 5 = Takeaway · rest = text
STATUS:    draft
---
Finding one key among 1 million items should take 1 million checks.
A hash map does it in about one. Why? And when does it stop being O(1)?

What is a hash map?
A hash map keeps key-value pairs in an array of slots called buckets. A hash function turns a key into a number. That number tells you which bucket to open.
Think of a coat check. You get ticket 42. Later, nobody searches every hook. They walk straight to hook 42.

Why do we need it?
Without hashing, finding a key means checking items one by one. That is O(n): the work grows with n, the number of items. With hashing, you compute the bucket and jump, the same O(1) jump an array makes by index (#03).

How does a hash map find a key in one step?
Looking up "cat":
1. hash("cat") gives a big number.
2. That number % bucket count picks a bucket, say bucket 3.
3. Check the few keys inside bucket 3.
4. Found it? Return the value.
Takeaway: the hash turns a key into an index, so lookup is one jump, not a search.

When does a hash map stop being O(1)?
Step 3 is the catch. A bad hash sends every key to bucket 3. Now step 3 checks all n keys. That is the O(n) worst case.
→ Get, set, delete: O(1) on average.
→ Worst case: O(n), when many keys land in one bucket.
→ Two keys in one bucket is a collision. Collisions are normal, not bugs.
→ Load factor = items ÷ buckets. When it gets too high, the table grows and moves every key. That one step is O(n), but spread over all inserts it is O(1) each ("amortised").
Takeaway: O(1) is an average that holds only while a good hash spreads keys evenly.

The senior detail: attackers can send keys that all collide and slow a server down. This is called hash flooding. So many runtimes use a random seed in their hash function. Java 8+ also turns a crowded bucket into a tree, so that bucket costs O(log n) instead of O(n).

[FACT_CHECK: many runtimes randomise their hash seed to stop hash flooding → 28C3 2011 hash-flooding talk (Klink & Wälde), Python PEP 456, Ruby/Perl changelogs]
[FACT_CHECK: Java 8+ HashMap turns a crowded bucket into a tree, O(log n) → JEP 180 and OpenJDK HashMap source (TREEIFY_THRESHOLD)]

Where is it used?
• JavaScript Map and Set, Python dict, Java HashMap
• Hash indexes in databases
• In-memory caches and key-value stores
• Symbol tables inside compilers

When to use it / when not to
Use it: you need "have I seen this?" or "what belongs to this key?" fast.
Not: you need sorted order or ranges, like "all users aged 20 to 30".

Should you use a Set or a Map?
Set and Map use the same engine inside. They answer different questions. Pick by the question.
A hash set stores unique keys only. A hash map stores keys, each with a value attached.
Think of a party. The guest list at the door is a set: "are you on it?" Your phone contacts are a map: name → number.
→ Both: add, lookup, delete in O(1) on average, O(n) worst case
→ Set: no duplicates. Adding the same key twice does nothing.
→ Map: one value per key. Setting a key again replaces the value.
→ In JS, both keep insertion order and have .size
→ Object keys match by reference. Two separate {id: 1} objects are two different keys.
Use a set: the only question is "have I seen this?" Use a map: you need how many, where, or what.
Takeaway: need "if"? Use a set. Need "what"? Use a map.

Why do we need both?
A set says "I only care if it exists." A map says "I need data about it." Choosing the right one makes your code say what it means. A set also skips storing values you never read.

Where each one is used
Set:
• Remove duplicates from a list
• Track "visited" nodes in graph search
• Contains Duplicate
Map:
• Two Sum: value → index
• Count how often each item appears
• Caches: request → response

Example
const hasDup = a => new Set(a).size !== a.length;

const count = new Map();
for (const c of "banana") count.set(c, (count.get(c) ?? 0) + 1);
// Map { b → 1, a → 3, n → 2 }

Why use a Map instead of a plain object?
A plain object turns keys into strings. obj[1] and obj["1"] are the same key. A Map keeps 1 and "1" apart. It also accepts objects as keys. For lookup tables that change often, use Map.
Takeaway: a plain object quietly turns every key into a string; a Map keeps keys as they are.

[FACT_CHECK: a plain JS object turns keys into strings, so obj[1] and obj["1"] are the same → MDN Property accessors / Map vs Object]

The senior detail: a set is a map that ignores the value. Java's HashSet is literally built on a HashMap inside.

[FACT_CHECK: Java's HashSet is built on a HashMap inside → OpenJDK java.util.HashSet source]

Keep in mind when you reach for a hash map
→ Need sorted order or ranges? A hash map can't give you either.
→ Two {id: 1} objects are two keys; key by the id instead.
→ Exposed to user-chosen keys? Rely on a seeded hash.
→ Only checking membership? A Set says that and stores less.

Takeaway
A hash map is fast because the hash turns a key into an index.
O(1) is an average, not a promise. Pick a Set for "if", a Map for "what".

Next: hash map patterns: find the partner (Two Sum) and group by the right key (anagrams).

#DataStructures #Algorithms #HashMap #CodingInterviews #JavaScript
