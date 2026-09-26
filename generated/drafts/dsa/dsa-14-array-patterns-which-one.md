SERIES:    DSA SERIES #14
TITLE:     Two Pointers vs Sliding Window vs Prefix Sum vs Kadane: Which One?
PILLAR:    DSA & Problem Solving — for juniors and mid-level devs who know the patterns but mix them up
LEVEL:     INTERMEDIATE
MODE:      COMPARE
FORMAT:    VISUAL
HEADLINE:  Four array patterns, four different clues
LAYOUT:    GRID
STATUS:    draft
---
Four patterns. All walk an array in O(n). All replace a nested loop.
That is exactly why people mix them up.

The shared problem
Each one avoids the O(n²) loop that checks every pair or every range. They differ in what they remember while they walk.

Two pointers (post #10)
Two indexes, often at both ends of a sorted array. One comparison shows which end can never be in the answer, so you drop it.
O(n) time, O(1) space.

Sliding window (post #11)
An unbroken range that moves forward. Add what enters, remove what leaves. Variable size: grow until a rule breaks, then shrink.
O(n) time, O(1) space, or O(k) with a map.

Prefix sum (post #12)
Running totals, built once. Any range sum is one subtraction. Add a hash map and it counts subarrays that sum to k.
O(n) to build, then O(1) per range. O(n) space.

Kadane (post #13)
One pass that keeps the best sum ending here. At each item: extend the run, or start again.
O(n) time, O(1) space.

Spot it when the problem says…
→ Two pointers: "sorted" + "pair" or "triplet", or compare from both ends
→ Sliding window: "longest / shortest subarray or substring" with a rule like "at most K". If the rule is a sum, all numbers must be 0 or more.
→ Prefix sum: many range-sum questions, or "count subarrays that sum to k", especially with negative numbers
→ Kadane: "maximum (or minimum) subarray sum", with no target given

One array, four questions
a = [2, -1, 3, -4, 5]
→ Two items that sum to 4? Sort to [-4, -1, 2, 3, 5], then two pointers: -1 + 5.
→ Sum of a[1..3], asked 10,000 times? Prefix sum: pre[4] − pre[1] = -2.
→ How many subarrays sum to 4? Prefix sum + hash map. Answer: 2.
→ Largest subarray sum? Kadane. Answer: 5.
→ Longest subarray with sum at most 3? A sliding window looks right, but -1 and -4 break it. Removing an item can make the sum bigger, so shrinking is no longer safe.

The common wrong choice
Using a variable sliding window for "subarray sum equals k" when the array has negative numbers. Use prefix sum + hash map instead.

The senior detail: Kadane is prefix sum in disguise. The best subarray is the biggest gap between a running total and the smallest total before it. Kadane just does not store the totals.

Takeaway: ask what you must remember as you walk. Two ends, a range, every total, or the best run so far.

Next: Boyer–Moore Voting — find the majority element with O(1) memory.

#Algorithms #DataStructures #CodingInterviews #ProblemSolving #PatternRecognition
