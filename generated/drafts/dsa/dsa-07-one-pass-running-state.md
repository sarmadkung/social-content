SERIES:    DSA SERIES #07
TITLE:     One Pass, One Running Value: Prefix Sum, Kadane and Boyer–Moore
PILLAR:    DSA & Problem Solving — for juniors and mid-level devs handling range, subarray and counting questions
LEVEL:     INTERMEDIATE
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Walk once. Carry one value.
LAYOUT:    FLOW
VISUALS:   1 = How do running totals answer any range in O(1)? · 2 = How do you count subarrays that sum to k? · 3 = How does Kadane find the best subarray in one pass? · 4 = How does Boyer–Moore find the majority with O(1) memory? · 5 = Takeaway · rest = text
STATUS:    draft
---
Summing a range of an array is O(n). Doing it for 10,000 different ranges is the slow part.
Checking every subarray for the largest sum is O(n²).
Counting every value to find the majority costs O(n) memory.

Three problems, one fix: walk the array once and carry one value.
A running total. The best run so far. A candidate and its count.

Part 1: prefix sum, a running total
A prefix sum array stores running totals. pre[i] is the sum of the first i items.
Think of a car's odometer. To know the distance from town A to town B, you do not re-drive the road. You subtract: reading at B minus reading at A.

Why do we need it?
Without it, every range question walks the range again. With q questions on n items, that is O(n·q). With prefix sums, it is O(n + q).

How do running totals answer any range in O(1)?
const a = [3, 1, 4, 1, 5];
const pre = [0];
for (const x of a) pre.push(pre[pre.length - 1] + x);
// pre = [0, 3, 4, 8, 9, 14]
const rangeSum = (l, r) => pre[r + 1] - pre[l];
rangeSum(1, 3); // 1 + 4 + 1 = 6
→ Build once: O(n) time, O(n) space
→ Sum of a[l..r] = pre[r + 1] − pre[l]: O(1)
→ Works with negative numbers, unlike a shrinking window (#06)
→ Slow if the array changes: one update can shift O(n) totals
Why start with 0? It makes the range starting at index 0 work with no special case.
Takeaway: precompute the running total once; every range becomes one subtraction.

How do you count subarrays that sum to k?
The interview version:
1. Walk the array and keep a running sum.
2. A subarray ending here sums to k if (sum − k) appeared as an earlier running sum.
3. Keep a hash map: running sum → how many times seen.
4. Add that count to the answer, then record the current sum.
O(n) time, O(n) space. It is the find-the-partner trick from #05, applied to totals.
Seed the map with 0 → 1, or you miss subarrays starting at index 0.
Takeaway: a running total plus a hash map turns "count subarrays" into one pass.

Where prefix sums are used
• Running totals in analytics, like SQL's SUM() OVER (ORDER BY ...)
• 2D prefix sums (summed-area tables) in image processing and fast face detection
• Cumulative counts behind histograms and percentiles
• Time-series queries: "total between 09:00 and 17:00"

[FACT_CHECK: summed-area tables are used for fast face detection → Viola & Jones 2001 (integral image); Crow 1984 (summed-area tables)]

When not to use it: the data changes often. Use a Fenwick tree or segment tree, with O(log n) updates and queries.

Part 2: Kadane, the best run so far
Kadane's algorithm finds the subarray with the largest sum. A subarray is an unbroken run of items, like a[2..5].
Think of a stock you are holding. If it has lost money overall, you do not carry that loss forward. You sell and start fresh from today.

Why do we need it?
Trying every start and end is O(n²) with running sums. On 1 million items, that is too slow. Kadane keeps only what matters: the best sum ending right here.

How does Kadane find the best subarray in one pass?
function maxSubarray(a) {
  let cur = a[0], best = a[0];
  for (let i = 1; i < a.length; i++) {
    cur = Math.max(a[i], cur + a[i]);
    best = Math.max(best, cur);
  }
  return best;
}
maxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]); // 6, from [4, -1, 2, 1]
The key line: extend the old run, or start again at a[i]. Pick the bigger one.
→ O(n) time, O(1) extra space
→ One pass, so it works on a stream of numbers
→ It is dynamic programming: best ending at i builds on best ending at i − 1
→ Works with negative numbers, including an all-negative array
The common bug: starting best at 0. On [-3, -1, -2] you return 0, but the right answer is -1. Start from a[0].
Takeaway: at every step, ask whether your past helps you or you should start over.

