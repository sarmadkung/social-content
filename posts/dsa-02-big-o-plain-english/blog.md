---
title: "Big-O measures growth, not speed: the basics in plain English"
description: "What Big-O counts, the four rules for reading it, what happens when your data grows 1,000 times, and how to read Big-O straight from your loops."
date: 2026-10-26
series: "DSA Series"
seriesNumber: 2
slug: dsa-02-big-o-plain-english
tags: [big-o, algorithms, data-structures, complexity, coding-interviews]
cover: cover.png
---

Big-O does not tell you how fast your code runs. It tells you how the work grows when the input grows.

That one difference explains most of what confuses people about it. This article explains it in plain words, with one example per idea.

## What we'll cover

![In this post: what Big-O counts, four rules, 1,000 times more data, and reading the loops](0.png)

1. **What Big-O counts:** how the work grows with the input.
2. **Four rules of reading Big-O:** what it drops, and what it covers.
3. **1,000 times more data:** how much more work, for each common Big-O.
4. **Read the loops:** Big-O straight from the code.

## What Big-O counts

![Delivering flyers: O(1), O(n) and O(n²), on a street of 6 houses and then 12](1.png)

**Big-O** describes how an algorithm's work grows as **n**, the size of its input, grows.

Think of delivering flyers on a street of n houses:

- **O(1):** one flyer to one house. The size of the street doesn't matter.
- **O(n):** one flyer to every house. Twice the houses, twice the work.
- **O(n²):** every house sends a flyer to every other house. On a street of 6 houses that is 6 × 5 = 30 flyers. On 12 houses it is 12 × 11 = 132. Twice the houses, about four times the work.

## Why we need it

A stopwatch depends on your laptop, your data and your luck. Big-O does not. It lets you compare two ideas before you write them. It also warns you which code will break when your data gets 1,000 times bigger.

## Four rules of reading Big-O

![Four rules: drops constants, drops smaller terms, usually the worst case, works for memory too](2.png)

- **It ignores constants.** 3n steps is still O(n).
- **It ignores smaller terms.** n² + n is O(n²). At n = 1,000, n² is 1,000,000 steps and the extra n is only 1,000 more. The biggest term wins as n grows.
- **It usually describes the worst case.** Finding x in a list of n items takes 1 step if x is first, and n steps if x is last or missing. So the search is O(n). Say which case you mean.
- **It works for memory too.** That is called space complexity. Summing an array needs one extra number: O(1) space. Copying it needs n new slots: O(n) space.

Dropping constants hides real costs. Two O(n) loops can differ a lot in practice. Walking an array reads memory in order, which the CPU cache loves. Walking a linked list jumps around memory. Same Big-O, different speed.

## 1,000 times more data

![How much more work each Big-O does when n grows from 1,000 to 1,000,000](3.png)

Here are the common ones, for n = 1,000:

- **O(1):** 1 step
- **O(log n):** about 10 steps
- **O(n):** 1,000 steps
- **O(n log n):** about 10,000 steps
- **O(n²):** 1,000,000 steps

Now make the data 1,000 times bigger. O(n) work grows 1,000 times. O(n²) work grows 1,000,000 times. Code that is fine at 1,000 rows is not fine at 1,000,000.

## Read the loops

![Three loops in code: one loop is O(n), a nested loop is O(n²), and includes() inside a loop is a hidden O(n²)](4.png)

```js
for (const x of a) total += x;        // O(n)

for (const x of a)
  for (const y of a) check(x, y);    // O(n²)
```

One loop over n: O(n). A loop inside a loop: O(n²).

Some loops hide inside a function call. `includes()` scans the whole array, so calling it inside a loop is a loop inside a loop: O(n²).

## Where you will meet it

- **Coding interviews:** in every answer.
- **Code review:** "this loop is n² on the full user list".
- **Library docs:** Redis, for example, lists a time complexity for each command.
- **Database query plans:** a full scan versus an index lookup.

## When to use it, and when not to

Use Big-O to compare approaches and predict how code behaves on large inputs. Don't use it to pick between two fast options on small inputs. There, measure.

## Keep in mind when you work out Big-O

- Say what n is: users, rows or characters.
- Two inputs, two letters: O(n × m), not O(n²).
- Loops in a row add. Loops inside loops multiply.
- `includes()` inside a loop is a hidden nested loop.
- Give time and space: faster code often uses more memory.

**In one line:** Big-O tells you how cost grows, not how fast code runs.

## Next in the series

Arrays: why reading by index is O(1), but inserting is O(n).
