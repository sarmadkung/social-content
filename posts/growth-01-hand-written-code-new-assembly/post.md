> ⚠ NOT READY — resolve these, then delete this block:
> - [FACT_CHECK: RollerCoaster Tycoon (1999) was written mostly in x86 assembly by Chris Sawyer → interviews with Chris Sawyer / reliable game-history sources]
> - [FACT_CHECK: compilers became good enough that hand-written assembly rarely beats them for most code → compiler history / optimisation sources]
> - [PERSONAL: how much of your code you write by hand now compared with a year ago, and one feature where an agent wrote most of it]
> - [FACT_CHECK: assembly is still used for boot code, drivers and performance-critical loops → OS kernel / compiler documentation]

---

In 1999, a hit PC game was written almost entirely in assembly, mostly by one developer. Today that sounds wild. Almost nobody writes a whole app that way any more.

[FACT_CHECK: RollerCoaster Tycoon (1999) was written mostly in x86 assembly by Chris Sawyer → interviews with Chris Sawyer / reliable game-history sources]

Writing code by hand, line by line, is starting to feel the same.

The question
If coding agents write most of the code, is hand-written code becoming what assembly became: still real, still useful, but no longer the level most of us work at?

How has the level we write code at moved up?
Every big step in programming hid one layer of detail, so people could think about the problem instead of the machine:
→ Machine code: you wrote the raw numbers the CPU runs.
→ Assembly: you wrote short names for those instructions (MOV, ADD) and managed registers yourself. Registers are the CPU's few tiny, very fast storage slots.
→ High-level languages (C, then Java, JavaScript, Python): a compiler turns readable code into machine instructions. You stopped managing registers.
→ Agents: you describe the behaviour, the rules and the tests. The agent writes the code. You stop typing most lines.
Each time, the old level did not disappear. It moved to the places where it still pays off.

[FACT_CHECK: compilers became good enough that hand-written assembly rarely beats them for most code → compiler history / optimisation sources]

What changes in a normal day?
Take one feature: "users can mute a chat for 8 hours".
Before: you write the data change, the API endpoint, the UI toggle and the tests yourself. Say 300 lines and most of a day.
Now: you write what it must do, in a few lines:
→ A mute lasts 8 hours, then turns off by itself.
→ Muted chats send no notifications, but still show unread counts.
→ Test: a message at hour 7 is silent; a message at hour 9 notifies.
The agent writes the code. You read the diff, run the tests and fix what is wrong.
The 300 lines still exist. You just did not type them.

[PERSONAL: how much of your code you write by hand now compared with a year ago, and one feature where an agent wrote most of it]

Where does the comparison break?
A compiler is deterministic: the same code gives the same output every time, and it is almost never the cause of your bug. Nobody reviews compiler output line by line.
An agent is not like that. The same request can give different code, and the code can be confidently wrong. So reading code did not become optional the way reading assembly did.
→ Compiler: fixed, proven rules → you trust the output.
→ Agent: a model's best guess → you check the output.
Review is now the main part of the job. DEV GROWTH #10 shows how to review a PR an agent wrote.

What do we still write by hand?
Assembly survived where it matters most: boot code, drivers and tight loops. Hand-written code survives in the same kind of places:
→ The risky core: money, security checks and code that runs at the same time (concurrency), where one wrong line costs a lot.
→ Hot paths: code that runs millions of times, where you tune every line.
→ The first example of a new pattern, so the agent has a good example to copy.
→ Learning: you write it yourself while you learn a new idea (DEV GROWTH #08).
→ The fix when the agent goes in circles on the same bug.

[FACT_CHECK: assembly is still used for boot code, drivers and performance-critical loops → OS kernel / compiler documentation]

Which skills matter more now?
When compilers arrived, the valued skill moved from managing registers to designing programs. Now it moves up again:
→ Saying exactly what you want: clear specs and edge cases.
→ Breaking a feature into small steps you can test.
→ Writing tests that pin the behaviour down.
→ Reading code fast and spotting what is wrong (DEV GROWTH #07).
→ Architecture: knowing where code should live, and why.
Typing speed matters less. Judgment matters more.

What goes wrong if you ignore the shift
→ You keep typing boilerplate by hand and spend hours on code an agent could draft in minutes.
→ Or you go too far: you treat agent code like compiler output and merge it unread.
The first wastes your time. The second ships bugs.

Keep in mind when agents write most of your code
→ Read every diff: an agent is not a compiler.
→ Write the tests first: they are the spec the agent must meet.
→ Hand-write the risky core: money, auth, concurrency.
→ Learn one level below where you work, as good C developers read assembly.

Takeaway
Writing code by hand is not dead. Like assembly, it is moving to the places where it matters most. Everywhere else, your job is to say what the code must do, and to check that it does.

Next: how to break a problem down before you code.

#DeveloperGrowth #SoftwareEngineering #AIEngineering #CodingAgents #Programming
