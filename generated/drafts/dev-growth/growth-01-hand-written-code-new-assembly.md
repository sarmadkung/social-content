SERIES:    DEV GROWTH #01
TITLE:     Writing Code by Hand Now Feels Like Writing Assembly
PILLAR:    Career & Developer Growth — for developers who work with coding agents, junior to senior
LEVEL:     INTERMEDIATE
MODE:      WHY
FORMAT:    VISUAL
HEADLINE:  Writing code by hand is the new assembly
LAYOUT:    FLOW
VISUALS:   1 = How has the level we write code at moved up? · 2 = What changes in a normal day? · 3 = Where does the comparison break? · 4 = What do we still write by hand? · 5 = Which skills matter more now? · 6 = Takeaway · rest = text
STATUS:    draft
---
In 1999, one developer wrote a hit PC game almost entirely in assembly.
Today that sounds wild. Nobody builds a whole app that way any more.

[FACT_CHECK: RollerCoaster Tycoon (1999) was written mostly in x86 assembly by Chris Sawyer → interviews with Chris Sawyer / reliable game-history sources]

Typing code line by line is going the same way.
Not gone. Just no longer where most of the work happens.

How has the level we write code at moved up?
Each step in programming hid one layer of detail, so you could think about the problem instead of the machine:
→ Machine code: the raw numbers the CPU runs. Example: 8B 45 F8.
→ Assembly: short names for those numbers. Example: MOV eax, [price]. You also manage registers, the CPU's few tiny, fast storage slots.
→ High-level languages: you write total = price + tax, and a compiler turns it into machine code for you.
→ Agents: you write what the code must do and how to test it. The agent writes the code.
Takeaway: each new level hides detail. The old level never dies; it moves to where it still pays off.

[FACT_CHECK: for most code, modern compilers produce machine code as good as or better than hand-written assembly → compiler optimisation sources]

What changes in a normal day?
Take one small feature: "users can mute a chat for 8 hours".
Before: you type the database change, the API endpoint, the mute switch in the UI and the tests. Roughly 300 lines and most of a day.
Now: you write three lines:
→ A mute lasts 8 hours, then turns off by itself.
→ Muted chats send no notifications, but still show unread counts.
→ Test: a message at hour 7 is silent; a message at hour 9 notifies.
The agent writes the 300 lines. You read them, run the tests and fix what is wrong.
Takeaway: the code still exists. Your job moved from typing it to describing it and checking it.

[PERSONAL: how much of your code you type by hand now compared with a year ago, and one feature where an agent wrote most of it]

Where does the comparison break?
Here the assembly story stops working, and this part matters most.
A compiler follows fixed rules. Same input, same output, every time, and it is almost never the cause of your bug. That is why most developers never read the machine code it produces.
An agent makes a best guess. Ask twice and you can get different code. The code can look right and still break a rule.
→ Compiler: fixed rules → you trust the output.
→ Agent: a best guess → you check the output.
So reading code did not become optional. Reviewing it is now the main part of the job. Later in this series, DEV GROWTH #07 shows how to review a PR an agent wrote.
Takeaway: you can trust a compiler. You must check an agent.

What do we still write by hand?
Assembly never died. It lives where every detail matters: boot code, drivers and very hot loops. Hand-written code is heading to the same kind of places:
→ The risky core: money, security checks, and code that runs at the same time (concurrency). One wrong line costs a lot.
→ Hot paths: code that runs millions of times, where you tune every line.
→ The first example of a new pattern, so the agent has a good one to copy.
→ Learning: you type it yourself while a new idea sinks in (more in DEV GROWTH #05).
→ The bug the agent keeps looping on: when it tries the same broken fix again and again, you take over.
Takeaway: type code by hand where one wrong line costs the most.

[FACT_CHECK: assembly is still used for boot code, drivers and performance-critical loops → OS kernel / compiler documentation]

Which skills matter more now?
When compilers arrived, the valued skill moved from managing registers to designing programs. It is moving up again, from typing every line to saying what the code must do and checking it:
→ Clear specs: say exactly what you want, edge cases included.
→ Small steps: break a feature into pieces you can test one by one.
→ Tests first: they tell the agent, and you, when the work is done.
→ Reading code fast: spot what is wrong in a diff (more in DEV GROWTH #07).
→ Architecture: know where code should live, and why.
Takeaway: typing speed matters less. Judgment matters more.

What goes wrong if you ignore the shift
→ You keep typing boilerplate by hand and spend a day on what an agent drafts in minutes.
→ Or you trust the agent like a compiler and merge code you never read.
The first wastes your time. The second ships bugs.

Keep in mind when agents write most of your code
→ Read every diff: an agent is not a compiler.
→ Write the tests first: they are the spec the agent must meet.
→ Type the risky core yourself: money, auth, concurrency.
→ Understand one level below where you work, the way good C developers can still read assembly.

Takeaway
Typing code is becoming the new assembly: still real, still useful, used where it matters most.
Your job: say what the code must do, and prove that it does.

Next: junior vs mid vs senior: what actually changes.

#DeveloperGrowth #SoftwareEngineering #AIEngineering #CodingAgents #Programming
