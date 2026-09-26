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
(wrapped in the What / Why / How / Where structure from the master prompt)

Every DSA post also has:
- complexity, and the reason for it ("each step drops one item for good, so n steps")
- a tiny walkthrough on a real input
- the invariant or one-line proof when there is one
- one common mistake (e.g. binary search: the range does not shrink → infinite loop)

## Pattern recognition (required on every pattern post)
Every post that teaches a pattern has a "Spot it when the problem says…" block,
placed just before "When to use it / when not to":

    Spot it when the problem says…
    → "<clue words from the problem statement>"
    → "<another clue>"
    → <a structural clue, e.g. a yes/no test that flips once>

2–3 lines. Clues do not guarantee the pattern; they tell you to try it first.
Clues are words or constraints a reader can find in a problem
statement, not a restated definition. Where two patterns are easy to confuse
(prefix sum vs sliding window vs Kadane), one clue says which to pick.

## Pattern quiz (bonus posts)
Every 3–4 pattern posts, an optional "DSA QUIZ #NN" post: one problem
statement, "Which pattern is this?", answer and reasoning in the first comment.
Only use patterns already taught. Not part of the Monday queue — post as an
extra (e.g. Saturday) when there is time. Drafts go in generated/quiz/dsa/.

## Roadmap (post in this order)
Each line: `#NN Title · MODE · needs <earlier posts>`. Modes are defined in the
master prompt. Never more than 4 TEACH posts in a row.

### Foundations
- #01 Reclaiming DSA: two weeks, 23 algorithms, one repo · PERSONAL · needs —
- #02 Big-O in plain English (what it measures, what it ignores) · TEACH · needs —
- #03 Arrays: why index access is O(1) but insert is O(n) · WHY · needs #02
- #04 Strings are arrays too (immutability, building strings efficiently) · TEACH · needs #03
- #05 Why a hash map lookup is O(1) — and when it isn't · WHY · needs #02, #03
- #06 Hash Set vs Hash Map: which one and why · COMPARE · needs #05
- #07 Hash maps: the pattern behind Two Sum · TEACH · needs #05

### Patterns on arrays and strings
- #08 Every DSA problem has a pattern — how to spot it · LIST · needs #07
- #09 Two Pointers · TEACH · needs #03, #08
- #10 Sliding Window (fixed and variable size) · TEACH · needs #09
- #11 Prefix Sum · TEACH · needs #03
- #12 Kadane's Algorithm (max subarray) · TEACH · needs #11
- #13 Two pointers vs sliding window vs prefix sum vs Kadane: which one? · COMPARE · needs #09, #10, #11, #12
- #14 Boyer–Moore Voting (majority element) · TEACH · needs #05
- #15 Anagrams and Group Anagrams (frequency counting) · TEACH · needs #04, #05
- #16 Binary Search (and "binary search on the answer") · TEACH · needs #02, #03
- #17 Sorting: stable, in-place, O(n log n) · TEACH · needs #02
- #18 7 array and string problems, and the pattern that solves each · LIST · needs #08–#17

### Linear structures
- #19 Linked Lists (and when you would actually use one) · TEACH · needs #03
- #20 Fast and Slow Pointers (cycle detection) · TEACH · needs #09, #19
- #21 Stacks (valid parentheses, undo) · TEACH · needs #03
- #22 Queues and Deques (BFS, sliding window max) · TEACH · needs #21
- #23 Stack vs queue vs deque: which one? · COMPARE · needs #21, #22
- #24 Monotonic Stack (next greater element) · TEACH · needs #21

### Trees and graphs
- #25 Trees and Binary Trees · TEACH · needs #19
- #26 Tree traversals: DFS vs BFS · COMPARE · needs #21, #22, #25
- #27 Binary Search Trees · TEACH · needs #16, #25
- #28 Heaps and Priority Queues (top-K) · TEACH · needs #25
- #29 Graphs: representation (list vs matrix) · TEACH · needs #03, #05
- #30 Graph BFS and DFS · TEACH · needs #26, #29
- #31 5 problems that are secretly graphs · LIST · needs #29, #30
- #32 Topological Sort (dependency order) · TEACH · needs #30
- #33 Union-Find · TEACH · needs #29
- #34 Dijkstra (shortest path) · TEACH · needs #28, #30
- #35 Tries (autocomplete) · TEACH · needs #25
- #36 Which graph algorithm? Routes, order, groups, prefixes · COMPARE · needs #32, #33, #34, #35

### Advanced techniques
- #37 Recursion, explained without the magic · TEACH · needs #21
- #38 Backtracking · TEACH · needs #37
- #39 Greedy algorithms (and when greedy is wrong) · TEACH · needs #17
- #40 Dynamic Programming: the idea · TEACH · needs #37
- #41 Greedy vs DP: how to tell which one a problem needs · COMPARE · needs #39, #40
- #42 DP: memoization vs tabulation · COMPARE · needs #40
- #43 Bit manipulation basics · TEACH · needs #02

### Wrap-up
- #44 The pattern cheat-sheet: clue words → pattern → example problem (CAROUSEL, recaps #08) · LIST · needs #08–#43
- #45 How I practise DSA (a repeatable routine) · PERSONAL · needs —

## Content opportunities
Explain a concept · Brute force vs optimised · A mistake I made · Pattern in a
real system · Interview phrasing
