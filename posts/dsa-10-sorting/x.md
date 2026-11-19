[1, 10, 2].sort() gives you [1, 10, 2].

Not a bug. With no comparator, JavaScript compares the items as strings, and "10" comes before "2".
[images: 0, 1]
---
The fix is a comparator, and it must return a number:

a.age > b.age → true/false, never negative: wrong order
a.age - b.age → negative, zero or positive: right

Sorting strings? Use a.localeCompare(b). a - b gives NaN.
---
Three properties decide which sort you want:

Stable: equal items keep their original order
In-place: no second array, O(1) extra space
Comparison-based: compares pairs, so it can't beat O(n log n) in the worst case
[images: 2]
---
Merge sort: stable, needs O(n) extra space.
Quicksort: in-place, not stable, O(n²) worst case.
Heapsort: O(n log n) always, in-place, not stable.
Timsort: merge + insertion hybrid, stable, fast on partly sorted data.
[images: 3]
---
"Which sort?" is rarely the real question. Ask: does the data have structure to use, do you need stability, can you afford the extra array?

What is the worst sorting bug you have shipped?

#Algorithms #JavaScript
