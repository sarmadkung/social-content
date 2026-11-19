TITLE: From idea to production with coding agents: 8 stages, 6 checks
COVER: cover.png
---
"Add CSV export for invoices." An agent builds it in 20 minutes. Then a customer called "Acme, Inc." downloads their file and every column after the comma moves right. Nobody told the agent that names can have commas.

The fix isn't a better prompt. It's a workflow: fixed stages, the agent does the work in each one, and you say yes before the next. Each stage leaves a file, so the agent remembers through the repo, not the chat.

**The stages**

- **Discover:** the agent finds the problem and the code that already exists. You decide if it's worth doing now.
- **Spec (you approve):** the goal, what's not in scope, what it must do, edge cases.
- **Plan (you approve):** files, steps, tests. The cheapest review you'll ever do.
- **Build:** one small task at a time, on its own branch, tests first.
- **Verify (you approve):** look at the proof (test output, screenshots), not the word "done".
- **Review (you approve):** an AI reviewer does a first pass. You do the final one.
- **Ship (you approve):** behind a feature flag, 5% → 25% → 100% of users.
- **Watch (you approve):** the agent reads the errors. You decide: fix or undo.

**Why the early checks matter:** the same wrong guess costs one line in the spec, one step in the plan, redoing the code in the PR, and an undo plus telling customers in production.

Agents made code cheap. Deciding what to build, and checking it's right, is still your job.
