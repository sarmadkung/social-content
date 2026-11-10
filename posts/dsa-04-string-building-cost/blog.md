---
title: "The hidden O(n²) in building strings in a loop"
description: "Why out += c in a loop can copy billions of characters, how to fix it with parts and join, and what string operations really cost."
date: 2026-11-13
series: "DSA Series"
seriesNumber: 4
slug: dsa-04-string-building-cost
tags: [strings, big-o, algorithms, performance, data-structures]
cover: cover.png
---

This loop looks O(n):

```js
let out = "";
for (const c of chars) out += c;
```

One pass over the characters, one `+=` each. But the real cost can be O(n²), and every small test passes. This article explains why, and the simple fix.

## What we'll cover

![In this post: why every += copies it all, the fix, and what strings really cost](0.png)

1. **Every += copies it all:** why one loop becomes O(n²).
2. **Build in parts, join once:** the O(n) fix, in any language.
3. **What strings really cost:** read, change, compare, join.

## Every += copies the whole string

![Building HELLO with += copies 1+2+3+4+5 = 15 characters; parts and join copies 5](1.png)

In JavaScript, Java, Python and C#, you cannot change a string after it is made. Every "change" builds a new string and copies the old characters into it. This is called **immutability**. Think of a printed page: to fix one letter, you print the whole page again.

So `out += c` copies everything in `out` so far, then adds one character. Building "HELLO" this way copies 1, then 2, then 3, then 4, then 5 characters: 15 copies for a 5-letter string.

In general that is 1 + 2 + ... + n, about n²/2 copies. O(n²), hidden inside one `+`.

- For n = 1,000 it is about 500,000 copies. Fast enough, which is why it passes every small test.
- For n = 100,000 it is about 5,000,000,000 copies.

## Build in parts, join once

![The fix as a diff: replace out += c with parts.push(c) and one parts.join at the end](2.png)

Collect the pieces in an array, then join them once at the end:

```js
const parts = [];
for (const c of chars) parts.push(c);
const out = parts.join(""); // each character copied once: O(n)
```

Need many edits to one string? Turn it into an array, edit the array, and join it back: `const chars = [...s];`.

The same idea exists in every mainstream language: `StringBuilder` in Java and C#, `"".join(parts)` in Python. Some runtimes optimise `+=` in some cases, but you can't count on it. Parts and join is the habit that works everywhere.

## What strings really cost

![A table of string costs: read is O(1), any change and compare are O(k), parts and join is O(n) total](3.png)

- **Read `s[i]`: O(1).** A string is laid out like an array, so the computer jumps straight to slot i.
- **Any change (`+`, `slice`, `replace`, `toUpperCase`): O(k)** for k characters, because it builds a new string.
- **Compare two strings: O(k), not O(1).** The check goes character by character.
- **Join or StringBuilder: O(n) total.** Each character is copied once.

## Where you will meet it

- Log lines, HTML templates, CSV and JSON output.
- Parsers that read text one character at a time.

## When to use it, and when not to

Use parts and join whenever you build a string inside a loop. You don't need it for 3 or 4 fixed pieces: `` `${a}-${b}` `` is clear and cheap.

## Keep in mind when you build strings

- In code review, flag `+=` on a string inside a loop.
- `s = s.slice(1)` in a loop can copy too: O(n²) again.
- Big CSV or log export? Stream the rows out; don't build one huge string.

**In one line:** strings are read-only. Build in parts, join once.

## Next in the series

Why a hash map lookup is O(1), and when it isn't.
