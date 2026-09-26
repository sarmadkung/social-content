SERIES:    DSA SERIES #07
TITLE:     Hash Set vs Hash Map: Which One and Why
PILLAR:    DSA & Problem Solving — for students and juniors choosing between Set and Map
LEVEL:     BEGINNER
MODE:      COMPARE
FORMAT:    VISUAL
HEADLINE:  Set asks if. Map asks what.
LAYOUT:    COMPARE
STATUS:    draft
---
Set and Map use the same engine inside.
They answer different questions. Pick by the question.

What is it?
A hash set stores unique keys only. A hash map stores keys, each with a value attached. Both use the hashing from post #06.
Think of a party. The guest list at the door is a set: "are you on it?" Your phone contacts are a map: name → number.

Why do we need both?
A set says "I only care if it exists." A map says "I need data about it." Choosing the right one makes your code say what it means. A set also skips storing values you never read.

Key properties
→ Both: add, lookup, delete in O(1) on average, O(n) worst case
→ Set: no duplicates. Adding the same key twice does nothing.
→ Map: one value per key. Setting a key again replaces the value.
→ In JS, both keep insertion order and have .size
→ Object keys match by reference. Two separate {id: 1} objects are two different keys.

Where is it used?
Set:
• Remove duplicates from a list
• Track "visited" nodes in graph search
• Contains Duplicate
Map:
• Two Sum: value → index
• Count how often each item appears
• Caches: request → response

When to use it / when not to
Use a set: the only question is "have I seen this?"
Use a map: you need how many, where, or what.

Example
const hasDup = a => new Set(a).size !== a.length;

const count = new Map();
for (const c of "banana") count.set(c, (count.get(c) ?? 0) + 1);
// Map { b → 1, a → 3, n → 2 }

Comparison: Map vs a plain object
A plain object turns keys into strings. obj[1] and obj["1"] are the same key. A Map keeps 1 and "1" apart. It also accepts objects as keys. For lookup tables that change often, use Map.

The senior detail: a set is a map that ignores the value. Java's HashSet is literally built on a HashMap inside.

Takeaway: need "if"? Use a set. Need "what"? Use a map.

Next: hash maps — the pattern behind Two Sum.

#DataStructures #Algorithms #JavaScript #CodingInterviews #ProblemSolving
