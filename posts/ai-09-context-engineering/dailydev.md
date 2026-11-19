TITLE: Context engineering: treat the window as a budget, not a bucket
COVER: cover.png
---

When a model gets something wrong, the first instinct is to give it more: more documents, more history, a bigger window. A bigger window is not the fix.

**Context engineering** is deciding what the model sees at each step. Not what it could see, what it should see. It is closer to cache design than to prompt writing: what enters the working set, what gets evicted, what is out of date.

Long context is not free memory. It is a search the model has to do before it can do your task.

Four questions per step:

- **Relevant?** To this step, not to the whole session.
- **Summarise?** Twelve tool calls become three lines of outcome.
- **Retrieve on demand?** Needed once in twenty steps means a tool call, not a prompt section.
- **Stale?** An old plan or a replaced file competes with the current truth, and sometimes wins.

**Budget it explicitly.** Give each part of the window a number and enforce it. For example: system 800, tools 1,200, retrieved 3,000, history 600. When retrieval wants 9,000 tokens, that is a design decision, not an accident.

**Measure the right thing:** tokens per successful task, not tokens per window.
