> ⚠ NOT READY — resolve these, then delete this block:
> - [FACT_CHECK: Java += on a String in a loop copies the whole string every iteration (javac/JIT does not turn it into one StringBuilder) → JEP 280 and Java String/StringBuilder docs]
> - [FACT_CHECK: "😀".length is 2, split("") cuts it in half, [...s] splits by code point → MDN String.length and String iterator]
> - [FACT_CHECK: V8 builds += strings as ropes (ConsString) and flattens later → V8 source / v8.dev blog on string representation]

---

This loop looks O(n):

let out = "";
for (const c of chars) out += c;

But strings can't be changed after they are made. So each += can build a new string and copy everything in out so far.

Copy 1 character, then 2, then 3, up to n. That's about n²/2 copies. At 1,000 characters it passes every test. At 100,000 it's about 5 billion copies.

The 3 images show:
1. Why every += copies the whole string
2. The fix: build in parts, join once
3. What string operations really cost

Some runtimes optimise += in some cases. You can't count on it, so build in parts and join once: each character is copied once, O(n).

Next: why a hash map lookup is O(1), and when it isn't.

#DataStructures #Algorithms #JavaScript #Performance #ProblemSolving
