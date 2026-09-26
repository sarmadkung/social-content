SERIES:    DEV GROWTH #04
TITLE:     How to Debug Systematically
PILLAR:    Career & Developer Growth — for students and junior developers, with a tool for mid-level
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Debugging is a loop, not a guess
LAYOUT:    FLOW
STATUS:    draft
---
The slowest way to fix a bug is to change random things until it goes away. Even when it works, you do not know why.

What it means
Systematic debugging is a loop: see the problem, make one guess, test that guess, repeat.

Think of a good doctor. They do not hand out every medicine at once. They ask questions, run one test, and narrow down the cause.

Why it matters
Guessing works on small bugs. On a real system, there are too many moving parts. A method finds the cause in steps you can explain to your team.

The steps
1. Reproduce it. Write the exact steps that make the bug happen. If you cannot trigger it, you cannot prove it is fixed.
2. Read the whole error. The stack trace is the list of function calls that led to the crash. Find the first line that is your code.
3. Shrink the problem. Remove parts until you have the smallest case that still fails.
4. Make one guess. "I think user is null because the data has not loaded yet."
5. Test the guess with evidence: a log line or a breakpoint (a pause point in the debugger). Change one thing at a time.
6. Fix the cause, not the symptom. Then write a test that fails without your fix.

Common mistakes
→ Changing three things at once.
→ Saying "that part can't be broken" and never checking it.
→ Stopping when it works, without knowing why.

[PERSONAL: a bug where a wrong assumption cost you time, and what finally revealed it]

For mid-level and seniors
If it worked before, stop reading code and search the history. git bisect runs a binary search over your commits. You mark one good commit and one bad one, and it halves the range each step. Around 1,000 commits take about 10 steps to reach the one that broke it.

Takeaway
Reproduce, shrink, guess one thing, prove it. Then repeat.

Next: how to ask a good technical question when you are still stuck.

#Debugging #DeveloperGrowth #SoftwareEngineering #ProblemSolving #CareerGrowth
