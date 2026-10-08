TITLE: How to review a PR an AI agent wrote, and why you still must
COVER: cover.png
---
An agent opens a PR: 38 files, +1,600 lines, every check green. It took 12 minutes to write and takes an hour to read properly. So teams start skimming. That's where it hurts.

Review isn't about the agent being worse at code. AI reviewers catch many line-level bugs well, so use them. You still review for four reasons:

- **Ownership.** The agent isn't on call. Approving means "I accept this".
- **Context it never saw.** The table being removed next month, the partner still reading the old field. That knowledge lives in people.
- **A team that knows its own code.** Skip review for months and nobody can safely change the system.
- **Agents optimise for the goal you set.** "Make tests pass" can mean fixing the bug, or changing the test.

**The order I review in**

1. **Intent:** read the ticket first. Does the PR do that, no more, no less?
2. **Scope:** config, CI, lockfiles and drive-by refactors go in a separate PR.
3. **Tests before code:** the test diff hides the worst changes. Watch for `expect(...).toBe(108.00)` quietly becoming `107.99`.
4. **Risky paths:** auth, payments, deletes, migrations, retries.
5. **Fit:** new dependencies, duplicate helpers, new patterns.
6. **Run it yourself:** the PR summary is a claim, not proof.
7. **Can you explain it?** If not, don't approve.

Let the AI reviewer do the line checks. You check intent, scope, tests and risk.
