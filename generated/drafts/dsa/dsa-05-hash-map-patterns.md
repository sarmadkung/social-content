SERIES:    DSA SERIES #05
TITLE:     Hash Map Patterns: Find the Partner, Group by the Right Key
PILLAR:    DSA & Problem Solving — for students and juniors preparing for interviews and meeting counting problems
LEVEL:     INTERMEDIATE
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Stop searching. Remember, or pick a key.
LAYOUT:    FLOW
VISUALS:   1 = How does a hash map solve Two Sum in one pass? · 2 = How do you check two words are anagrams? · 3 = How does the right key group anagrams? · 4 = Which problems use these two patterns? · 5 = Takeaway · rest = text
STATUS:    draft
---
Most people learn Two Sum as a trick. It isn't. It's a trade.
And "listen" vs "silent" is not a string problem. It's a key problem.

Both are the same move: replace a search with a hash map lookup (#04).

Pattern 1: find the partner
The brute force for Two Sum is two nested loops. For every number, scan the rest of the array looking for its partner. O(n²). It works, and on a whiteboard it'll get you politely moved along.

Here's the question that cracks it: what am I actually doing in that inner loop?

You're asking "have I seen this number before?" That's a lookup. And a lookup against an array is O(n), while a lookup against a hash map is O(1) on average (#04 showed why).

How does a hash map solve Two Sum in one pass?
So you stop scanning and start remembering:

const seen = new Map()
for (let i = 0; i < n; i++) {
  if (seen.has(target - a[i]))
    return [seen.get(target - a[i]), i]
  seen.set(a[i], i)
}

One pass. O(n) time, O(n) space.
You traded memory for time. That's the whole idea — and it's why this is a pattern and not a trick.
Takeaway: if the inner loop searches, a hash map can remember instead.

The moment you recognise it: any time you catch yourself writing a nested loop whose inner job is "search for something." Two Sum, contains-duplicate, group-anagrams, subarray-sum-equals-k. Same move, different clothes.

Interview line: don't lead with the answer. Say "the inner loop is a search, so I can trade space for time with a hash map." That sentence is what they're listening for.

Pattern 2: group by the right key
An anagram is a word made by rearranging all the letters of another word. Trying every rearrangement to prove it is O(k!). Counting letters is O(k).
Frequency counting means recording how many times each item appears.
Think of two bags of Scrabble tiles. Sort each bag into piles by letter. If every pile matches, the words are anagrams.

Anagram problems are really "same items, order ignored" problems. With a count per letter, one pass is enough.

How do you check two words are anagrams?
→ Check two words (length k) with counts: O(k) time
→ Space: O(1) for a fixed 26-letter alphabet, O(k) for any character set
→ Sort both and compare: O(k log k), simpler to write
Takeaway: count the letters, and the order stops mattering.

How does the right key group anagrams?
Give each word a key that all its anagrams share:

const words = ["eat", "tea", "tan", "ate", "nat", "bat"];
const groups = new Map();
for (const w of words) {
  const key = [...w].sort().join("");
  if (!groups.has(key)) groups.set(key, []);
  groups.get(key).push(w);
}
// [...groups.values()] → [["eat","tea","ate"], ["tan","nat"], ["bat"]]

The key for "eat", "tea" and "ate" is "aet". Same key, same bucket.

Cost for n words of length up to k: O(n · k log k) with a sorted key. Use a letter-count key like "1#0#0#...#1" and it drops to O(n · k). Keep the "#". Without it, counts 1,12 and 11,2 both become "112".
Takeaway: choose a key that equal items share, and the map does the grouping.

The senior detail: "é" can be one character or two (e + an accent mark). Call w.normalize("NFC") first. Also lowercase and remove spaces, or "Dormitory" and "dirty room" will not match.

[FACT_CHECK: "é" can be one or two code points and normalize("NFC") unifies them → MDN String.prototype.normalize]

Which problems use these two patterns?
Find the partner:
• Two Sum: value → index
• Contains Duplicate: "seen before?"
• Subarray sum equals k: running total → count (#07)
Group by a key:
• Group Anagrams
• Word-game solvers: index a dictionary by sorted letters
• Grouping by a canonical key, like log lines by template
• Find All Anagrams in a String: the sliding window (#06) plus counts
Takeaway: one lookup or one key replaces a whole inner loop.

Spot it when the problem says…
→ "find two items that add up to" or "find the partner"
→ "have we seen this before?" or "contains duplicate"
→ the input is unsorted and you must return original indexes
→ "anagram", "permutation of", "rearrange the letters"
→ "group" items that are equal once order is ignored

When to use it / when not to
Use the partner lookup: unsorted input, and the inner loop is a search.
Use a grouping key: only what appears and how often matters, not the order.
Not: order matters. That is string matching.

Keep in mind when you use a hash map pattern
→ In Two Sum, check before you insert, or a[i] pairs with itself.
→ A sorted key is easy; a count key is faster for long words.
→ Normalise text (case, spaces, accents) before you build the key.

Takeaway
Stop searching, start remembering. Turn "same items in any order" into one key.
Either way, a hash map replaces the nested loop.

Next: two pointers and sliding window: one pass instead of a nested loop.

#Algorithms #DataStructures #HashMap #CodingInterviews #ProblemSolving
