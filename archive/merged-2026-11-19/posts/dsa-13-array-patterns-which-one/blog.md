---
title: "Two pointers, sliding window, prefix sum or Kadane? Read the clues"
description: "Four O(n) array patterns that people mix up, what each one remembers, the clue words that point to it, and the common wrong choice."
date: 2027-02-10
series: "DSA Series"
seriesNumber: 13
slug: dsa-13-array-patterns-which-one
tags: [algorithms, data-structures, arrays, coding-interviews]
cover: cover.png
---

Four patterns. All walk an array in O(n). All replace a nested loop.

That is exactly why people mix them up. The last four posts in this series taught them one at a time. This one puts them side by side, so you can tell which one a problem needs.

## What we'll cover

![In this post: what each pattern remembers, the clue words, one array with four questions, and Kadane as prefix sum](0.png)

1. **What each pattern remembers** as it walks the array.
2. **The clue words** in a problem that point to each one.
3. **One array, four questions:** the same input, a different pattern each time.
4. **Kadane is prefix sum in disguise:** the link most people miss.

## The shared problem

Each pattern avoids the O(n²) loop that checks every pair or every range. A **subarray** is an unbroken run of items, like `a[1..3]`. With n items there are about n²/2 subarrays, so checking them all is slow.

The four patterns differ in what they remember while they walk.

## What each pattern remembers

![Two pointers remembers two ends, sliding window one range, prefix sum every running total, Kadane the best run ending here](1.png)

- **Two pointers** (post #09) keeps two indexes, often at both ends of a sorted array. One comparison shows which end can never be in the answer, so you drop it. O(n) time, O(1) space.
- **Sliding window** (post #10) keeps one unbroken range that moves forward. Add what enters, remove what leaves. With a variable size, grow until a rule breaks, then shrink. O(n) time, O(1) space, or O(k) with a map of what is inside.
- **Prefix sum** (post #11) keeps running totals, built once. `pre[i]` is the sum of the first i items, so any range sum is one subtraction. Add a hash map and it counts subarrays that sum to k. O(n) to build, O(1) per range, O(n) space.
- **Kadane** (post #12) keeps the best sum ending at the current item. At each item: extend the run, or start again. O(n) time, O(1) space.

## The clue words

![Each pattern with the words in a problem statement that point to it, plus the common wrong choice](2.png)

- **Two pointers:** "sorted" + "pair" or "triplet", or you compare from both ends.
- **Sliding window:** "longest / shortest subarray or substring" with a rule like "at most K". If the rule is a sum, all numbers must be 0 or more.
- **Prefix sum:** many range-sum questions, or "count subarrays that sum to k", especially with negative numbers.
- **Kadane:** "maximum (or minimum) subarray sum", with no target given.

Clues do not guarantee the pattern. They tell you which one to try first.

## One array, four questions

![The array [2, -1, 3, -4, 5] with five questions, the pattern for each, and the answer](3.png)

Take `a = [2, -1, 3, -4, 5]`.

- **Two items that sum to 4?** Sort to `[-4, -1, 2, 3, 5]`, then two pointers: -1 + 5.
- **Sum of `a[1..3]`, asked 10,000 times?** Prefix sum: `pre[4] − pre[1] = -2`.
- **How many subarrays sum to 4?** Prefix sum + hash map. Answer: 2.
- **Largest subarray sum?** Kadane. Answer: 5.
- **Longest subarray with sum at most 3?** A sliding window looks right, but -1 and -4 break it. Removing an item can make the sum bigger, so shrinking is no longer safe.

## The common wrong choice

Using a variable sliding window for "subarray sum equals k" when the array has negative numbers. The window shrinks when the sum is too big, which only works if removing an item always makes the sum smaller. A negative item breaks that. Use prefix sum + hash map instead.

## Kadane is prefix sum in disguise

![Running totals of the array as bars: the best subarray sum is the biggest gap between a total and the lowest total before it](4.png)

The sum of `a[l..r]` is `pre[r + 1] − pre[l]`. So the best subarray is the biggest gap between a running total and the smallest total before it. For our array, the totals are `[0, 2, 1, 4, 0, 5]`: the biggest gap is 5 − 0 = 5, the same answer Kadane gives.

Kadane keeps that gap as it walks. It just does not store the totals, which is why it needs O(1) space instead of O(n).

## Keep in mind when you pick an array pattern

- See negative numbers? Rule out a sum-based window first.
- Sorting for two pointers costs O(n log n) and loses the original indexes.
- Seed the prefix-sum map with 0 → 1, or you miss subarrays that start at index 0.

**In one line:** ask what you must remember as you walk. Two ends, a range, every total, or the best run so far.

## Next in the series

Boyer–Moore Voting: finding the majority with O(1) memory.
