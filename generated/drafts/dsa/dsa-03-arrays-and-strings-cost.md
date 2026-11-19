SERIES:    DSA SERIES #03
TITLE:     Arrays and Strings: What Each Operation Really Costs
PILLAR:    DSA & Problem Solving — for students and juniors who use arrays and strings daily, and anyone who builds text at scale
LEVEL:     BEGINNER
MODE:      WHY
FORMAT:    VISUAL
HEADLINE:  Reading is instant. Rearranging is not.
LAYOUT:    COMPARE
VISUALS:   1 = Why is reading O(1) but inserting O(n)? · 2 = What does each array operation cost? · 3 = Why can building a string in a loop become O(n²)? · 4 = How do you build a string in O(n)? · 5 = Takeaway · rest = text
STATUS:    draft
---
a[500000] is as fast as a[0].
But adding one item at the front can touch every item in the array.

And this loop looks O(n):

let out = "";
for (const c of chars) out += c;

Build a 100,000-character string this way in Java and it copies about 5 billion characters.

[FACT_CHECK: Java += on a String in a loop copies the whole string every iteration (javac/JIT does not turn it into one StringBuilder) → JEP 280 and Java String/StringBuilder docs]

Both surprises come from the same place: how the data sits in memory.

What is an array?
An array stores items side by side, in one block of memory. Each slot has a number, called its index.
Think of a row of cinema seats. Finding seat 7 is instant. But if someone must sit in seat 1, everyone moves one seat right.

Why is reading O(1) but inserting O(n)?
Reading: the computer knows where the block starts and how big each slot is. So:
address = start + index × slot size
One sum, one jump. It does not matter how long the array is.
Inserting: there are no gaps. To insert at position i, every item after i shifts one slot. At the front, that is all n items.
Takeaway: an array jumps to any slot, but it cannot make room without moving things.

What does each array operation cost?
→ Read or write by index: O(1)
→ Find a value in an unsorted array: O(n)
→ push / pop at the end: O(1) amortised
→ Insert or delete at the front or middle: O(n)
→ Items sit next to each other, so the CPU cache reads them fast

const a = [10, 20, 30, 40];
a[2];               // O(1): jump to slot 2
a.push(50);         // O(1) amortised: add at the end
a.unshift(5);       // O(n): every item shifts right
a.splice(2, 0, 15); // O(n): items after slot 2 shift

Why "amortised" for push? A JS array grows as needed. When its space is full, the engine copies it into a bigger block, about 1.5 times the size. That copy is O(n), but it happens rarely, so the average push is O(1).
Takeaway: work at the end is cheap; work at the front or middle costs O(n).

Where are arrays used?
• Every list you render in a UI
• Image pixels and file buffers (TypedArray in JS)
• The buckets inside a hash map (#04)
• Stacks, which only touch the end

When to use an array / when not to
Use it: you read by position, loop in order, or add at the end.
Not: you insert or remove at the front all the time. Use a deque or a queue instead.

The senior detail: a.shift() is O(n) too. The spec says every item moves down one slot. Some engines have tricks that make it cheap in some cases, but you can't count on them. Using an array as a queue in a big BFS loop can quietly turn O(n) into O(n²). A head index that moves forward is O(1), every time.

Why can building a string in a loop become O(n²)?
A string is laid out like an array, so reading s[i] is O(1). Changing it is another story.
In JavaScript, Java, Python and C#, you cannot change a string after it is made. Every "change" builds a new string and copies the old characters into it. So out += c copies everything in out so far, then adds one character.
This is called immutability. Think of a printed page: to fix one letter, you print the whole page again.
Copy 1 character, then 2, then 3, up to n. That is 1 + 2 + ... + n, about n²/2 copies. O(n²), hidden inside one "+".
For n = 100,000 that is about 5,000,000,000 copies. For n = 1,000 it is 500,000, which is why it passes every small test.
Takeaway: one "+" inside a loop can hide a full copy of the string.

How do you build a string in O(n)?
Build in parts, join once:
const parts = [];
for (const c of chars) parts.push(c);
const out = parts.join(""); // each character copied once: O(n)

Need many edits? Turn it into an array, edit, join back:
const chars = [...s];

What strings cost:
→ Read s[i]: O(1), like an array.
→ Any change (+, slice, replace, toUpperCase): a new string, O(k) for k characters.
→ Compare two strings: O(k), not O(1).
→ join or StringBuilder: O(n) total.
Takeaway: collect the pieces, then join once.

Where is it used?
• Java and C# StringBuilder, Python "".join(parts)
• Log lines, HTML templates, CSV and JSON output
• Parsers that read text one character at a time

When to build in parts / when not to
Use parts + join whenever you build a string inside a loop.
Not needed for 3 or 4 fixed pieces: `${a}-${b}` is clear and cheap.

Comparison: Java vs JavaScript
Java: += in a loop copies every time. Use StringBuilder.
JavaScript: V8 links pieces and copies later (a "rope"), so += is often fast. Parts + join is still the portable habit.

[FACT_CHECK: V8 builds += strings as ropes (ConsString) and flattens later → V8 source / v8.dev blog on string representation]

Common mistake
Reversing with s.split("").reverse().join(""). JS length counts UTF-16 code units, so "😀".length is 2 and split("") cuts the emoji in half. [...s] splits by code point, so 😀 stays whole.

[FACT_CHECK: "😀".length is 2, split("") cuts it in half, [...s] splits by code point → MDN String.length and String iterator]

Keep in mind when you work with arrays and strings
→ Queue in a loop? Move a head index; don't call shift().
→ In code review, flag += on a string inside a loop.
→ s = s.slice(1) in a loop can copy too: O(n²) again.
→ Big CSV or log export? Stream rows; don't build one string.

Takeaway
Arrays are fast to read and slow to rearrange.
Strings are read-only: build in parts, join once.

Next: how a hash map finds a key in about one step, and when to use a Set or a Map.

#DataStructures #Algorithms #JavaScript #Performance #ProblemSolving
