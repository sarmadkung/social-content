SERIES:    DSA SERIES #09
TITLE:     Two Pointers
PILLAR:    DSA & Problem Solving — for students and juniors preparing for coding interviews
HEADLINE:  Two pointers replace the nested loop
LAYOUT:    FLOW
---
Checking every pair in an array is O(n²).
If the array is sorted, you can do it in O(n) with no extra memory.

What is it?
Two pointers means keeping two indexes into the same array and moving them by a rule. A pointer here is just an index.
Think of people standing in a line, sorted by height. You need two whose heights add to 340 cm. Start with the shortest and the tallest. Too short together? Swap in the next shortest. Too tall? Swap in the next tallest.

Why do we need it?
The nested loop checks pairs that can never work. Two pointers skip them. Each step removes one item for good. So there are at most n steps.

Key properties
→ Time O(n), extra space O(1)
→ Usually needs sorted data, or some order to exploit
→ Opposite ends: pair sum, palindrome check, container with most water
→ Same direction: remove duplicates in place, merge two sorted lists

Example: pair with a target sum (sorted input)
function pairSum(a, target) {
  for (let l = 0, r = a.length - 1; l < r; ) {
    const s = a[l] + a[r];
    if (s === target) return [l, r];
    s < target ? l++ : r--;
  }
  return null;
}

Why is it safe to move l? If a[l] + a[r] is too small, a[r] is the biggest partner left. So a[l] can never reach the target with anyone. Drop it. The same logic drops a[r] when the sum is too big. This rule is the proof. Say it in the interview.

Where is it used?
• The merge step of merge sort
• Merge joins in databases, walking two sorted inputs
• Diffing and merging sorted lists
• Palindrome and string-reverse checks

Spot it when the problem says…
→ "sorted array" + "pair" or "triplet" that sums to a target
→ "palindrome", "reverse in place", "compare from both ends"
→ "remove duplicates in place" or "merge two sorted lists"

When to use it / when not to
Use it: the data is sorted, or you compare items from both ends.
Not: the data is unsorted and you need original indexes. Use a hash map.

Comparison: Two Sum, two ways
Hash map: O(n) time, O(n) space, works on unsorted input.
Two pointers: O(n) time, O(1) space, but needs sorted input. Sorting first adds O(n log n).

Takeaway: if a sorted array gives you a pair problem, try two pointers before a nested loop.

Next: Sliding Window — the same idea, moving over ranges instead of pairs.

#Algorithms #DataStructures #TwoPointers #CodingInterviews #ProblemSolving
