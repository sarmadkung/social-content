SERIES:    DSA SERIES #01
TITLE:     Reclaiming DSA: Two Weeks, 23 Algorithms, One Repo
PILLAR:    DSA & Problem Solving — for developers rebuilding their fundamentals
LEVEL:     BEGINNER
MODE:      PERSONAL
FORMAT:    VISUAL
HEADLINE:  Two weeks, 23 algorithms
LAYOUT:    STAT
STATUS:    draft
---
This month I spent two weeks rebuilding my algorithm fundamentals in public. Here's the honest state of it.

23 technique explainers written — Boyer-Moore voting, Kadane's, two pointers, monotonic stack, union-find, Dijkstra, backtracking, and the rest.
179 problem files across 23 categories.
41 commits, mostly at night.

What I didn't expect was which part took longest.

Not the solutions. Writing code that passes is the easy half. The slow part was answering "why does this work?" in a way that survives being read six months later — the invariant, the proof sketch, the reason the loop terminates.

I also added a section to every explainer I hadn't planned on: where the technique shows up in real systems. Cyclic sort is the same trick a receiver can use to spot missing packet numbers. Monotonic stacks are how you compute a stock's next-higher price in one pass. Union-find answers "are these two machines in the same partition?" almost instantly.

[FACT_CHECK: cyclic sort is a trick receivers can use to spot missing packet numbers (real stacks use sequence numbers, SACK or bitmaps) → RFC 9293 (TCP), RFC 2018 (SACK)]

That section changed how I write the rest. An algorithm you can place in a real system is one you actually remember.

[PERSONAL: confirm the 3,417 figure from your fuzz run, or drop the number]
One bug worth admitting: my Boyer-Moore n/3 implementation passed every test I wrote, then failed 3,417 cases under a fuzz test. The check ordering was wrong in a way no hand-written test was ever going to catch.

Write the fuzz test. Your tests agree with your assumptions.

This series is where I'll share it, one pattern at a time.

Next: Big-O in plain English — what it measures, and what it ignores.

#DataStructures #Algorithms #BuildInPublic #LearningInPublic #SoftwareEngineering
