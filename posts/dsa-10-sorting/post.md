> ⚠ NOT READY — resolve these, then delete this block:
> - [FACT_CHECK: [1, 10, 2].sort() gives [1, 10, 2] because the default sort compares strings → MDN Array.prototype.sort]
> - [FACT_CHECK: Timsort is used by Python, Java (objects) and V8 → Python listsort.txt, Java Arrays.sort(Object[]) docs, v8.dev blog "Getting things sorted in V8" (2018)]
> - [FACT_CHECK: a boolean comparator is wrong in JS sort (it must return negative/zero/positive) → MDN Array.prototype.sort compareFn]

---

[1, 10, 2].sort() gives you [1, 10, 2].

Not a bug. With no comparator, JavaScript compares the items as strings, and "10" comes before "2".

Every language ships a sort. Almost nobody reads what theirs actually does. Three properties decide which one you want: is it stable, is it in-place, and does it compare pairs?

What's in the images:
1. The default comparator, and the boolean one that breaks too
2. Stable, in-place, comparison-based, with an example each
3. Merge sort vs quicksort vs heapsort vs Timsort

"Which sorting algorithm?" is rarely the real interview question. The real one: does your data have structure the sort can use, do you need stability, and can you afford the extra array? Answer those three and the algorithm picks itself.

What is the worst sorting bug you have shipped?

#Algorithms #DataStructures #Sorting #CodingInterviews #ProblemSolving
