SERIES:    DSA QUIZ #01
TITLE:     Which Pattern Is This? Shortest Subarray With Sum ≥ K
PILLAR:    DSA & Problem Solving — quiz after DSA #09–#11 (two pointers, sliding window, prefix sum)
HEADLINE:  Which pattern is this?
LAYOUT:    STATEMENT
POST AFTER: DSA SERIES #11 is live
---
Quiz time. No code needed, just the pattern.

You get an array of positive numbers and a number k.
Find the length of the shortest subarray whose sum is at least k.

nums = [2, 3, 1, 2, 4, 3], k = 7 → answer 2 ([4, 3])

Which pattern would you reach for?
A) Two Pointers
B) Sliding Window
C) Prefix Sum
D) Hash Map

Reply with a letter and one clue word that gave it away. Answer in the first comment.

#Algorithms #ProblemSolving #CodingInterviews #DSA
---
FIRST COMMENT (post right after):
Answer: B) Sliding Window.

Clues: "subarray" (an unbroken range) and "shortest". And every number is positive, so growing the window only raises the sum and shrinking it only lowers it. That one-way rule is what sliding window needs.

Grow the right edge until sum ≥ k. Then shrink from the left while it still holds, and record the length. O(n) time, O(1) space.

The twist: if negative numbers were allowed, the one-way rule breaks. Then you need prefix sums with a monotonic deque instead.
