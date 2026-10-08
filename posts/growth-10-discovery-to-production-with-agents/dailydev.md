TITLE: From discovery to production with coding agents: 8 stages, 6 gates
COVER: cover.png
---
"Add CSV export for invoices." An agent ships it in 20 minutes. Then a customer called "Acme, Inc." downloads their file and every column after the comma shifts right. Nobody wrote down that names can contain commas.

The fix isn't a better prompt. It's a workflow: fixed stages, the agent does the work inside each one, and a person signs off at the gates between them. Each stage leaves a file, so the agent's memory is the repo, not the chat.

**The stages**

- **Discover:** the agent groups tickets and finds existing code. You decide if it's worth doing now.
- **Spec (gate):** goal, non-goals, acceptance criteria, edge cases.
- **Plan (gate):** files, steps, tests, risks. This is the cheapest review you'll ever do.
- **Build:** one small task at a time, on its own branch, tests first.
- **Verify (gate):** you check evidence (test output, screenshots), not the word "done".
- **Review (gate):** you check intent, scope, tests and risk. An AI reviewer does the line checks.
- **Ship (gate):** behind a feature flag, 5% → 25% → 100%.
- **Watch (gate):** the agent reads errors and drafts a fix or rollback. You decide.

**Why the early gates matter:** the same wrong guess costs one line in the spec, one step in the plan, a rework in the PR, and a rollback plus customer apology in production.

Agents made code cheap. Deciding what to build, and checking it's right, is still the job.
