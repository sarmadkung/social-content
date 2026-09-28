SERIES:    DSA SERIES #01
TITLE:     Why I'm Relearning DSA in the Age of AI
PILLAR:    DSA & Problem Solving — for developers rebuilding their fundamentals
LEVEL:     BEGINNER
MODE:      PERSONAL
FORMAT:    VISUAL
HEADLINE:  Why DSA still matters with AI
LAYOUT:    GRID
STATUS:    draft
---
This month I spent two weeks relearning data structures and algorithms. In 2026. When AI agents write most of the code.

AI writes the code. You still solve the problem.
DSA was never really about writing code. It is about problem solving: seeing what a problem really is, and knowing which way to solve it. AI can type the solution. It can't tell whether it solved the right problem.
I noticed I was accepting answers I could not fully check. That is the gap I wanted to close.

What I did
→ 179 problems solved, across 23 categories
→ 23 technique write-ups: two pointers, sliding window, prefix sum, Kadane's, binary search, monotonic stack, union-find, Dijkstra, backtracking and more
→ 41 commits, mostly at night

[PERSONAL: confirm 179 problems / 23 categories / 41 commits are still your current numbers]

Why it still matters
→ It trains your eye for patterns. After enough sliding-window problems, you stop seeing "a new problem". You see "a window that grows and shrinks".
→ You can check AI's work. Is this loop O(n²) on a list that keeps growing? Is there a simpler way?
→ It is how architects think. Designing a full system means spotting the problem, matching it to a pattern you know, and choosing a solution and its trade-offs. The same skill, at a bigger size.
→ AI itself is built on it. Three examples:

Search: when a chatbot looks up your own documents (RAG), a vector database finds the closest matches. Many use HNSW, a layered graph searched greedily from the top layer down instead of scanning millions of vectors.

Traversal: when a model trains, backpropagation walks its computation graph backwards in reverse topological order to get each weight's gradient. PyTorch does it every training step.

In-place: PyTorch ops like x.relu_() change a tensor where it sits instead of making a copy. On a tight GPU, that can decide whether a model fits. Same idea as reversing an array in place with two pointers.

Who it helps
• Students and juniors: many companies still run DSA rounds in their interviews. It is still one of the doors to your first job.
• Mid-level developers: the step from "it works" to "it scales".
• Seniors and architects: better decisions about storage, caching, queues and scale.

What surprised me
Writing code that passes was the easy half. The slow part was answering "why does this work?" in a way I would still understand six months later.

This series is where I'll share it, one pattern at a time.

Next: Big-O in plain English — what it measures, and what it ignores.

#DataStructures #Algorithms #AI #LearningInPublic #SoftwareEngineering
