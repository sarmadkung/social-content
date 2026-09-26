SERIES:    DSA SERIES #13
TITLE:     Kadane's Algorithm (Maximum Subarray)
PILLAR:    DSA & Problem Solving — for juniors and mid-level devs preparing for subarray interview questions
LEVEL:     INTERMEDIATE
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Drop the past when it hurts
LAYOUT:    FLOW
STATUS:    draft
---
Checking every subarray to find the largest sum is O(n²).
Kadane's algorithm does it in one pass, with two variables.

What is it?
Kadane's algorithm finds the subarray with the largest sum. A subarray is an unbroken run of items, like a[2..5].
Think of a stock you are holding. If it has lost money overall, you do not carry that loss forward. You sell and start fresh from today.

Why do we need it?
Trying every start and end is O(n²) with running sums. On 1 million items, that is too slow. Kadane keeps only what matters: the best sum ending right here.

Key properties
→ O(n) time, O(1) extra space
→ One pass, so it works on a stream of numbers
→ It is dynamic programming: best ending at i builds on best ending at i − 1
→ Works with negative numbers, including an all-negative array

Example
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

The common bug: starting best at 0. On [-3, -1, -2] you return 0, but the right answer is -1. Start from a[0].

The link to post #12: sum of a[l..r] = pre[r + 1] − pre[l]. So the best subarray is the biggest gap between a running total and the smallest total before it. Kadane is that idea without storing the array.

Where is it used?
• Stock profit: turn prices into daily changes, then run Kadane
• Best period in a series of gains and losses
• Brightest rectangle in a 2D grid: Kadane on column sums, O(n³) for an n×n grid
• Highest-scoring segment in DNA and protein sequences

Spot it when the problem says…
→ "maximum (or minimum) subarray sum"
→ "best contiguous stretch", like max profit over a run of days
→ one pass, where each step asks: extend the run, or start again here?

When to use it / when not to
Use it: largest (or smallest) contiguous sum.
Not: items need not be next to each other. Then sum the positives (or take the largest item if none).

Takeaway: at every step, ask one question. Does my past help me, or should I start over?

Next: two pointers vs sliding window vs prefix sum vs Kadane — which one?

#Algorithms #DataStructures #DynamicProgramming #CodingInterviews #ProblemSolving
