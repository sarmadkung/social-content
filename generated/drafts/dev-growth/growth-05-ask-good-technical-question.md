SERIES:    DEV GROWTH #05
TITLE:     How to Ask a Good Technical Question
PILLAR:    Career & Developer Growth — for students and junior developers, and seniors who answer questions
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  A clear question gets a fast answer
LAYOUT:    ANATOMY
STATUS:    draft
---
"It doesn't work, can someone help?" is the question that waits longest for an answer. Not because people are unkind. They cannot help without more facts.

What it means
A good technical question gives the helper everything they need to answer in one reply.

Think of calling a mechanic. "My car makes a noise" gets you nowhere. "A clicking noise when I turn left at low speed" gets a quick answer.

Why it matters
Clear questions save everyone's time, including yours. And writing one often solves the problem before you send it. Explaining it forces you to check your own steps.

The steps
1. Try first. Search the error, read the docs, and set a time limit so you do not stay stuck too long.
2. State the goal, not only your attempt.
3. Say what you expected and what actually happened.
4. Paste the exact error and the smallest code that shows it. Text, not a screenshot.
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

[PERSONAL: a question you once asked badly, or one from a teammate that was easy to answer because it was clear]

For seniors
When you answer, ask for the goal first. Half the time, the real fix is one step before the code they showed you.

Takeaway
Goal, expected, actual, tried, setup. Five lines, faster help.

Next: why fundamentals still matter when AI writes the code.

#DeveloperGrowth #SoftwareEngineering #Communication #CareerGrowth #Programming
