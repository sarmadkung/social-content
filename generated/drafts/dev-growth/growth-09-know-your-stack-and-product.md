SERIES:    DEV GROWTH #09
TITLE:     Building With Agents: Why Your Stack and Product Knowledge Still Matter
PILLAR:    Career & Developer Growth — for engineers and founders building whole products with coding agents
LEVEL:     INTERMEDIATE
MODE:      WHY
FORMAT:    VISUAL
HEADLINE:  The agent drives. You still need the map.
LAYOUT:    GRID
VISUALS:   1 = Lesson 1: Know your stack well enough to review it · 2 = Lesson 2: Know the product deeply · 3 = Lesson 3: Keep the big picture yourself · rest = text
STATUS:    draft
---
The agent asks: "Should I store sessions in Redis or in Postgres?" You don't know the stack well, so you pick one. The agent builds on it for three weeks: login, logout, rate limits, "remember me". Then you find out the choice does not fit how you deploy. Now you are rewriting auth, not adding features.

The agent did nothing wrong. It asked. The answer was the problem.

The question
If agents can write most of the code, why does it still matter what stack you pick and how well you know the product?

The reason, step by step
1. Agents ask you questions all the time. Which database, which library, what happens when a payment fails, who can see this page. Each answer is a decision the agent builds on.
2. One wrong answer early moves the whole product. The agent does not push back on a bad choice. It builds on it quickly, so the cost of the mistake grows quickly too.
3. You can only answer well in a stack you understand. If you have never used a tool, you cannot tell a good suggestion from a bad one. You just accept it.
4. You can only answer product questions if you know the product. "Should admins see deleted orders?" has no technical answer. It depends on who the users are and what they need.
5. Someone has to hold the big picture. The agent works on one task at a time. It does not track what is done, what is half-done and what is left. If you don't, nobody does.

Lesson 1: Know your stack well enough to review it
What goes wrong without it: you accept every choice the agent makes, because you cannot judge any of them.
What to do: pick the stack for what the job needs, then learn enough of it to read a diff, run it and debug it before it goes into the product. A stack can be new to you. It can't be one nobody on the team can review. Try a new tool on a side project or one small, separate job first, not on the core of the product you need to ship. (How to pick for the job, not for habit: DEV GROWTH #10.)

Takeaway: you don't have to know the stack already. You have to understand it well enough to judge what the agent builds on it.

Lesson 2: Know the product deeply
What goes wrong without it: you answer the agent's questions with guesses, and each guess sends the product a little further from what users need.
What to do: before the first prompt, write a one-page product brief:
→ who it is for
→ the 3 to 5 things it must do
→ what it will not do (yet)
→ the rules that never change (for example: "a user only sees their own invoices")
Point the agent to this brief. Read it again before you answer a big question.

Takeaway: write the product brief before the first prompt. Every answer you give the agent should come from it.

Lesson 3: Keep the big picture yourself
What goes wrong without it: you only give commands. You don't know what was built, what is broken or what is left. Every session starts from scratch, and the product never reaches the end.
What to do: keep a progress.md file in the repo and update it after every session:
→ Done: what works, and how you checked it
→ In progress: what is half-built
→ Next: the next 3 tasks, in order
→ Decisions: what you chose and why (Postgres for sessions, because we already run it)
The agent reads it at the start. You read it to know where the product stands.

Takeaway: keep progress.md current. It is the one place the whole picture lives.

[PERSONAL: the real moment you learned this while building with agents: a choice you made too fast, or a point where you lost track of what was done]

What goes wrong if you ignore this
→ The product drifts. Each answer is a little off, and after a month it is not the product you planned.
→ You can't review the work. Checking an agent's output still needs you to understand the stack (how to review: DEV GROWTH #07).
→ You become a person who only gives commands. Lots of activity, but no finish line.

Keep in mind when you build a product with agents
→ Not sure of an answer? Ask the agent for trade-offs, not a pick.
→ Try a new tool in a throwaway branch before it enters the product.
→ A new library the agent adds is a stack choice too. Check it.
→ Update progress.md before you close the session, not tomorrow.
→ A request that surprises you? Check the brief before you answer.

Takeaway
Agents make building fast. Only you know where it is going.

Next: agents made code cheap to write, not cheap to run. Pick the stack for how it runs.

#DeveloperGrowth #AIEngineering #SoftwareEngineering #CodingAgents #Programming
