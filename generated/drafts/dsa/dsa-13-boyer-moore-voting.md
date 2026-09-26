SERIES:    DSA SERIES #13
TITLE:     Boyer–Moore Voting (Majority Element)
PILLAR:    DSA & Problem Solving — for juniors and mid-level devs who reach for a hash map by default
LEVEL:     INTERMEDIATE
FORMAT:    VISUAL
HEADLINE:  Opposite votes cancel. The majority survives.
LAYOUT:    FLOW
STATUS:    draft
---
Last post, Kadane reset its running sum when it turned negative.
Boyer–Moore uses the same reset trick to find a majority in O(1) memory.

What is it?
The majority element is the value that appears more than n/2 times, where n is the number of items. Boyer–Moore finds it in one pass with just a candidate and a counter.
Think of a room where people pair up. Each pair must hold two different opinions, and both leave. If one opinion has more than half the room, someone holding it is still standing at the end.

Why do we need it?
The usual fix is a hash map of counts: O(n) time, but also O(n) memory. Boyer–Moore keeps two variables. That matters when the data is huge or arrives as a stream you cannot store.

Key properties
→ O(n) time, O(1) extra space
→ One pass is enough if a majority is guaranteed
→ If it is not guaranteed, do a second pass to count the candidate
→ It finds "more than half", not the most common value

Example
function majority(a) {
  let cand = null, count = 0;
  for (const x of a) {
    if (count === 0) cand = x;
    count += x === cand ? 1 : -1;
  }
  return cand;
}
majority([2, 2, 1, 1, 1, 2, 2]); // 2

Steps
1. Count is 0? The current item becomes the candidate.
2. Same as the candidate? Count up.
3. Different? Count down. One vote cancels one vote.

The trap: majority([1, 2, 3]) returns 3. There is no majority, but the code still returns something. Always verify unless the problem promises one.

Where is it used?
• Interview classic: Majority Element (LeetCode 169)
• Its generalisation, Misra–Gries, finds frequent items in data streams, like top queries or heavy network traffic
• With two candidates, it finds every value above n/3 (LeetCode 229)

Spot it when the problem says…
→ "majority element" or "appears more than n/2 times"
→ "O(1) extra space" plus counting
→ "more than n/3 times" (same trick, two candidates)

When to use it / when not to
Use it: "more than half" and memory is tight.
Not: you need the top value with no majority, or all counts. Use a hash map.

Name check: same authors as the Boyer–Moore string search, but a different algorithm.

Takeaway: when opposite votes cancel, the majority is the one left standing.

Next: Anagrams and Group Anagrams — counting letters with a hash map.

#Algorithms #DataStructures #CodingInterviews #ProblemSolving #SoftwareEngineering
