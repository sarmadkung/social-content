SERIES:    DSA SERIES #08
TITLE:     Hash Maps: The Pattern Behind Two Sum
PILLAR:    DSA & Problem Solving — for students and juniors preparing for interviews
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Hash maps turn lookup into O(1)
LAYOUT:    STATEMENT
STATUS:    draft
---
Most people learn Two Sum as a trick. It isn't. It's a trade.

The brute force is two nested loops. For every number, scan the rest of the array looking for its partner. O(n²). It works, and on a whiteboard it'll get you politely moved along.

Here's the question that cracks it: what am I actually doing in that inner loop?

You're asking "have I seen this number before?" That's a lookup. And a lookup against an array is O(n), while a lookup against a hash map is O(1) on average (post #06 showed why).

So you stop scanning and start remembering:

const seen = new Map()
for (let i = 0; i < n; i++) {
  if (seen.has(target - a[i]))
    return [seen.get(target - a[i]), i]
  seen.set(a[i], i)
}

One pass. O(n) time, O(n) space.

You traded memory for time. That's the whole idea — and it's why this is a pattern and not a trick.

The moment you recognise it: any time you catch yourself writing a nested loop whose inner job is "search for something." Two Sum, contains-duplicate, group-anagrams, subarray-sum-equals-k. Same move, different clothes.

Spot it when the problem says…
→ "find two items that add up to" or "find the partner"
→ "have we seen this before?" or "contains duplicate"
→ the input is unsorted and you must return original indexes

Interview takeaway: don't lead with the answer. Say "the inner loop is a search, so I can trade space for time with a hash map." That sentence is what they're listening for.

Next: every DSA problem has a pattern — how to spot which one before you write code.

#DataStructures #Algorithms #ProblemSolving #CodingInterviews #SoftwareEngineering
