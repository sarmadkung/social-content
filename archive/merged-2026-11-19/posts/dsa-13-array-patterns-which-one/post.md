Four array patterns. All walk the array in O(n). All replace a nested loop.

That is exactly why people mix them up.

Pick the wrong one and "subarray sum equals k" gets a sliding window. Add one negative number to the array, and the answer is quietly wrong.

What's in the images:
1. What each pattern remembers as it walks
2. The clue words that point to each one
3. One array, four questions, four patterns
4. Why Kadane is prefix sum in disguise

Before you write the loop, ask what you must remember as you walk: two ends, a range, every total, or the best run so far. The answer names the pattern.

Next: Boyer–Moore Voting, finding the majority with O(1) memory.

#Algorithms #DataStructures #CodingInterviews #ProblemSolving #PatternRecognition
