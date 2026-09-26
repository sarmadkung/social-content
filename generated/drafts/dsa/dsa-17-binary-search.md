SERIES:    DSA SERIES #17
TITLE:     Binary Search (and "Binary Search on the Answer")
PILLAR:    DSA & Problem Solving — for juniors learning it and mid-level devs who want the "on the answer" version
LEVEL:     INTERMEDIATE
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Halve the space until one remains
LAYOUT:    FLOW
STATUS:    draft
---
Finding one value in 1 billion sorted numbers takes at most 30 checks.
The idea is easy. The off-by-one errors are not.

What is it?
Binary search finds a target in sorted data. It checks the middle, then throws away the half that cannot hold the answer.
Think of the "higher or lower" game with numbers 1 to 100. Guess the middle each time. 7 guesses are always enough.

Why do we need it?
Checking items one by one is O(n). Binary search is O(log n): each step halves what is left.

Key properties
→ O(log n) time, O(1) space
→ Needs sorted data, or a yes/no test that flips only once
→ Needs jumping to any index: on a linked list, reaching the middle is O(n)

Example
function firstTrue(lo, hi, ok) {
  while (lo < hi) {
    const mid = lo + Math.floor((hi - lo) / 2);
    if (ok(mid)) hi = mid; else lo = mid + 1;
  }
  return lo;
}
const a = [1, 3, 5, 7, 9];
firstTrue(0, a.length, i => a[i] >= 7); // 3

It returns the first spot where ok is true. ok(mid) true? The answer is mid or to its left. False? It is to the right.

Binary search on the answer
Example: work piles [3, 6, 7, 11]. Each hour you do up to k units of one pile. Smallest k that finishes in 8 hours?
1. Search the answers, not an array: k is 1 to 11.
2. Test k. k = 3 takes 10 hours. k = 4 takes 8.
3. A bigger k also finishes, so the test flips once.
4. firstTrue(1, 11, k => hours(k) <= 8) returns 4.
Cost: O(n log m), where m is the largest pile.

The senior detail: (lo + hi) / 2 overflowed in Java's Arrays.binarySearch for about nine years. lo + (hi − lo) / 2 avoids it in any language.

Where is it used?
• git bisect: finds the commit that broke a build in O(log n) test runs
• B-tree database indexes, inside each page

[PERSONAL: a time you used git bisect or a halving search to find a bug or a limit]

Spot it when the problem says…
→ "sorted" + "find" in O(log n)
→ "minimum speed / capacity / days so that it works"
→ a yes/no test that flips from false to true only once

When to use it / when not to
Use it: sorted data, or "find the smallest x that works".
Not: unsorted data you search once. Sorting first costs O(n log n).

Takeaway: if a yes/no answer flips only once, you can binary search it.

Next: Sorting — what every developer should know: stable, in-place, O(n log n).

#Algorithms #DataStructures #BinarySearch #CodingInterviews #ProblemSolving
