This loop looks O(n):

let out = "";
for (const c of chars) out += c;

It can be O(n²), and every small test passes. Here's why 🧵
[images: 0, 1]
---
Strings can't be changed after they're made. Each += can build a new string and copy everything so far.

Copy 1, then 2, then 3, up to n: about n²/2 copies.

n = 1,000: ~500,000 copies
n = 100,000: ~5 billion
---
The fix: build in parts, join once.

const parts = [];
for (const c of chars) parts.push(c);
const out = parts.join("");

Each character is copied once: O(n). Java and C#: StringBuilder. Python: "".join(parts).
[images: 2]
---
What strings cost:
read s[i]: O(1)
any change (+, slice, replace): O(k), a new string
compare a === b: O(k), not O(1)
parts + join: O(n) total
[images: 3]
---
Some runtimes optimise += in some cases. Don't count on it.

Strings are read-only. Build in parts, join once.

Next: why a hash map lookup is O(1), and when it isn't.

#DataStructures #Algorithms
