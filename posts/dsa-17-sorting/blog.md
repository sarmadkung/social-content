---
title: "sort() does not sort numbers: comparators, stability, in-place"
description: "Why [1, 10, 2].sort() gives [1, 10, 2], how a comparator must work, and the three properties that decide which sort you want."
date: 2027-03-22
series: "DSA Series"
seriesNumber: 17
slug: dsa-17-sorting
tags: [algorithms, sorting, javascript, coding-interviews]
cover: cover.png
---

`[1, 10, 2].sort()` gives you `[1, 10, 2]`.

Not a bug. With no comparator, JavaScript compares the items as strings first. Sorting puts elements in order, and every language ships a sort. Almost nobody reads what theirs actually does.

## What we'll cover

![In this post: the default comparator, three properties, four sorts compared](0.png)

1. **The default comparator:** why `[1, 10, 2]` stays `[1, 10, 2]`, and how to fix it.
2. **Three properties:** stable, in-place, comparison-based.
3. **Four sorts compared:** speed, memory and stability.

## The default comparator

![Code: the default sort compares strings; a comparator must return a number, not true or false](1.png)

A **comparator** is the function you pass to `sort()`. It gets two items, `a` and `b`, and returns a number: negative puts `a` first, positive puts `b` first, 0 means they are equal.

With no comparator, the items are compared as strings. `"10"` comes before `"2"` because the first characters compare first, and `"1"` < `"2"`.

```js
// the default comparator compares strings
[1, 10, 2].sort();                 // [1, 10, 2]
[1, 10, 2].sort((a, b) => a - b);  // [1, 2, 10]

// a comparator must return a number, not a boolean
arr.sort((a, b) => a.age > b.age); // wrong: true/false
arr.sort((a, b) => a.age - b.age); // right: negative/zero/positive
```

`a.age > b.age` returns true or false. As a number that is 1 or 0, never negative, so the sort never learns that `a` should come first.

## Three properties that decide which sort you want

![Stable keeps equal items in order; in-place uses no second array; comparison-based sorts can't beat O(n log n)](2.png)

- **Stable:** equal elements keep their original order. Sort posts by date, then by author, and a stable sort keeps the dates in order inside each author. An unstable one can scramble them.
- **In-place:** it sorts inside the array instead of allocating a second one. O(1) extra space instead of O(n).
- **Comparison-based:** it works by comparing pairs, so in the worst case it can never beat O(n log n). Counting sort and radix sort beat that by not comparing at all, but they only work on keys like small integers or fixed-length strings.

## Why sorting matters

Sorted data makes other things possible. Binary search needs it. Two pointers usually needs it. Removing duplicates becomes one pass, because equal items sit next to each other. Merging two sorted datasets becomes one pass too.

## Four sorts compared

![Merge sort, quicksort, heapsort and Timsort by average and worst time, in-place and stable](3.png)

- **Merge sort:** O(n log n), stable, needs O(n) extra space.
- **Quicksort:** O(n log n) on average, O(n²) in the worst case, in-place, not stable.
- **Heapsort:** O(n log n) always, in-place, not stable.
- **Timsort:** a hybrid of merge sort and insertion sort. Stable, and fast on partly sorted real data.

## Spot it when the problem says…

- "pairs", "duplicates", "closest" or "overlapping intervals" on unsorted data.
- Order would help, but the input has none: sort first, then use two pointers or binary search.
- The limits allow O(n log n), but not O(n²).

## Keep in mind when you call sort()

- Sorting numbers in JS? Always pass a comparator.
- Return `a - b`, never `a > b`: the sign is the answer.
- Strings: use `a.localeCompare(b)`. `a - b` gives NaN.
- `sort()` changes the array. Use `toSorted()` to keep the original.
- Need only the min or max? One O(n) pass beats an O(n log n) sort.

## The interview takeaway

"Which sorting algorithm?" is rarely the real question. The real one is: does your data have structure the sort can use, do you need stability, and can you afford the extra array? Answer those three and the algorithm picks itself.

## Next in the series

7 array and string problems, and the pattern that solves each.
