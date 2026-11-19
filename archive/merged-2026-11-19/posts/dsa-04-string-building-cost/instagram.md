This loop looks O(n). It can be O(n²).

Strings can't be changed after they're made, so each += can copy the whole string so far. 1 + 2 + 3 … + n adds up to about n²/2 copies.

The images show the copying step by step, the fix (build in parts, join once), and what string operations really cost.

Strings are read-only. Build in parts, join once.

Swipe →

#datastructures #algorithms #javascript #programming #codinginterview
