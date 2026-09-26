SERIES:    DSA SERIES #10
TITLE:     Sliding Window (Fixed and Variable Size)
PILLAR:    DSA & Problem Solving — for juniors and mid-level devs working on subarray and substring problems
LEVEL:     INTERMEDIATE
FORMAT:    VISUAL
HEADLINE:  Don't recompute. Slide the window.
LAYOUT:    COMPARE
STATUS:    draft
---
"Best run of k days" does not mean re-adding k numbers each time.
Add the new day. Remove the old one. Done.

What is it?
A sliding window is a range of the array, from index start to index end, that moves forward. A subarray is one such unbroken range.
Think of looking out of a train. As it moves, one new tree enters the view and one old tree leaves. You never re-count the whole view.

Why do we need it?
Brute force checks every range from scratch. For windows of size k, that is O(n·k). For all ranges, it can be O(n²) or worse. The window reuses work, so it is O(n).

Two kinds
→ Fixed size: the window is always k long. Slide by one each step.
→ Variable size: grow the end until a rule breaks, then shrink the start until it holds again.

Key properties
→ Time O(n): each item enters the window once and leaves once
→ Space O(1), or O(k) if you track what is inside with a map
→ Works on contiguous ranges only, not on any subset

Example: best sum of k items in a row (fixed)
function maxSumK(a, k) {
  let sum = 0, best = -Infinity;
  for (let i = 0; i < a.length; i++) {
    sum += a[i];
    if (i >= k) sum -= a[i - k];
    if (i >= k - 1) best = Math.max(best, sum);
  }
  return best;
}

Variable size, in steps (longest substring with no repeated letter):
1. Move end forward and add the new letter.
2. If that letter is already inside, move start past its last position.
3. Record end − start + 1 if it is the best so far.

Where is it used?
• Rate limiters: requests in the last 60 seconds
• Moving averages on dashboards and stock charts
• TCP's sliding window for bytes in flight

Spot it when the problem says…
→ "subarray" or "substring" (an unbroken range)
→ "longest", "shortest" or "max sum" of a range
→ "at most K", "without repeating", "window of size k"

When to use it / when not to
Use it: the question is about a contiguous range, and extending or shrinking it changes the answer in one direction.
Not: the array has negative numbers and you shrink "while sum > target". Removing an item can then make the sum bigger, so the rule breaks.

The senior detail: that negative-number case is a common interview trap. The fix is prefix sums.

Takeaway: if you are re-adding the same numbers, slide the window instead.

Next: Prefix Sum — answer any range-sum question in O(1).

#Algorithms #DataStructures #SlidingWindow #CodingInterviews #ProblemSolving
