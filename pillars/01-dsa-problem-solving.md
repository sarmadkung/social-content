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
- #01 Reclaiming DSA in the age of AI · PERSONAL · needs —
- #02 Big-O in plain English (what it measures, what it ignores) · TEACH · needs —
- #03 Arrays and strings: what each operation really costs (index O(1), insert O(n), the hidden O(n²) of building strings) · WHY · needs #02
- #04 How hash maps work: why lookup is O(1), when it isn't, and Set vs Map · WHY · needs #02, #03
- #05 Hash map patterns: find the partner (Two Sum), group by the right key (anagrams) · TEACH · needs #04

### Patterns on arrays and strings
- #06 Two pointers and sliding window: one pass instead of a nested loop · TEACH · needs #03, #05
- #07 One pass, one running value: prefix sum, Kadane and Boyer–Moore voting · TEACH · needs #05, #06
- #08 Which array pattern? Read the problem for clues, then pick · COMPARE · needs #05, #06, #07
- #09 Binary Search: Halving Sorted Data, Then Halving the Answer · TEACH · needs #02, #03
- #10 Sorting: stable, in-place, and the comparator that bites everyone · TEACH · needs #02
- #11 7 array and string problems, and the pattern that solves each · LIST · needs #08–#10

### Linear structures
- #12 Linked lists: when they beat an array (and why they usually don't), plus fast and slow pointers for cycles · TEACH · needs #03, #06
- #13 Stacks, queues and deques: which one and why (valid parentheses, undo, BFS) · COMPARE · needs #03
- #14 Monotonic stack and deque (next greater element, sliding window max) · TEACH · needs #06, #13

### Trees and graphs
- #15 Trees: why hierarchical data changes how you search, and DFS vs BFS traversals · COMPARE · needs #12, #13
- #16 Binary Search Trees · TEACH · needs #09, #15
- #17 Heaps and Priority Queues (top-K) · TEACH · needs #15
- #18 Graphs: adjacency list vs matrix, then BFS and DFS · TEACH · needs #03, #04, #15
- #19 5 problems that are secretly graphs · LIST · needs #18
- #20 Topological Sort (dependency order) · TEACH · needs #18
- #21 Union-Find · TEACH · needs #18
- #22 Dijkstra (shortest path) · TEACH · needs #17, #18
- #23 Tries (autocomplete) · TEACH · needs #15
- #24 Which graph algorithm? Routes, order, groups, prefixes · COMPARE · needs #20, #21, #22, #23

### Advanced techniques
- #25 What recursion really costs: stack depth and repeated work · TEACH · needs #13
- #26 Backtracking · TEACH · needs #25
- #27 Dynamic Programming: the idea, then memoization vs tabulation · TEACH · needs #25
- #28 Greedy algorithms: when greedy works, and how to tell greedy from DP · COMPARE · needs #10, #27
- #29 Bit tricks you will actually meet in real code · TEACH · needs #02

### Wrap-up
- #30 The pattern cheat-sheet: clue words → pattern → example problem (CAROUSEL, recaps #08) · LIST · needs #08–#29
- #31 How I practise DSA (a repeatable routine) · PERSONAL · needs —

## Content opportunities
Explain a concept · Brute force vs optimised · A mistake I made · Pattern in a
real system · Interview phrasing
