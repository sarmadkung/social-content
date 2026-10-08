TITLE: How to review a PR an AI agent wrote, and why you still must
COVER: cover.png
---
An agent opens a PR: 38 files, 1,600 lines, all checks green. It took 12 minutes to write and takes an hour to read properly. So people start skimming. That's where it hurts.

We don't review because the agent writes bad code. AI reviewers catch many small bugs well, so use them. You still review for four reasons:

- **You're on call.** If it breaks at 2 a.m., you fix it, not the agent.
- **You know things it doesn't.** The table being removed next month, the partner still using the old field. That lives in people's heads.
- **Your team must know its code.** Skip review for months and nobody dares change the system.
- **"Tests pass" can be faked.** The agent can fix the bug, or change the test.

**The order I review in**

1. **The ticket:** what should change? Does the PR do that, no more, no less?
2. **Size:** only what was asked. Extra changes go in another PR.
3. **The tests:** read them before the code. Watch for `toBe(108.00)` quietly becoming `107.99`.
4. **Risky code:** login, payments, deletes, data changes.
5. **Fit:** does it match how the rest of the code works?
6. **Run it:** "done" is not proof.
7. **Explain it:** if you can't, don't approve.

Let the AI reviewer do the small checks. You check that it does the right thing, safely.
