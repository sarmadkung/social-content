TITLE: Big-O measures growth, not speed: the basics in plain English
COVER: cover.png
---

Big-O does not tell you how fast your code runs. It tells you how the work grows when the input grows. A stopwatch depends on your laptop, your data and your luck; Big-O doesn't, so you can compare two ideas before you write them.

- **It counts growth.** One flyer to one house is O(1). One to every house on the street is O(n). Every house sending one to every other house is O(n²).
- **It drops constants.** 3n steps is still O(n). That hides real costs: walking an array and walking a linked list are both O(n), but the array reads memory in order, which the CPU cache loves.
- **It drops smaller terms.** n² + n is O(n²). The biggest term wins as n grows.
- **It usually means the worst case.** Finding x in n items is 1 step if x is first and n steps if it is missing. Say which case you mean.
- **It works for memory too.** Summing an array needs O(1) extra space; copying it needs O(n).
- **Grow the data 1,000×** and O(n) work grows 1,000×, while O(n²) work grows 1,000,000×.

Read the loops: one loop over n is O(n), a loop inside a loop is O(n²), and `includes()` inside a loop is a nested loop in disguise.

Use Big-O to predict large inputs. For two fast options on small inputs, measure.
