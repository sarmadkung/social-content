An agent opens a PR: 38 files, 1,600 lines, all checks green. 12 minutes to write, an hour to read properly.

So people skim and approve. That's where it hurts.

Why we still review agent PRs, and how:
[images: 0, 1]
---
It's not that the agent writes bad code.

You review because you're on call for it, you know things the agent doesn't, and your team has to understand its own code.
---
The order I review in:
1. the ticket
2. size
3. the tests
4. risky code
5. fit
6. run it
7. can you explain it?
[images: 2]
---
The check most people skip: the test change.

- expect(total).toBe(108.00)
+ expect(total).toBe(107.99)

Tests pass. The bug is still there, and now a test protects it.
[images: 3]
---
The agent can write the code. Only your team can own it. Review is how you own it.

Next: the full workflow, from idea to production, with agents.

#CodeReview #AIAgents
