SERIES:    DSA SERIES #06
TITLE:     Strings Are Arrays Too
PILLAR:    DSA & Problem Solving — for students and juniors solving string problems
LEVEL:     BEGINNER
FORMAT:    VISUAL
HEADLINE:  Strings are read-only arrays
LAYOUT:    ANATOMY
STATUS:    draft
---
Most string problems are array problems in disguise.
With one big difference: you cannot change a string.

What is it?
A string is a sequence of characters, stored in order like an array. s[0] is the first character. s.length is the count.
It is also immutable, which means it cannot be changed after it is made.
Think of a printed page. To fix one letter, you do not edit the ink. You print a new page.

Why does this matter?
Every "change" makes a new string. s.toUpperCase(), s + "!", s.slice(1): each one creates a copy. Copying k characters costs O(k).
So a loop that copies a growing string n times does 1 + 2 + ... + n work. That is O(n²).

Key properties
→ Read s[i]: O(1)
→ s.length: O(1)
→ Compare two strings: O(k), k = the shorter length
→ Copy, slice or join: O(k) for k characters
→ s[0] = "x" does nothing. Strings are read-only.

Example: build in parts, join once
const parts = [];
for (const w of words) parts.push(w.toUpperCase());
const out = parts.join(" "); // one final copy: O(n) total

Need many edits? Turn it into an array, edit, join back:
const chars = [...s]; // now you can swap and change freely

Where is it used?
• Java StringBuilder and C# StringBuilder
• Python "".join(parts)
• Log lines, HTML templates, JSON output
• Parsers that read text one character at a time

When to use it / when not to
Use array patterns on strings: index access, two pointers, counting.
Do not rebuild a big string inside a loop in a language that copies it every time.

Comparison
In Java, s += x in a loop copies every time. Use StringBuilder.
In JavaScript, engines like V8 use a trick called ropes, so += is often fast. Parts and join is still the clear, portable habit.

The senior detail: in JS, length counts UTF-16 code units, not visible characters. "😀".length is 2. [..."😀"].length is 1. This breaks "reverse a string" answers that use split("").

Takeaway: strings are read-only arrays. Build in parts, join once.

Next: Hash Set vs Hash Map — which one to reach for, and why.

#DataStructures #Algorithms #JavaScript #CodingInterviews #ProblemSolving
