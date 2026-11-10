Two pointers, sliding window, prefix sum, Kadane.

All four walk an array in O(n). All four replace a nested loop. That is exactly why people mix them up.

The difference is what each one remembers as it walks.
[images: 0, 1]
---
The clues in the problem text:

"sorted" + "pair" → two pointers
"longest subarray" + "at most K" → sliding window
"count subarrays that sum to k" → prefix sum + hash map
"maximum subarray sum" → Kadane
[images: 2]
---
The common wrong choice: a sliding window for "subarray sum equals k" when the array has negative numbers.

Removing a negative item makes the sum bigger, so shrinking the window is no longer safe. Use prefix sum + a hash map instead.
[images: 3]
---
The senior detail: Kadane is prefix sum in disguise.

The best subarray is the biggest gap between a running total and the lowest total before it. Kadane keeps that gap as it walks and never stores the totals.
[images: 4]
---
Before you write the loop, ask: what must I remember? Two ends, a range, every total, or the best run so far.

Next: Boyer–Moore Voting, finding the majority with O(1) memory.

#Algorithms #DSA
