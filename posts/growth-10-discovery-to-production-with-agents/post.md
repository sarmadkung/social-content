> ⚠ NOT READY — resolve these, then delete this block:
> - [PERSONAL: how you run this day to day: which agent, where the spec and plan files live, and the one check you never skip]

---

"Add CSV export for invoices." You paste that into a coding agent. Twenty minutes later there is a PR, and it works. Then a customer called "Acme, Inc." downloads their invoices, and every column after the comma moves one place to the right. Nobody told the agent that names can have commas.

The agent did what it was told. The problem is what it was not told.

What it is
The fix is not a better prompt. It is a workflow. The feature goes through fixed stages. The agent does most of the work in each stage. You say yes before it moves to the next one. Each stage leaves a file behind (a spec, a plan, tests, a PR), so the next stage starts from something written down.

Think of building a house. Machines do the digging. An inspector still checks the foundation before the walls go up, because a crack found later costs the whole wall.

Why do we need it?
Without stages, one prompt goes straight to code. Every wrong guess shows up at the end, in the PR or in production, where it costs the most. With stages, most wrong guesses show up in the spec or the plan, where the fix is one line.

The images show the 8 stages and who does what, what one wrong guess costs at each stage, the spec that would have stopped the Acme bug, and what helps and what breaks.

Key points
→ Every stage leaves a file. The agent remembers through the repo, not the chat.
→ You make the decisions. The agent does the work in between.
→ Most checking happens before any code exists.
→ Small tasks give small PRs, and small PRs get real reviews.

Where it fits
New features and anything that touches users or money, with any coding agent.

When to use it / when not to
→ Use it for a real feature with users or data.
→ Skip it for a typo, a one-line config change or a quick prototype.

Common mistake
Skipping the spec and plan "to save time", then reviewing a 2,000-line PR that went the wrong way. Fix: write the spec, even ten lines, and read the plan before the agent writes code.

[PERSONAL: how you run this day to day: which agent, where the spec and plan files live, and the one check you never skip]

Keep in mind
→ Spend more time on the spec than on the prompt.
→ Read the plan. It's the cheapest place to change direction.
→ One agent per branch, so they don't step on each other.
→ Ship behind a flag, so undo is a switch, not a deploy.

Takeaway
Agents made writing code cheap. Deciding what to build, and checking it's right, is still your job.

Next: how to break a problem down before you write any code.

#AIEngineering #SoftwareEngineering #DeveloperGrowth #AIAgents #ProductEngineering
