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
- #02 How we measure an algorithm: time and space complexity · TEACH · needs —
- #03 Big-O in plain English (what it measures, what it ignores) · TEACH · needs #02
- #04 Arrays: why index access is O(1) but insert is O(n) · WHY · needs #03
- #05 Strings are arrays too (immutability, building strings efficiently) · TEACH · needs #04
- #06 Why a hash map lookup is O(1) — and when it isn't · WHY · needs #03, #04
- #07 Hash Set vs Hash Map: which one and why · COMPARE · needs #06
- #08 Hash maps: the pattern behind Two Sum · TEACH · needs #06

### Patterns on arrays and strings
- #09 Every DSA problem has a pattern — how to spot it · LIST · needs #08
- #10 Two Pointers · TEACH · needs #04, #09
- #11 Sliding Window (fixed and variable size) · TEACH · needs #10
- #12 Prefix Sum · TEACH · needs #04
- #13 Kadane's Algorithm (max subarray) · TEACH · needs #12
- #14 Two pointers vs sliding window vs prefix sum vs Kadane: which one? · COMPARE · needs #10, #11, #12, #13
- #15 Boyer–Moore Voting (majority element) · TEACH · needs #06
- #16 Anagrams and Group Anagrams (frequency counting) · TEACH · needs #05, #06
- #17 Binary Search (and "binary search on the answer") · TEACH · needs #03, #04
- #18 Sorting: stable, in-place, O(n log n) · TEACH · needs #03
- #19 7 array and string problems, and the pattern that solves each · LIST · needs #09–#18

### Linear structures
- #20 Linked Lists (and when you would actually use one) · TEACH · needs #04
- #21 Fast and Slow Pointers (cycle detection) · TEACH · needs #10, #20
- #22 Stacks (valid parentheses, undo) · TEACH · needs #04
- #23 Queues and Deques (BFS, sliding window max) · TEACH · needs #22
- #24 Stack vs queue vs deque: which one? · COMPARE · needs #22, #23
- #25 Monotonic Stack (next greater element) · TEACH · needs #22

### Trees and graphs
- #26 Trees and Binary Trees · TEACH · needs #20
- #27 Tree traversals: DFS vs BFS · COMPARE · needs #22, #23, #26
- #28 Binary Search Trees · TEACH · needs #17, #26
- #29 Heaps and Priority Queues (top-K) · TEACH · needs #26
- #30 Graphs: representation (list vs matrix) · TEACH · needs #04, #06
- #31 Graph BFS and DFS · TEACH · needs #27, #30
- #32 5 problems that are secretly graphs · LIST · needs #30, #31
- #33 Topological Sort (dependency order) · TEACH · needs #31
- #34 Union-Find · TEACH · needs #30
- #35 Dijkstra (shortest path) · TEACH · needs #29, #31
- #36 Tries (autocomplete) · TEACH · needs #26
- #37 Which graph algorithm? Routes, order, groups, prefixes · COMPARE · needs #33, #34, #35, #36

### Advanced techniques
- #38 Recursion, explained without the magic · TEACH · needs #22
- #39 Backtracking · TEACH · needs #38
- #40 Greedy algorithms (and when greedy is wrong) · TEACH · needs #18
- #41 Dynamic Programming: the idea · TEACH · needs #38
- #42 Greedy vs DP: how to tell which one a problem needs · COMPARE · needs #40, #41
- #43 DP: memoization vs tabulation · COMPARE · needs #41
- #44 Bit manipulation basics · TEACH · needs #03

### Wrap-up
- #45 The pattern cheat-sheet: clue words → pattern → example problem (CAROUSEL, recaps #09) · LIST · needs #09–#44
- #46 How I practise DSA (a repeatable routine) · PERSONAL · needs —

## Content opportunities
Explain a concept · Brute force vs optimised · A mistake I made · Pattern in a
real system · Interview phrasing
