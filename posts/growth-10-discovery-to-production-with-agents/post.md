> ⚠ NOT READY — resolve these, then delete this block:
> - [PERSONAL: how you run this day to day: which agent, where the spec and plan files live, and the one gate you never skip]

---

"Add CSV export for invoices." You paste that into a coding agent. Twenty minutes later there is a PR. It works. Then a customer called "Acme, Inc." downloads their invoices, and every column after the comma shifts one place to the right. Nobody wrote down that names can contain commas.

The agent did what it was told. The problem is what it was not told.

What it is
The fix is not a better prompt. It is a workflow: the feature moves through fixed stages, the agent does most of the work inside each stage, and a person signs off at the gate between stages. Each stage leaves a file behind (a spec, a plan, tests, a PR), so the next stage starts from something written, not from memory.

Think of a building site. Machines do most of the digging and lifting. An inspector still signs off the foundation before the walls go up, because a crack found later costs the whole wall.

Why do we need it?
Without stages, one prompt goes straight to code. Every wrong guess is found at the end, in the PR or in production, where it costs the most to fix. With stages, most wrong guesses are found in a spec or a plan, where the fix is one edited line.

The 8 stages and who decides at each gate, what one wrong guess costs at each stage, the spec that would have stopped the Acme bug, and where this workflow wins and breaks: it's all in the images.

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

Takeaway
Agents made writing code cheap. Deciding what to build, and checking it is right, is still the job. Put your time at the gates.

Next: how to break a problem down before you write any code.

#AIEngineering #SoftwareEngineering #DeveloperGrowth #AIAgents #ProductEngineering
