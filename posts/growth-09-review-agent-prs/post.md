> ⚠ NOT READY — resolve these, then delete this block:
> - [PERSONAL: one agent PR you sent back, and what the review caught: a changed test, scope creep, a missed edge case]

---

An agent opens a pull request. 38 files, +1,600 lines, every check green, a tidy summary that says "all tests pass". It took the agent 12 minutes. Reading it properly takes an hour.

So the tempting move is a skim and an approve. That is where teams get hurt.

Review is not about the agent being worse at code. Why we still review, the 7 checks I run in order, and the one most people skip (the test diff): it's all in the images.

Split the work with an AI reviewer
→ AI reviewer, first pass: typos, null checks, unused code, obvious bugs, style.
→ You, second pass: intent, scope, tests, risk, fit.
Neither pass replaces the other. Together they are fast and still careful.

[PERSONAL: one agent PR you sent back, and what the review caught: a changed test, scope creep, a missed edge case]

Keep in mind when you review an agent's PR
→ Read the ticket before the diff: intent first.
→ Review the tests first: a changed assert can hide a bug.
→ Big PR? Ask for smaller ones. Size hides problems.
→ Run it yourself: "all tests pass" is a claim.
→ Let an AI reviewer do the line checks; you check intent.
→ Don't approve a line you can't explain.

Watch out: what reviewing agent PRs costs
→ Review fatigue → agents open PRs faster than you can read them → cap PR size and how many agent PRs are open per reviewer.
→ Green CI as proof → the same agent wrote the code and the tests → write or agree the acceptance tests before the agent starts.
→ Skim approvals → "it's probably fine" becomes the habit → make "I ran it" part of every approval.

Takeaway
The agent can write the code. Only your team can own it. Review is how you take ownership.

Next: the whole workflow, from feature discovery to production, with agents.

#CodeReview #AIEngineering #SoftwareEngineering #DeveloperGrowth #AIAgents
