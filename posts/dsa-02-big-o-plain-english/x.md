Big-O does not tell you how fast your code runs.

It tells you how the work grows when the input grows.

Big-O in plain English 🧵
[images: 0, 1]
---
Four rules:
- it drops constants: 3n is O(n)
- it drops smaller terms: n² + n is O(n²)
- it usually means the worst case, so say which case
- it works for memory too (space complexity)
[images: 2]
---
Grow the data 1,000×:
O(1): same work
O(log n): about 2×
O(n): 1,000×
O(n²): 1,000,000×

Fine at 1,000 rows is not fine at 1,000,000.
[images: 3]
---
Read the loops. One loop over n: O(n). A loop inside a loop: O(n²).

Watch for hidden loops: includes() inside a loop scans the array every time. That is O(n²) too.
[images: 4]
---
Same Big-O can still mean different speed: an array walk beats a linked-list walk, because the CPU cache loves memory read in order.

Big-O for large inputs. A stopwatch for small ones.

Next: arrays, and why insert is O(n).

#BigO #Algorithms
