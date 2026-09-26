SERIES:    DSA SERIES #04
TITLE:     Why Building Strings in a Loop Can Quietly Become O(n²)
PILLAR:    DSA & Problem Solving — for developers who build or process text at scale
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  The hidden O(n²) in string building
LAYOUT:    COMPARE
STATUS:    draft
---
This loop looks O(n):

let out = "";
for (const c of chars) out += c;

Build a 100,000-character string this way in Java and it copies about 5 billion characters.

What is it?
You cannot change a string after it is made. Every "change" builds a new string and copies the old characters into it. So out += c copies everything in out so far, then adds one character.
This is called immutability. Think of a printed page: to fix one letter, you print the whole page again.

Why does it matter?
Copy 1 character, then 2, then 3, up to n. That is 1 + 2 + ... + n, about n²/2 copies. O(n²), hidden inside one "+".
For n = 100,000 that is about 5,000,000,000 copies. For n = 1,000 it is 500,000, which is why it passes every small test.

How do you fix it?
Build in parts, join once:
const parts = [];
for (const c of chars) parts.push(c);
const out = parts.join(""); // each character copied once: O(n)

Need many edits? Turn it into an array, edit, join back:
const chars = [...s];

Key properties
→ Read s[i]: O(1). A string is laid out like an array (#03).
→ Any change (+, slice, replace, toUpperCase): a new string, O(k) for k characters.
→ Compare two strings: O(k), not O(1).
→ join or StringBuilder: O(n) total.

Where is it used?
• Java and C# StringBuilder, Python "".join(parts)
• Log lines, HTML templates, CSV and JSON output
• Parsers that read text one character at a time

When to use it / when not to
Use parts + join whenever you build a string inside a loop.
Not needed for 3 or 4 fixed pieces: `${a}-${b}` is clear and cheap.

Common mistake
Reversing with s.split("").reverse().join(""). JS length counts UTF-16 code units, so "😀".length is 2 and split("") cuts the emoji in half. [...s] splits by character.

Comparison
Java: += in a loop copies every time. Use StringBuilder.
JavaScript: V8 links pieces and copies later (a "rope"), so += is often fast. Parts + join is still the portable habit.

Takeaway: strings are read-only. Build in parts, join once.

Next: why a hash map lookup is O(1) — and when it isn't.

#DataStructures #Algorithms #JavaScript #Performance #ProblemSolving
