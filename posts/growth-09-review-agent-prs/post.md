> ⚠ NOT READY — resolve these, then delete this block:
> - [PERSONAL: one agent PR you sent back, and what the review caught: a changed test, extra changes, a missed edge case]

---

An agent opens a pull request. 38 files, 1,600 new lines, all checks green. The summary says "all tests pass". The agent wrote it in 12 minutes. Reading it properly takes an hour.

So it's tempting to skim it and click approve. That is where teams get hurt.

We don't review because the agent writes bad code. We review because:
→ You are on call for it, not the agent.
→ You know things the agent doesn't: plans, users, rules.
→ Your team has to understand its own code.
→ "Tests pass" can mean the agent changed the test, not the code.

The images show the 7 checks I do, in order, and the one most people skip.

Red flags in a test change
→ An expected value changed to match the new output.
→ A check deleted, or a test skipped.
→ A mock that replaces the very thing being tested.

Split the work with an AI reviewer
→ AI reviewer first: typos, null checks, unused code, obvious bugs.
→ You second: does it do what the ticket asked, and is it safe?
One does not replace the other.

[PERSONAL: one agent PR you sent back, and what the review caught: a changed test, extra changes, a missed edge case]

Keep in mind when you review an agent's PR
→ Read the ticket before the code.
→ Read the tests before the code.
→ PR too big? Ask for smaller ones.
→ Run it yourself. "Done" is not proof.
→ Don't approve a line you can't explain.

Watch out
→ Too many PRs to read → set a limit of open agent PRs per reviewer.
→ The agent wrote the code and the tests → agree on the tests before it starts.
→ "It's probably fine" becomes a habit → only approve what you ran.

Takeaway
The agent can write the code. Only your team can own it. Review is how you own it.

Next: the full workflow, from idea to production, with agents.

#CodeReview #AIEngineering #SoftwareEngineering #DeveloperGrowth #AIAgents
