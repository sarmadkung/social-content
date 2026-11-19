TITLE: sort() does not sort numbers: comparators, stability and in-place
COVER: cover.png
---
`[1, 10, 2].sort()` gives you `[1, 10, 2]`. Not a bug: with no comparator, JavaScript compares the items as strings, and "10" comes before "2". Every language ships a sort; few people read what theirs does.

**The comparator rules**

- Pass one for numbers: `(a, b) => a - b` gives `[1, 2, 10]`.
- It must return a number. `a.age > b.age` returns true or false, never a negative, so the order is wrong. `a.age - b.age` is right.

**Three properties decide which sort you want**

- **Stable:** equal items keep their original order. Sort by date, then stably by author, and each author's posts stay in date order.
- **In-place:** it sorts inside the array, O(1) extra space instead of O(n).
- **Comparison-based:** it compares pairs, so in the worst case it can never beat O(n log n). Counting and radix sort skip comparing, but need keys like small integers.

**The classic four:** merge sort is stable but needs O(n) extra space. Quicksort is in-place but not stable, and O(n²) in the worst case. Heapsort is O(n log n) always and in-place, but not stable. Timsort, a merge and insertion hybrid, is stable and fast on partly sorted data.

"Which sort?" is rarely the real question. Ask instead: does the data have structure the sort can use, do you need stability, and can you afford the extra array?
