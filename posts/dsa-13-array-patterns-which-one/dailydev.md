TITLE: Two pointers, sliding window, prefix sum or Kadane? Read the clues
COVER: cover.png
---
Four array patterns. All walk the array in O(n). All replace a nested loop. That is why people mix them up. They differ in one thing: what they remember while they walk.

- **Two pointers** remembers two ends, usually of a sorted array. One comparison shows which end can never be in the answer, so you drop it. Clue: "sorted" + "pair" or "triplet".
- **Sliding window** remembers one unbroken range. Add what enters, remove what leaves. Clue: "longest / shortest subarray" + "at most K". If the rule is a sum, every number must be 0 or more.
- **Prefix sum** remembers every running total. Any range sum is one subtraction; add a hash map and it counts subarrays that sum to k, negatives included.
- **Kadane** remembers the best run ending here: extend it, or start again. Clue: "maximum subarray sum", no target given.

**The common wrong choice:** a variable sliding window for "subarray sum equals k" when the array has negative numbers. Removing a negative item makes the sum bigger, so shrinking is no longer safe. Use prefix sum + hash map.

**The senior detail:** Kadane is prefix sum in disguise. The best subarray is the biggest gap between a running total and the smallest total before it. Kadane just does not store the totals.

Before you code, ask what you must remember as you walk. The answer names the pattern.
