SERIES:    DSA SERIES #04
TITLE:     Big-O in Plain English
PILLAR:    DSA & Problem Solving — for students meeting Big-O and juniors who use it without trusting it
LEVEL:     BEGINNER
HEADLINE:  Big-O measures growth, not speed
LAYOUT:    GRID
STATUS:    draft
---
Big-O does not tell you how fast your code runs.
It tells you how the work grows when the input grows.

What is it?
Big-O describes how an algorithm's work grows as n, the input size, grows.
Think of delivering flyers. One flyer to one house: O(1). One to every house on the street: O(n). Every house visits every other house: O(n²).

Why do we need it?
A stopwatch depends on your laptop, your data and your luck. Big-O does not. It lets you compare two ideas before you write them. It also warns you which code will break when data gets 1,000 times bigger.

Key properties
→ It ignores constants. 3n steps is still O(n).
→ It ignores smaller terms. n² + n is O(n²).
→ It usually describes the worst case. Say which case you mean.
→ It works for memory too. That is space complexity.

The common ones, for n = 1,000:
• O(1): 1 step
• O(log n): about 10 steps
• O(n): 1,000 steps
• O(n log n): about 10,000 steps
• O(n²): 1,000,000 steps

Where is it used?
• Coding interviews, in every answer
• Code review: "this loop is n² on the full user list"
• Library docs, like Redis, which lists a time complexity for each command
• Database query plans: a full scan vs an index lookup

When to use it / when not to
Use it: to compare approaches and predict behaviour on large inputs.
Not: to pick between two fast options on small inputs. There, measure.

Example
for (const x of a) total += x;        // O(n)
for (const x of a)
  for (const y of a) check(x, y);    // O(n²)

Read the loops. One loop over n: O(n). A loop inside a loop: O(n²).

The senior detail: dropping constants hides real costs. Two O(n) loops can differ a lot in practice. Walking an array reads memory in order, which the CPU cache loves. Walking a linked list jumps around memory. Same Big-O, different speed.

[PERSONAL: one real case where an O(n²) loop showed up in code review or production]

Takeaway: Big-O tells you how cost grows, not how fast code runs.

Next: Arrays — why reading by index is O(1), but inserting is O(n).

#BigO #Algorithms #DataStructures #CodingInterviews #ProblemSolving
