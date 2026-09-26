SERIES:    DSA SERIES #05
TITLE:     Arrays: Why Index Access Is O(1) but Insert Is O(n)
PILLAR:    DSA & Problem Solving — for students and juniors who use arrays daily
LEVEL:     BEGINNER
FORMAT:    VISUAL
HEADLINE:  Reading is instant. Inserting shifts everything.
LAYOUT:    COMPARE
STATUS:    draft
---
a[500000] is as fast as a[0].
But adding one item at the front can touch every item in the array.

What is it?
An array stores items side by side, in one block of memory. Each slot has a number, called its index.
Think of a row of cinema seats. Finding seat 7 is instant. But if someone must sit in seat 1, everyone moves one seat right.

Why is reading O(1)?
The computer knows where the block starts and how big each slot is. So:
address = start + index × slot size
One sum, one jump. It does not matter how long the array is.

Why is inserting O(n)?
There are no gaps. To insert at position i, every item after i shifts one slot. At the front, that is all n items.

Key properties
→ Read or write by index: O(1)
→ Find a value in an unsorted array: O(n)
→ push / pop at the end: O(1) amortised
→ Insert or delete at the front or middle: O(n)
→ Items sit next to each other, so the CPU cache reads them fast

Why "amortised" for push? A JS array grows as needed. When its space is full, the engine copies it into a bigger block. That copy is O(n), but it happens rarely, so the average push is O(1).

Example
const a = [10, 20, 30, 40];
a[2];               // O(1): jump to slot 2
a.push(50);         // O(1) amortised: add at the end
a.unshift(5);       // O(n): every item shifts right
a.splice(2, 0, 15); // O(n): items after slot 2 shift

Where is it used?
• Every list you render in a UI
• Image pixels and file buffers (TypedArray in JS)
• The buckets inside a hash map (post #03)
• Stacks, which only touch the end

When to use it / when not to
Use it: you read by position, loop in order, or add at the end.
Not: you insert or remove at the front all the time. Use a deque or a queue instead.

The senior detail: a.shift() is O(n) too. Using an array as a queue in a big BFS loop can quietly turn O(n) into O(n²).

Takeaway: arrays are fast to read and slow to rearrange.

Next: strings are arrays too — and why building them the wrong way costs O(n²).

#DataStructures #Algorithms #JavaScript #CodingInterviews #ProblemSolving
