SERIES:    DEV GROWTH #03
TITLE:     New Stack, New Codebase: How to Get Productive Fast
PILLAR:    Career & Developer Growth — for junior and mid-level developers starting a new stack or joining a new team
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Build first. Follow one request.
LAYOUT:    FLOW
VISUALS:   1 = How do you learn a new technology fast? · 2 = How do you read a codebase you have never seen? · 3 = What slows most people down? · rest = text
STATUS:    draft
---
You join a new team. New framework, and a codebase you have never seen.

Most people do two slow things. They watch a long course on the framework, and a week later they open a blank file and freeze. Then they read the codebase file by file, top to bottom, and forget file three by the time they reach file thirty.

The course was not the problem. Neither was the codebase. The order was.

What it means
Getting productive fast is not reading more. It is reaching your first working thing sooner, then filling gaps as they appear. For a new tool, that means building something tiny on day one. For a new codebase, it means building a rough map: where things start, where data lives, and how one request moves through.

Think of moving to a new city. You do not memorise the whole map first. You walk to one shop, then another, and the map builds itself in your head.

Why it matters
Tools change every few years. The skill that lasts is how fast you become useful in a new one. Without a method, you stay in "tutorial mode": you can follow along, but you cannot build alone.

And on a real team, you rarely write code from scratch. You change code other people wrote. The faster you build a map, the sooner you can ship your first safe change.

How do you learn a new technology fast?
1. Find the problem it solves. Ask: what was painful before this existed?
2. Read the official "getting started" guide. It is short and up to date. Ten blog posts are not.
3. Build something tiny on day one. One page, one API route. Small enough to finish.
4. Break it on purpose. Change one thing, predict the result, then run it. A wrong guess shows you a gap.
5. Link it to what you know. "A Go channel is like a queue between two workers." New ideas stick to old ones.
6. Build a second, bigger project. Look things up only when you get stuck.
7. Read real code that uses it: the library's examples or a small open-source project.

Takeaway: build first, read second, and let your mistakes choose what you learn next.

[PERSONAL: one technology you picked up quickly at work, and the first small thing you built with it]

How do you read a codebase you have never seen?
Think of your first day in a big shopping mall. You do not visit every shop. You find the entrance, the "You are here" sign, and the one shop you need.

1. Run it first. Follow the README until the app works on your machine.
2. Find the entry points: the main file, the routes, the scripts in package.json.
3. Pick one feature, like "log in". Trace it from the button click to the database and back. Note each file you pass.
4. Read the data models. The shape of the data shows what the system cares about.
5. Read the tests. They show how the code is meant to be used.
6. Check the history. git blame shows who changed a line and in which commit. The commit message often explains why.
7. Make one tiny change, like adding a log line, and watch it run.
8. Draw a rough map: boxes for modules, arrows for calls.

Takeaway: follow one real request end to end. The map grows from there.

[PERSONAL: a codebase you joined, and the one habit that made you productive fastest]

What slows most people down?
→ Collecting courses instead of building.
→ Learning every feature before writing any code.
→ Skipping error messages. They are free lessons.
→ Trying to understand the whole codebase before changing anything.
→ Calling odd code "bad" before checking why it was written.
→ Asking an AI tool to explain it all, then never checking the answer against the code.

Takeaway: each of these delays the first working change. Get to one, then learn from it.

For seniors
Learn a tool's limits early. Read the "caveats" or "trade-offs" page and scan the open issues. Knowing when not to use a tool is the clearest sign you understand it.

In a codebase, look for the seams: the places where modules talk to each other. APIs, queues, shared database tables. Most design decisions, and most bugs, live at those boundaries.

Takeaway: build one small thing in the new tool, and follow one real request through the new code. Both maps grow from there.

Next: when you are stuck. How to debug systematically, and how to ask a question that gets a fast answer.

#DeveloperGrowth #SoftwareEngineering #LearningInPublic #CodeReading #CareerGrowth
