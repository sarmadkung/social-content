A model gets something wrong. The first instinct: give it more. More documents, more history, a bigger window.

A 200k window isn't 200k useful context.
[images: 1]
---
Context engineering is deciding what the model sees at each step.

Not what it could see. What it should see.

It is closer to cache design than prompt writing: what enters, what gets evicted, what is out of date.
---
Four questions per step:
1. Relevant to this step, not the whole session?
2. Can it be summarised? 12 tool calls → 3 lines of outcome
3. Fetch on demand instead of preloading?
4. Stale? An old plan competes with the current truth.
[images: 2]
---
Budget it. System 800, tools 1,200, retrieved 3,000, history 600.

When retrieval wants 9,000 tokens, that is a design decision, not an accident.
---
Measure tokens per successful task, not tokens per window.

Next: AI memory, short-term vs long-term.

#AIEngineering #LLM
