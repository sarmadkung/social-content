SERIES:    DSA SERIES #11
TITLE:     Prefix Sum
PILLAR:    DSA & Problem Solving — for juniors and mid-level devs handling range queries
LEVEL:     INTERMEDIATE
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Add once, answer any range instantly
LAYOUT:    FLOW
STATUS:    draft
---
Summing a range of an array is O(n).
Doing it for 10,000 different ranges is the slow part. Prefix sums make each one O(1).

What is it?
A prefix sum array stores running totals. pre[i] is the sum of the first i items.
Think of a car's odometer. To know the distance from town A to town B, you do not re-drive the road. You subtract: reading at B minus reading at A.

Why do we need it?
Without it, every range question walks the range again. With q questions on n items, that is O(n·q). With prefix sums, it is O(n + q).

Key properties
→ Build once: O(n) time, O(n) space
→ Sum of a[l..r] = pre[r + 1] − pre[l]: O(1)
→ Works with negative numbers, unlike a shrinking window
→ Slow if the array changes: one update can shift O(n) totals

Example
const a = [3, 1, 4, 1, 5];
const pre = [0];
for (const x of a) pre.push(pre[pre.length - 1] + x);
// pre = [0, 3, 4, 8, 9, 14]
const rangeSum = (l, r) => pre[r + 1] - pre[l];
rangeSum(1, 3); // 1 + 4 + 1 = 6

Why start with 0? It makes the range starting at index 0 work with no special case.

The interview version: count subarrays that sum to k.
1. Walk the array and keep a running sum.
2. A subarray ending here sums to k if (sum − k) appeared as an earlier running sum.
3. Keep a hash map: running sum → how many times seen.
4. Add that count to the answer, then record the current sum.
O(n) time, O(n) space. It is post #07's hash map trick, applied to totals.

Where is it used?
• Running totals in analytics, like SQL's SUM() OVER (ORDER BY ...)
• 2D prefix sums (summed-area tables) in image processing and fast face detection
• Cumulative counts behind histograms and percentiles
• Time-series queries: "total between 09:00 and 17:00"

Spot it when the problem says…
→ "sum of range [l, r]", asked many times
→ "count subarrays that sum to k" (prefix sum + hash map)
→ negative numbers rule out sliding window, but you still need range sums

When to use it / when not to
Use it: the data does not change, and you ask many range questions.
Not: the data changes often. Use a Fenwick tree or segment tree, with O(log n) updates and queries.

Takeaway: precompute the running total once. Every range becomes one subtraction.

Next: Kadane's Algorithm — the largest subarray sum in one pass.

#Algorithms #DataStructures #PrefixSum #CodingInterviews #ProblemSolving