The link to prefix sums: sum of a[l..r] = pre[r + 1] − pre[l]. So the best subarray is the biggest gap between a running total and the smallest total before it. Kadane is that idea without storing the array.

Where Kadane is used
• Stock profit: turn prices into daily changes, then run Kadane
• Best period in a series of gains and losses
• Brightest rectangle in a 2D grid: Kadane on column sums, O(n³) for an n×n grid
• Highest-scoring segment in DNA and protein sequences

[FACT_CHECK: max-subarray is used for highest-scoring segments in DNA and protein sequences → Karlin & Altschul 1990; Ruzzo & Tompa 1999]

When not to use it: items need not be next to each other. Then sum the positives (or take the largest item if none).

Part 3: Boyer–Moore voting, a candidate and its count
Kadane reset its running sum when it turned negative. Boyer–Moore uses the same reset trick to find a majority in O(1) memory.
The majority element is the value that appears more than n/2 times, where n is the number of items. Boyer–Moore finds it in one pass with just a candidate and a counter.
Think of a room where people pair up. Each pair must hold two different opinions, and both leave. If one opinion has more than half the room, someone holding it is still standing at the end.

Why do we need it?
The usual fix is a hash map of counts: O(n) time, but also O(n) memory. Boyer–Moore keeps two variables. That matters when the data is huge or arrives as a stream you cannot store.

How does Boyer–Moore find the majority with O(1) memory?
function majority(a) {
  let cand = null, count = 0;
  for (const x of a) {
    if (count === 0) cand = x;
    count += x === cand ? 1 : -1;
  }
  return cand;
}
majority([2, 2, 1, 1, 1, 2, 2]); // 2
1. Count is 0? The current item becomes the candidate.
2. Same as the candidate? Count up.
3. Different? Count down. One vote cancels one vote.
→ O(n) time, O(1) extra space
→ One pass is enough if a majority is guaranteed
→ If it is not guaranteed, do a second pass to count the candidate
→ It finds "more than half", not the most common value
The trap: majority([1, 2, 3]) returns 3. There is no majority, but the code still returns something. Always verify unless the problem promises one.
Takeaway: when opposite votes cancel, the majority is the one left standing.

Where Boyer–Moore is used
• Interview classic: Majority Element (LeetCode 169)
• Its generalisation, Misra–Gries, finds frequent items in data streams, like top queries or heavy network traffic
• With two candidates, it finds every value above n/3 (LeetCode 229)

[FACT_CHECK: Majority Element is LeetCode 169 → leetcode.com/problems/majority-element]
[FACT_CHECK: Misra–Gries generalises Boyer–Moore voting to frequent items in streams → Misra & Gries 1982, "Finding repeated elements"]
[FACT_CHECK: the n/3 version is LeetCode 229 → leetcode.com/problems/majority-element-ii]

When not to use it: you need the top value with no majority, or all counts. Use a hash map.

Name check: same authors as the Boyer–Moore string search, but a different algorithm.

[FACT_CHECK: voting algorithm has the same authors (Boyer and Moore) as the string search → Boyer & Moore, MJRTY 1981/1991; Boyer & Moore 1977 string search paper]

Spot it when the problem says…
→ "sum of range [l, r]", asked many times → prefix sum
→ "count subarrays that sum to k" → prefix sum + hash map
→ negative numbers rule out sliding window, but you still need range sums → prefix sum
→ "maximum (or minimum) subarray sum", "best contiguous stretch" → Kadane
→ "majority element", "appears more than n/2 times", "O(1) extra space" → Boyer–Moore
→ "more than n/3 times" → Boyer–Moore with two candidates

When to use which
Prefix sum: the data does not change, and you ask many range questions.
Kadane: largest (or smallest) contiguous sum.
Boyer–Moore: "more than half" and memory is tight.

Keep in mind when you carry a running value
→ Prefix sums: seed the map with 0 → 1 before you walk.
→ Kadane: start best at a[0], never at 0.
→ Boyer–Moore: verify the candidate unless a majority is promised.
→ Data that changes often breaks prefix sums; use a Fenwick tree.

Takeaway
One pass, one value carried forward, replaces a nested loop.
Pick the value by the question: a running total, the best run so far, or a candidate and its count.

Next: which array pattern? How to read a problem for clues before you write code.

#Algorithms #DataStructures #PrefixSum #CodingInterviews #ProblemSolving
