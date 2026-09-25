SERIES:    DSA SERIES #08
TITLE:     Every DSA Problem Has a Pattern — How to Spot It
PILLAR:    DSA & Problem Solving — for students and juniors who solve many problems but freeze on new ones
HEADLINE:  Read the problem for clues, not code
LAYOUT:    GRID
---
Solving 500 problems does not help if every new one feels new.
There are only about 15 core patterns. Most interview problems are one of them wearing a new costume.

What is a pattern?
A pattern is a reusable way of solving a whole family of problems. Two Sum, "pair with target sum" and "3Sum" look different, but they are the same idea.
Think of a mechanic. They do not memorise every car. They hear a noise, and it points to a part.

Why do we need it?
Memorised answers break when the problem changes one word. A pattern still works, because you know why it works. Most of the work is picking the right one.

How to spot it: read for clue words
→ "sorted" + "pair" → Two Pointers
→ "subarray" / "substring", "longest", "at most K" → Sliding Window
→ "sum of range", asked many times → Prefix Sum
→ "seen before?", "count", "find the partner" → Hash Map / Set
→ "sorted" or "smallest x that works" → Binary Search
→ "top K", "K-th largest" → Heap
→ "all combinations / subsets" → Backtracking
→ "number of ways", "min cost", choices that repeat → Dynamic Programming

Steps before you write any code
1. Underline the clue words: sorted, contiguous, k, all, minimum.
2. Check the limits. n up to 10⁵ means you need about O(n log n) or better.
3. Say the brute force out loud, then ask what work it repeats.
4. Match that repeated work to a pattern from the list above.

Where is it used?
• Coding interviews: the interviewer is checking step 4
• Real code: a "find duplicates" task in a log pipeline is a hash set
• Reviews: spotting an O(n²) loop that a pattern would make O(n)

When to use it / when not to
Use it: before coding any new problem.
Not: to force a pattern that does not fit. If no clue matches, the brute force is your starting point.

Takeaway: do not ask "have I seen this problem?" Ask "what is this problem asking me to repeat?"

From now on, every pattern post in this series includes a "Spot it when…" list.

Next: Two Pointers — solving pair problems in O(n) with O(1) extra space.

#Algorithms #DataStructures #ProblemSolving #CodingInterviews #PatternRecognition
