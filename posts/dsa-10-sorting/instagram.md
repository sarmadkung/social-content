[1, 10, 2].sort() gives you [1, 10, 2]. JavaScript compared the items as strings.

The images show the fix (a comparator that returns a number, not true/false), the three properties that decide which sort you want (stable, in-place, comparison-based), and four classic sorts side by side.

The real question is never "which algorithm". It is: is the data partly sorted, do you need stability, and can you afford a second array?

Swipe →

#algorithms #javascript #codinginterview #programming #datastructures
