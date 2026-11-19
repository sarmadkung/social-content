TITLE: The hidden O(n²) in building strings in a loop
COVER: cover.png
---

This loop looks O(n):

```js
let out = "";
for (const c of chars) out += c;
```

In JavaScript, Java, Python and C#, a string can't be changed after it is made. Every "change" builds a new string and copies the old characters into it.

- **The cost hides inside one `+`.** Copy 1 character, then 2, then 3, up to n: about n²/2 copies. At n = 1,000 that's about 500,000, so small tests pass. At n = 100,000 it's about 5 billion.
- **The fix: build in parts, join once.** Push pieces into an array and call `parts.join("")` at the end. Each character is copied once: O(n). Java and C# use `StringBuilder`; Python uses `"".join(parts)`.
- **Know what strings cost.** Reading `s[i]` is O(1). Any change (`+`, `slice`, `replace`, `toUpperCase`) builds a new string: O(k) for k characters. Comparing two strings is O(k), not O(1).
- **Not every `+` is a problem.** Three or four fixed pieces like `` `${a}-${b}` `` are clear and cheap. The trap is the loop.

Some runtimes optimise `+=` in some cases. Don't count on it: strings are read-only, so build in parts and join once.
