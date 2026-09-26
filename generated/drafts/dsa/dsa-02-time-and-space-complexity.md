SERIES:    DSA SERIES #02
TITLE:     How We Measure an Algorithm: Time and Space Complexity
PILLAR:    DSA & Problem Solving — for students meeting complexity for the first time and juniors who want the idea behind it
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Count the steps, not the seconds
LAYOUT:    COMPARE
STATUS:    draft
---
Your code takes 2 seconds on your laptop. It takes 5 on a friend's.
So how fast is your code? Seconds cannot tell you. They measure the machine too.

What is it?
Count the steps instead. Then ask one question: when the input grows, how do the steps grow?
We call the input size n. For an array, n is its length.
Do the same for memory: how much extra memory does the code need as n grows?
Counting steps as n grows is called time complexity. Counting extra memory as n grows is called space complexity.
Think of a recipe: "stir once per guest". A fast cook finishes sooner. The number of stirs only changes when the guest count does.

Why do we need it?
A stopwatch changes with the laptop, the language and the data. Step counts do not. They let you compare two ideas before you write them. They also warn you which code will struggle when the data gets 1,000 times bigger.

How does it work? Two tiny examples
function sum(a) {
  let total = 0;
  for (const x of a) total += x;
  return total;
}
Time: one step per item, so n steps.
Space: one extra variable, total, whatever n is.

const copy = [...a];
Time: n steps, one per item copied.
Space: n new slots. Double the input, double the memory.

Same time, different space. That is why we measure both.

Key properties
→ We care how the count grows, not the exact number. n + 2 steps grows like n steps.
→ Space means extra memory, not the input you were given.
→ Time and space often trade: use more memory to do fewer steps.
→ The same code can take different steps on different inputs. A search may stop at item 1, or check all n.

Where is it used?
• Coding interviews: "what is the time and space of your solution?"
• Code review: a loop over every user, inside another loop over every user
• Picking a data structure: a plain list vs a lookup table

When to use it / when not to
Use it: to compare approaches and predict behaviour on big inputs.
Not: to replace real measurement on small inputs. There, run it and time it.

Common mistake: counting lines of code. A 3-line loop over n items does n steps. A 20-line block with no loop does a fixed amount.

The senior detail: function calls use memory too. A function that calls itself n levels deep keeps n calls waiting, so it uses n extra space, even with no array.

Takeaway: time is steps as n grows. Space is extra memory as n grows.

Next: Big-O in plain English — the short way to write how the steps grow.

#Algorithms #DataStructures #BigO #CodingInterviews #ProblemSolving
