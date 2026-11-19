SERIES:    DSA SERIES #08
TITLE:     Which Array Pattern? Read the Problem for Clues, Then Pick
PILLAR:    DSA & Problem Solving — for juniors and mid-level devs who know the patterns but freeze or mix them up on new problems
LEVEL:     INTERMEDIATE
MODE:      COMPARE
FORMAT:    VISUAL
HEADLINE:  Read the problem for clues, not code
LAYOUT:    GRID
VISUALS:   1 = Which clue words point to which pattern? · 2 = What do you do before you write any code? · 3 = What does each array pattern remember? · 4 = One array, which pattern answers each question? · 5 = Takeaway · rest = text
STATUS:    draft
---
Solving 500 problems does not help if every new one feels new.
And knowing five array patterns does not help if you pick the wrong one.

Two pointers, sliding window, prefix sum, Kadane and the hash map trick all walk an array in O(n). All replace a nested loop. That is exactly why people mix them up.

What is a pattern?
A pattern is a reusable way of solving a whole family of problems. Two Sum, "pair with target sum" and "3Sum" look different, but they are the same idea.
Most interview problems reuse a small set of patterns — lists differ, but it is a few dozen at most. Each new problem is usually an old pattern wearing a new costume.
Think of a mechanic. They do not memorise every car. They hear a noise, and it points to a part.

Why do we need it?
Memorised answers break when the problem changes one word. A pattern still works, because you know why it works. Most of the work is picking the right one.

Which clue words point to which pattern?
→ "sorted" + "pair" → Two Pointers
→ "subarray" / "substring", "longest", "at most K" → Sliding Window
→ "sum of range", asked many times → Prefix Sum
→ "seen before?", "count", "find the partner" → Hash Map / Set
→ "maximum subarray sum", no target given → Kadane
→ "sorted" or "smallest x that works" → Binary Search
→ "top K", "K-th largest" → Heap
→ "all combinations / subsets" → Backtracking
→ "number of ways", "min cost", choices that repeat → Dynamic Programming
Takeaway: the problem statement names its pattern; underline the words that do.

What do you do before you write any code?
1. Underline the clue words: sorted, contiguous, k, all, minimum.
2. Check the limits. n up to 10⁵ means you need about O(n log n) or better.
3. Say the brute force out loud, then ask what work it repeats.
4. Match that repeated work to a pattern from the list above.
Takeaway: the repeated work in the brute force tells you what to remember.

[FACT_CHECK: n up to 10⁵ means O(n log n) or better → competitive-programming limit tables (e.g. USACO Guide, CP-Algorithms / Codeforces rules of thumb)]

The shared problem
Each array pattern avoids the O(n²) loop that checks every pair or every range. They differ in what they remember while they walk.

What does each array pattern remember?
Two pointers (#06): two indexes, often at both ends of a sorted array. One comparison shows which end can never be in the answer, so you drop it. O(n) time, O(1) space.
Sliding window (#06): an unbroken range that moves forward. Add what enters, remove what leaves. Variable size: grow until a rule breaks, then shrink. O(n) time, O(1) space, or O(k) with a map.
Prefix sum (#07): running totals, built once. Any range sum is one subtraction. Add a hash map and it counts subarrays that sum to k. O(n) to build, then O(1) per range. O(n) space.
Kadane (#07): one pass that keeps the best sum ending here. At each item: extend the run, or start again. O(n) time, O(1) space.
Takeaway: same O(n) walk; the difference is what each one carries.

Spot it when the problem says…
→ Two pointers: "sorted" + "pair" or "triplet", or compare from both ends
→ Sliding window: "longest / shortest subarray or substring" with a rule like "at most K". If the rule is a sum, all numbers must be 0 or more.
→ Prefix sum: many range-sum questions, or "count subarrays that sum to k", especially with negative numbers
→ Kadane: "maximum (or minimum) subarray sum", with no target given

One array, which pattern answers each question?
a = [2, -1, 3, -4, 5]
→ Two items that sum to 4? Sort to [-4, -1, 2, 3, 5], then two pointers: -1 + 5.
→ Sum of a[1..3], asked 10,000 times? Prefix sum: pre[4] − pre[1] = -2.
→ How many subarrays sum to 4? Prefix sum + hash map. Answer: 2.
→ Largest subarray sum? Kadane. Answer: 5.
→ Longest subarray with sum at most 3? A sliding window looks right, but -1 and -4 break it. Removing an item can make the sum bigger, so shrinking is no longer safe.
Takeaway: the same array needs a different pattern for each question.

The common wrong choice
Using a variable sliding window for "subarray sum equals k" when the array has negative numbers. Use prefix sum + hash map instead.

The senior detail: Kadane is prefix sum in disguise. The best subarray is the biggest gap between a running total and the smallest total before it. Kadane just does not store the totals.

Where is it used?
• Coding interviews: the interviewer is checking step 4
• Real code: a "find duplicates" task in a log pipeline is a hash set
• Reviews: spotting an O(n²) loop that a pattern would make O(n)

When to use it / when not to
Use it: before coding any new problem.
Not: to force a pattern that does not fit. If no clue matches, the brute force is your starting point.

Keep in mind when you pick an array pattern
→ See negative numbers? Rule out a sum-based window first.
→ Sorting for two pointers costs O(n log n) and loses indexes.
→ Seed the prefix-sum map with 0 → 1, or you miss subarrays starting at index 0.
→ No clue matches? Start from the brute force, not a guess.

Takeaway
Do not ask "have I seen this problem?" Ask "what is this problem asking me to repeat?"
Then ask what you must remember as you walk: two ends, a range, every total, or the best run so far.

Next: binary search: halving sorted data, then halving the answer.

#Algorithms #DataStructures #ProblemSolving #CodingInterviews #PatternRecognition
