SERIES:    DSA SERIES #16
TITLE:     Sorting: stable, in-place, and the comparator that bites everyone
PILLAR:    DSA & Problem Solving — for juniors who use sort() daily and mid-levels who get asked "which sort, and why"
LEVEL:     INTERMEDIATE
HEADLINE:  sort() does not sort numbers
LAYOUT:    STATEMENT
STATUS:    draft
VARIANT:   C (source mode)
---
[1, 10, 2].sort() gives you [1, 10, 2].
Not a bug. JavaScript converted every element to a string first.

What is it?
Sorting puts elements in order. Every language ships one. Almost nobody reads what theirs actually does.

Three properties decide which sort you want:

Stable — equal elements keep their original order. Sort by date, then by author, and a stable sort keeps the dates in order inside each author. An unstable one scrambles them.

In-place — it sorts inside the array instead of allocating a second one. O(1) extra space instead of O(n).

Comparison-based — it works by comparing pairs, which caps it at O(n log n). Counting sort and radix sort beat that by not comparing at all, but they need small integer keys.

Why do we need it?
Sorted data unlocks other things. Binary search needs it. Two pointers usually needs it. Deduplication becomes one pass. Merging two datasets becomes one pass.

Key properties
→ Merge sort: O(n log n), stable, needs O(n) extra space
→ Quicksort: O(n log n) average, O(n²) worst, in-place, not stable
→ Heapsort: O(n log n) always, in-place, not stable
→ Timsort (Python, Java objects, V8): merge + insertion hybrid, stable, fast on partly-sorted real data

Example
// the default comparator is lexicographic
[1, 10, 2].sort();              // [1, 10, 2]
[1, 10, 2].sort((a, b) => a - b); // [1, 2, 10]

// a comparator must return a number, not a boolean
arr.sort((a, b) => a.age > b.age);      // wrong: true/false
arr.sort((a, b) => a.age - b.age);      // right: negative/zero/positive

Spot it when the problem says…
→ "pairs", "duplicates", "closest" or "overlapping intervals" on unsorted data
→ order helps but the input has none: sort first, then two pointers or binary search
→ the limits allow O(n log n) but not O(n²)

The interview takeaway
"Which sorting algorithm" is rarely the real question. The real one is: does your data have structure the sort can exploit, do you need stability, and can you afford the extra array? Answer those three and the algorithm picks itself.

What is the worst sorting bug you have shipped?
