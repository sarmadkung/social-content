An agent opens a PR: 38 files, +1,600 lines, all checks green. 12 minutes to write, an hour to read properly.

So teams skim and approve. That's where it hurts.

Why we still review agent PRs, and how:
[images: 1]
---
It's not that the agent codes badly. AI reviewers catch many line-level bugs well. Use them.

You review for ownership (the agent isn't on call), for context only people have, and so your team still understands its own code.
---
The order I review in:
1. intent: read the ticket first
2. scope
3. tests before code
4. risky paths
5. fit with the codebase
6. run it yourself
7. can you explain it?
[images: 2]
---
The most overlooked check is the test diff.

- expect(total).toBe(108.00)
+ expect(total).toBe(107.99)

CI goes green. The rounding bug stays, and now a test protects it.
[images: 3]
---
The agent can write the code. Only your team can own it. Review is how you take ownership.

Next: the full workflow, from feature discovery to production, with agents.

#CodeReview #AIAgents
