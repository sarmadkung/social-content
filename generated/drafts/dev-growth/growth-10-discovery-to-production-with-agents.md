SERIES:    DEV GROWTH #10
TITLE:     From Discovery to Production: A Feature Workflow With Agents
PILLAR:    Career & Developer Growth — for engineers and tech leads moving real feature work onto coding agents
LEVEL:     INTERMEDIATE
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Agents do the work. You make the calls.
LAYOUT:    FLOW
VISUALS:   1 = How it works: 8 stages, 6 gates · 2 = Why the early gates matter most · 3 = Example: the spec the agent builds from · 4 = Keep in mind when you build a feature with agents + Watch out: where agent workflows break · rest = text
STATUS:    draft
---
"Add CSV export for invoices." You paste that into a coding agent. Twenty minutes later there is a PR. It works. Then a customer called "Acme, Inc." downloads their invoices, and every column after the comma shifts one place to the right. Nobody wrote down that names can contain commas.

The agent did what it was told. The problem is what it was not told.

What it is
The fix is not a better prompt. It is a workflow: the feature moves through fixed stages, the agent does most of the work inside each stage, and a person signs off at the gate between stages. Each stage leaves a file behind (a spec, a plan, tests, a PR), so the next stage starts from something written, not from memory.

Think of a building site. Machines do most of the digging and lifting. An inspector still signs off the foundation before the walls go up, because a crack found later costs the whole wall.

Why do we need it?
Without stages, one prompt goes straight to code. Every wrong guess is found at the end, in the PR or in production, where it costs the most to fix. With stages, most wrong guesses are found in a spec or a plan, where the fix is one edited line.

How it works: 8 stages, 6 gates
1. Discover. Agent: groups the support tickets, searches the codebase for what already exists. You: decide if the problem is worth solving now. Leaves: a short problem statement.
2. Spec. Agent: drafts the spec and asks you about edge cases. You: approve the goal, non-goals and acceptance criteria. Leaves: spec.md. Gate.
3. Plan. Agent: reads the code, lists the files, steps, tests and risks. You: review the plan. Leaves: plan.md with small tasks. Gate.
4. Build. Agent: one task at a time, on its own branch, tests first, a commit per step. You: check in between tasks, not on every line. Leaves: commits and tests.
5. Verify. Agent: runs tests, type checks and the app, then reviews its own diff against the spec. An AI review tool takes a pass. You: check the evidence (test output, screenshots), not the word "done". Gate.
6. Review. You: review the PR for intent, scope, tests and risk (DEV GROWTH #09). Gate.
7. Ship. Merge behind a feature flag (a switch that turns the feature on without a deploy). Roll out to 5%, then 25%, then 100% of users. You: decide each step. Gate.
8. Watch. Agent: reads error logs and metrics, drafts a fix or a rollback. You: decide. What you learn goes back into Discover. Gate.

Why the early gates matter most
The same wrong guess, "names never contain commas", costs very different amounts depending on where you catch it:
→ In the spec: add one line, "escape commas and quotes".
→ In the plan: change one step before any code exists.
→ In the PR: rework the export and its tests.
→ In production: roll back, fix the code, and tell customers their files were wrong.
So the cheapest review you will ever do is the review of a plan.

Example: the spec the agent builds from
Goal: account admins export invoices for a date range as CSV.
Non-goals: PDF export, scheduled exports.
Acceptance criteria:
→ range is 12 months or less
→ columns: number, date, customer, amount, currency, status
→ commas and quotes in any field are escaped
→ 50,000 rows download without loading them all into memory
→ non-admins get 403 Forbidden
Edge cases: an empty range, dates shown in the account's time zone.

A short spec. The agent now writes a test for each line, and the Acme bug never reaches a customer.

Key properties
→ Every stage leaves a file. The agent's memory is the repo, not the chat.
→ The person owns the decisions. The agent does the work between them.
→ Gates move earlier. Most review happens before code exists.
→ Small tasks mean small PRs, and small PRs get real reviews.

Where it fits
New features, changes that touch several files, anything with users or money on the other side. Teams use the same shape with any coding agent: the tool changes, the gates do not.

When to use it / when not to
→ Use it for a feature with real users, data or more than one moving part.
→ Skip it for a typo, a one-line config change or a throwaway prototype. Eight stages for a typo is waste.

Common mistake
Skipping the spec and the plan "to save time", then spending that time and more reviewing a 2,000-line PR that went the wrong way. Fix: write the spec, even if it is ten lines, and read the plan before the agent writes code.

[PERSONAL: how you run this day to day: which agent, where the spec and plan files live, and the one gate you never skip]

Keep in mind when you build a feature with agents
→ Spend more time on the spec than on the prompt.
→ Review the plan: it's the cheapest place to fix direction.
→ One small task per change, one reviewable PR each.
→ One agent per branch or worktree: no shared mess.
→ Ask for evidence, not "done": test output, screenshots.
→ Ship behind a flag: rollback is a switch, not a deploy.
→ Put what you learn in the repo's agent docs for next time.

Watch out: where agent workflows break
→ Vague spec → the agent fills the gaps with guesses → write non-goals and edge cases down.
→ Long sessions drift → later steps forget early decisions → keep the plan in a file and start a fresh session per task.
→ Parallel agents on the same files → conflicts and duplicate code → split work by area of the code.
→ Review becomes the bottleneck → agents produce faster than people review → limit open PRs per reviewer.

Takeaway
Agents made writing code cheap. Deciding what to build, and checking it is right, is still the job. Put your time at the gates.

Next: how to break a problem down before you write any code.

#AIEngineering #SoftwareEngineering #DeveloperGrowth #AIAgents #ProductEngineering
