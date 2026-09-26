SERIES:    DEV GROWTH #02
TITLE:     How to Read an Unfamiliar Codebase
PILLAR:    Career & Developer Growth — for junior and mid-level developers joining a new team
LEVEL:     BEGINNER
FORMAT:    VISUAL
HEADLINE:  Follow one request, not every file
LAYOUT:    FLOW
STATUS:    draft
---
Opening a new codebase and reading files from top to bottom feels productive. It rarely is. You forget file three by the time you reach file thirty.

What it means
Reading a codebase is not reading every line. It is building a rough map: where things start, where data lives, and how a request moves through.

Think of your first day in a big shopping mall. You do not visit every shop. You find the entrance, the "You are here" sign, and the one shop you need.

Why it matters
On a real team, you rarely write code from scratch. You change code other people wrote. The faster you build a map, the sooner you can ship your first safe change.

The steps
1. Run it first. Follow the README until the app works on your machine.
2. Find the entry points: the main file, the routes, the scripts in package.json.
3. Pick one feature, like "log in". Trace it from the button click to the database and back. Note each file you pass.
4. Read the data models. The shape of the data shows what the system cares about.
5. Read the tests. They show how the code is meant to be used.
6. Check the history. git blame shows who changed a line and in which commit. The commit message often explains why.
7. Make one tiny change, like adding a log line, and watch it run.
8. Draw a rough map: boxes for modules, arrows for calls.

Common mistakes
→ Trying to understand everything before changing anything.
→ Calling odd code "bad" before checking why it was written.
→ Asking an AI tool to explain it all, then never checking the answer against the code.

[PERSONAL: a codebase you joined, and the one habit that made you productive fastest]

For seniors
Look for the seams: the places where modules talk to each other. APIs, queues, shared database tables. Most design decisions, and most bugs, live at those boundaries.

Takeaway
Follow one real request end to end. The map grows from there.

Next: how to debug systematically instead of guessing.

#DeveloperGrowth #SoftwareEngineering #CodeReading #CareerGrowth #Programming
