# Pillar 1 — DSA & Problem Solving

Series label: `DSA SERIES #NN` · Visual accent: amber `#FFB86B` · Tag: `DSA`

## Purpose
Teach data structures, algorithms and problem-solving patterns so a reader can
recognise the pattern in a new problem, not memorise answers.

## Audience
Students, juniors preparing for interviews, mid-level devs rebuilding
fundamentals, seniors who like a clean explanation.

## Teaching format
Problem → Intuition → Pattern → Example → Solution → Complexity → Interview takeaway
(wrapped in the What / Why / Where / Properties structure from the master prompt)

## Pattern recognition (required on every pattern post)
Every post that teaches a pattern has a "Spot it when the problem says…" block,
placed just before "When to use it / when not to":

    Spot it when the problem says…
    → "<clue words from the problem statement>"
    → "<another clue>"
    → <a structural clue, e.g. a yes/no test that flips once>

2–3 lines. Clues are words or constraints a reader can find in a problem
statement, not a restated definition. Where two patterns are easy to confuse
(prefix sum vs sliding window vs Kadane), one clue says which to pick.

## Pattern quiz (bonus posts)
Every 3–4 pattern posts, an optional "DSA QUIZ #NN" post: one problem
statement, "Which pattern is this?", answer and reasoning in the first comment.
Only use patterns already taught. Not part of the Monday queue — post as an
extra (e.g. Saturday) when there is time. Drafts go in generated/quiz/dsa/.

## Roadmap (post in this order)
Published: #01 Reclaiming DSA · #02 Hash Maps: The Pattern Behind Two Sum

### Foundations
- #03 Why a hash map lookup is O(1) — and when it isn't (hashing, collisions)
- #04 Big-O in plain English (what it measures, what it ignores)
- #05 Arrays: why index access is O(1) but insert is O(n)
- #06 Strings are arrays too (immutability, building strings efficiently)
- #07 Hash Set vs Hash Map: which one and why

### Patterns on arrays and strings
- #08 Every DSA problem has a pattern — how to spot it (clue words → pattern)
- #09 Two Pointers
- #10 Sliding Window (fixed and variable size)
- #11 Prefix Sum
- #12 Kadane's Algorithm (max subarray)
- #13 Boyer–Moore Voting (majority element)
- #14 Anagrams and Group Anagrams (frequency counting)
- #15 Binary Search (and "binary search on the answer")
- #16 Sorting: what every developer should know (stable, in-place, O(n log n))

### Linear structures
- #17 Linked Lists (and when you would actually use one)
- #18 Fast and Slow Pointers (cycle detection)
- #19 Stacks (valid parentheses, undo)
- #20 Monotonic Stack (next greater element)
- #21 Queues and Deques (BFS, sliding window max)

### Trees and graphs
- #22 Trees and Binary Trees
- #23 Tree traversals: DFS vs BFS
- #24 Binary Search Trees
- #25 Heaps and Priority Queues (top-K)
- #26 Graphs: representation (list vs matrix)
- #27 Graph BFS and DFS
- #28 Topological Sort (dependency order)
- #29 Union-Find
- #30 Dijkstra (shortest path)
- #31 Tries (autocomplete)

### Advanced techniques
- #32 Recursion, explained without the magic
- #33 Backtracking
- #34 Greedy algorithms (and when greedy is wrong)
- #35 Dynamic Programming: the idea
- #36 DP: memoization vs tabulation
- #37 Bit manipulation basics

### Wrap-up
- #38 The pattern cheat-sheet: clue words → pattern → example problem (CAROUSEL, recaps #08)
- #39 How I practise DSA (a repeatable routine) [PERSONAL]

## Content opportunities
Explain a concept · Brute force vs optimised · A mistake I made · Pattern in a
real system · Interview phrasing
