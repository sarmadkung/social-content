SERIES:    DEV GROWTH #04
TITLE:     When You Are Stuck: Debug Systematically, Then Ask a Good Question
PILLAR:    Career & Developer Growth — for students and junior developers, with tools for mid-level and seniors who answer questions
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Debug in a loop. Ask in five lines.
LAYOUT:    FLOW
VISUALS:   1 = How do you debug without guessing? · 2 = How do you find the commit that broke it? · 3 = What goes into a good technical question? · rest = text
STATUS:    draft
---
The slowest way to fix a bug is to change random things until it goes away. Even when it works, you do not know why.

The second slowest is a message that says "It doesn't work, can someone help?" It waits longest for an answer. Not because people are unkind. They cannot help without more facts.

Being stuck has two good moves, in this order: debug with a method, then ask with the facts your debugging found.

What it means
Systematic debugging is a loop: see the problem, make one guess, test that guess, repeat.

A good technical question gives the helper everything they need to answer in one reply.

Think of a good doctor. They do not hand out every medicine at once. They ask questions, run one test, and narrow down the cause. And when you call a mechanic, "my car makes a noise" gets you nowhere. "A clicking noise when I turn left at low speed" gets a quick answer.

Why it matters
Guessing works on small bugs. On a real system, there are too many moving parts. A method finds the cause in steps you can explain to your team.

Clear questions save everyone's time, including yours. And writing one often solves the problem before you send it. Explaining it forces you to check your own steps.

How do you debug without guessing?
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

Takeaway: reproduce, shrink, guess one thing, prove it. Then repeat.

[PERSONAL: a bug where a wrong assumption cost you time, and what finally revealed it]

How do you find the commit that broke it?
If it worked before, stop reading code and search the history. git bisect runs a binary search over your commits. You mark one good commit and one bad one, and it halves the range each step. Around 1,000 commits take about 10 steps to reach the one that broke it.

Takeaway: if it worked before, search the history, not the code.

What goes into a good technical question?
1. Try first. Search the error, read the docs, and set a time limit so you do not stay stuck too long.
2. State the goal, not only your attempt.
3. Say what you expected and what actually happened.
4. Paste the exact error and the smallest code that shows it. Text, not a screenshot. (The smallest failing case from step 3 of debugging is exactly this.)
5. List what you already tried.
6. Add your setup: versions, operating system, anything in between.

A real example
Goal: upload a profile photo.
Expected: 200 with the image URL.
Actual: 413 Payload Too Large on files over 1 MB.
Tried: raised the upload limit in Express. Same error.
Setup: Node 20, behind Nginx.

[FACT_CHECK: HTTP 413 is named "Payload Too Large" → RFC 9110 §15.5.14 (now "Content Too Large"; Nginx's own page says "Request Entity Too Large")]

That last line is the clue. Nginx rejects request bodies over 1 MB by default (client_max_body_size), before Express ever sees them. A good question often carries its own answer.

[FACT_CHECK: Nginx rejects request bodies over 1 MB by default via client_max_body_size, before the app sees them → Nginx ngx_http_core_module docs, client_max_body_size]

Common mistakes
→ The XY problem: asking about your broken fix (Y) instead of your real goal (X).
→ "Can I ask a question?" Just ask it.
→ Leaving without sharing the answer once you find it.

[FACT_CHECK: XY problem = asking about your attempted fix (Y) instead of the real goal (X) → xyproblem.info / the original definition]

Takeaway: goal, expected, actual, tried, setup. Five lines, faster help.

[PERSONAL: a question you once asked badly, or one from a teammate that was easy to answer because it was clear]

For seniors
When you answer, ask for the goal first. Half the time, the real fix is one step before the code they showed you.

Takeaway: debug with one guess at a time. When you still need help, send the facts your debugging found, starting with the goal.

Next: why fundamentals still matter when AI writes the code, and how to use AI tools without losing your skills.

#Debugging #DeveloperGrowth #SoftwareEngineering #ProblemSolving #CareerGrowth
