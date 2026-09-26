SERIES:    DSA SERIES #14
TITLE:     Anagrams and Group Anagrams (Frequency Counting)
PILLAR:    DSA & Problem Solving — for students and juniors meeting counting problems in interviews
LEVEL:     INTERMEDIATE
FORMAT:    VISUAL
HEADLINE:  Same letters, same key, same group
LAYOUT:    FLOW
STATUS:    draft
---
"listen" and "silent" use the same letters.
Trying every rearrangement to prove it is O(k!). Counting letters is O(k).

What is it?
An anagram is a word made by rearranging all the letters of another word. Frequency counting means recording how many times each item appears.
Think of two bags of Scrabble tiles. Sort each bag into piles by letter. If every pile matches, the words are anagrams.

Why do we need it?
Anagram problems are really "same items, order ignored" problems. With a count per letter, one pass is enough.

Key properties
→ Check two words (length k) with counts: O(k) time
→ Space: O(1) for a fixed 26-letter alphabet, O(k) for any character set
→ Sort both and compare: O(k log k), simpler to write
→ Group anagrams: give each word a key that all its anagrams share

Example (group anagrams)
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

The senior detail: "é" can be one character or two (e + an accent mark). Call w.normalize("NFC") first. Also lowercase and remove spaces, or "Dormitory" and "dirty room" will not match.

Where is it used?
• Word-game solvers: index a dictionary by sorted letters
• Grouping by a canonical key, like log lines by template
• Find All Anagrams in a String: post #10's sliding window plus counts

Spot it when the problem says…
→ "anagram", "permutation of", "rearrange the letters"
→ "same characters", "same counts", in any order
→ "group" items that are equal once order is ignored

When to use it / when not to
Use it: only what appears and how often matters, not the order.
Not: order matters. That is string matching.

Takeaway: turn "same items in any order" into one key. Then a hash map does the grouping.

Next: Binary Search — sorted data lets you throw away half every step.

#Algorithms #DataStructures #HashMap #CodingInterviews #ProblemSolving
