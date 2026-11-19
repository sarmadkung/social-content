SERIES:    DSA SERIES #06
TITLE:     Two Pointers and Sliding Window: One Pass Instead of a Nested Loop
PILLAR:    DSA & Problem Solving — for juniors and mid-level devs working on pair, subarray and substring problems
LEVEL:     INTERMEDIATE
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Two pointers replace the nested loop
LAYOUT:    FLOW
VISUALS:   1 = How do two pointers find a pair in one pass? · 2 = Why is it safe to drop an item? · 3 = How does a sliding window reuse work? · 4 = When does a sliding window break? · 5 = Takeaway · rest = text
STATUS:    draft
---
Checking every pair in an array is O(n²).
Re-adding k numbers for every "best run of k days" is O(n·k).

Both waste work the same way: they start from scratch each time.
Two pointers and sliding window walk the array once and keep what they learned.

Part 1: two pointers
Two pointers means keeping two indexes into the same array and moving them by a rule. A pointer here is just an index.
Think of people standing in a line, sorted by height. You need two whose heights add to 340 cm. Start with the shortest and the tallest. Too short together? Swap in the next shortest. Too tall? Swap in the next tallest.

Why do we need it?
The nested loop checks every pair. Because the data is sorted, one comparison tells you which end can never be part of the answer, so that item is dropped for good. So there are at most n steps.

How do two pointers find a pair in one pass?
Pair with a target sum (sorted input):
function pairSum(a, target) {
  for (let l = 0, r = a.length - 1; l < r; ) {
    const s = a[l] + a[r];
    if (s === target) return [l, r];
    s < target ? l++ : r--;
  }
  return null;
}
Time O(n), extra space O(1).
Takeaway: on sorted data, one comparison moves one pointer, so n steps are enough.

Why is it safe to drop an item?
If a[l] + a[r] is too small, a[r] is the biggest partner left. So a[l] can never reach the target with anyone. Drop it. The same logic drops a[r] when the sum is too big.
This rule is the proof. Say it in the interview.
Takeaway: each step proves one item can never be in the answer.

Two pointer shapes
→ Opposite ends usually needs sorted data. Same direction often does not.
→ Opposite ends: pair sum, palindrome check, container with most water
→ Same direction: remove duplicates in place, merge two sorted lists

Where is it used?
• The merge step of merge sort
• Merge joins in databases, walking two sorted inputs
• Diffing and merging sorted lists
• Palindrome and string-reverse checks

Comparison: Two Sum, two ways
Hash map (#05): O(n) time, O(n) space, works on unsorted input.
Two pointers (opposite ends): O(n) time, O(1) space, but needs sorted input. Sorting first adds O(n log n).

Part 2: sliding window
A sliding window is a range of the array, from index start to index end, that moves forward. A subarray is one such unbroken range.
Think of looking out of a train. As it moves, one new tree enters the view and one old tree leaves. You never re-count the whole view.

Why do we need it?
Brute force checks every range from scratch. For windows of size k, that is O(n·k). For all ranges, it can be O(n²) or worse. The window reuses work, so it is O(n).

How does a sliding window reuse work?
Add the new item. Remove the old one. Done.
Best sum of k items in a row (fixed size):
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
→ Fixed size: the window is always k long. Slide by one each step.
→ Variable size: grow the end until a rule breaks, then shrink the start until it holds again.
→ Time O(n): each item enters the window once and leaves once
→ Space O(1), or O(k) if you track what is inside with a map
Takeaway: each item enters once and leaves once, so the whole walk is O(n).

When does a sliding window break?
It works on contiguous ranges only, not on any subset.
It also needs extending or shrinking to change the answer in one direction.
The trap: the array has negative numbers and you shrink "while sum > target". Removing an item can then make the sum bigger, so the rule breaks.
That negative-number case is a common interview trap. The fix is prefix sums (#07).
Takeaway: with negative numbers, a sum-based window can no longer trust its shrink step.

Where is it used?
• Rate limiters: requests in the last 60 seconds
• Moving averages on dashboards and stock charts
• TCP's sliding window for bytes in flight

[FACT_CHECK: TCP uses a sliding window for bytes in flight → RFC 9293 (TCP)]

Spot it when the problem says…
→ "sorted array" + "pair" or "triplet" that sums to a target → two pointers
→ "palindrome", "reverse in place", "compare from both ends" → two pointers
→ "remove duplicates in place" or "merge two sorted lists" → two pointers
→ "subarray" or "substring" (an unbroken range), "longest", "shortest" or "max sum" → sliding window
→ "at most K", "without repeating", "window of size k" → sliding window

When to use it / when not to
Two pointers: the data is sorted, or you compare items from both ends. Not: the data is unsorted and you need original indexes. Use a hash map.
Sliding window: the question is about a contiguous range, and extending or shrinking it changes the answer in one direction. Not: negative numbers with a sum rule.

Keep in mind when you walk with pointers or a window
→ Say the drop rule out loud; it is your correctness proof.
→ Sorting for two pointers costs O(n log n) and loses indexes.
→ See negative numbers? Rule out a sum-based window first.

Takeaway
If a sorted array gives you a pair problem, try two pointers before a nested loop.
If you are re-adding the same numbers, slide the window instead.

Next: one pass, one running value: prefix sum, Kadane and Boyer–Moore voting.

#Algorithms #DataStructures #TwoPointers #SlidingWindow #CodingInterviews
