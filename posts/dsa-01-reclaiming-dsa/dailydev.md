TITLE: Why DSA still matters when AI writes the code
COVER: cover.png
---
AI is great at writing code, and it keeps getting better. DSA still matters.

DSA was never really about writing code. It's about problem solving: understanding what a problem really asks, recognising its pattern, and knowing more than one way to solve it.

**Why it still matters**

- **Patterns.** After enough sliding-window problems, you stop seeing "a new problem" and see a pattern you know: "a window that grows and shrinks". Most problems are a few patterns in disguise.
- **One problem, many ways.** Two Sum: check every pair O(n²), sort + two pointers O(n log n), or one pass with a hash map O(n). Each has a different trade-off.
- **Understanding existing systems.** An LRU cache is a hash map plus a linked list. A database index is a B-tree. Job schedulers often use a heap.
- **Building better systems.** Spot the problem, match a pattern, choose the trade-off.
- **A sharp mind, and interviews.** Many companies still run DSA rounds.
- **AI is built on it.** RAG lookups search a graph (HNSW). Training walks the computation graph backwards (backprop). PyTorch's in-place ops like `x.relu_()` save GPU memory.

**Keep in mind: how to learn DSA without wasting time**

- **Learn the pattern, not the answer.** Memorised solutions fail on the next problem; a pattern carries over.
- **Depth beats count.** 150 problems understood, then revisited, beat 500 skimmed.
- **Use AI as a tutor, not an answer key.** Try first, ask for a hint, then compare.
- **Explain it to lock it in.** Write a short "why this works" note.
- **Small and steady.** 30–45 minutes a day beats a weekend marathon.
- **Measure before optimising.** Big-O ignores constants; for small inputs the simple version is often fine.
- **Use built-ins at work.** Learn how a heap works, then use your language's heap.
- **Balance it.** DSA isn't the whole job: add system design, debugging and reading code.

I'm writing this up one pattern at a time. Next: Big-O in plain English.
