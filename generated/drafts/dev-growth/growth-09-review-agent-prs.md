SERIES:    DEV GROWTH #09
TITLE:     How to Review a PR an AI Agent Wrote (and Why You Still Must)
PILLAR:    Career & Developer Growth — for mid-level and senior engineers who review agent-written code, and juniors who open it
LEVEL:     INTERMEDIATE
MODE:      LIST
FORMAT:    VISUAL
HEADLINE:  The agent wrote it. You still own it.
LAYOUT:    GRID
VISUALS:   1 = Why we still review · 2 = What I check, in this order · 3 = The most overlooked check: the test diff · rest = text
STATUS:    draft
---
An agent opens a pull request. 38 files, +1,600 lines, every check green, a tidy summary that says "all tests pass". It took the agent 12 minutes. Reading it properly takes an hour.

So the tempting move is a skim and an approve. That is where teams get hurt.

Why we still review
This is not about the agent being worse at code. Agents read code fast, and AI review tools catch many line-level bugs well. Use them. The reasons to review are different:

→ Ownership. A merge puts the code under your team's name. When it breaks at 2 a.m., the agent is not on call. You are. Approving means "I accept this".
→ Context the agent never saw. It solves the ticket as written. It does not know that this table is being removed next month, that a partner still reads the old field, or that legal said not to store that data. That knowledge lives in people. Review is where it meets the code.
→ A team that understands its own code. If nobody has read a change, nobody can safely change it later. Skip review for a few months and the team no longer knows its own system.
→ Agents optimise for the goal you gave them. "Make the tests pass" can be met by fixing the bug, or by changing the test. Review checks the goal was met the honest way.

What I check, in this order
1. Intent first, diff second. Read the ticket. Write one line: what should change? Then check the PR does that. No more, no less.
2. Scope. Files outside the task are a flag: config, CI, lockfiles, a "while I was here" refactor. Ask for those in a separate PR.
3. Tests before code. Read the test diff first, and read it hardest (see below).
4. Risky paths. Auth, payments, deletes, data migrations, retries and timeouts on external calls, anything that logs user data.
5. Fit with the codebase. A new dependency? A helper written again when one already exists? A new pattern next to the one the team uses?
6. Run it yourself. Pull the branch. Click the feature or call the endpoint. The PR summary is a claim, not proof.
7. Can you explain it? If you cannot explain a line to a teammate, do not approve it. Ask the agent why, or ask for a smaller change.

The most overlooked check: the test diff
A price calculation test fails. The agent's fix:

- expect(total(cart)).toBe(108.00)
+ expect(total(cart)).toBe(107.99)

CI turns green. The rounding bug is still there, and now a test protects it. Nothing in the code diff looks wrong. Only the test diff shows it.

Look for: changed expected values, deleted asserts, .skip or .only, a mock that replaces the very thing under test, a snapshot updated with no reason given.

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
