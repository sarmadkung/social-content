SERIES:    AI ENGINEERING #14
TITLE:     Context engineering: the window is a budget, not a bucket
PILLAR:    AI Engineering — for engineers building agents and RAG systems who keep adding context and getting worse answers
LEVEL:     ADVANCED
HEADLINE:  A 200k window isn't 200k useful context
LAYOUT:    STAT
STATUS:    draft
VARIANT:   B (budget bar)
---
The first instinct when a model gets something wrong is to give it more. More documents, more history, a bigger window. It usually gets worse.

What is it?
Context engineering is deciding what the model sees at each step. Not what it could see — what it should see.

It is closer to cache design than to prompt writing. You are choosing what enters a working set, what gets evicted, and what gets invalidated.

Why do we need it?
Because long context is not free memory. It is a retrieval problem the model has to solve before it can solve yours. Bury three useful sentences in forty thousand tokens of loosely related material and you have made the task harder, not easier.

There is also a cost you feel on the invoice: most APIs resend the entire context every single turn.

The four questions per step
→ What is actually relevant to this step, not to the whole session?
→ What can be summarised instead of carried? Twelve tool calls become three lines of outcome.
→ What should be retrieved on demand rather than preloaded? Needed once in twenty steps means it is a tool call, not a prompt section.
→ What is stale? An old plan or a superseded file does not sit there quietly — it competes with the current truth, and sometimes wins.

Budget it explicitly
Give each part of the window a number and enforce it. System 800, tools 1,200, retrieved 3,000, history 600. When retrieval wants 9,000 tokens, that is a design decision, not an accident.

What to measure
Tokens per successful task, not tokens per window. The teams shipping reliable agents are almost always sending less than you would expect.

What is in your agent's context right now that has not been read in ten steps?
