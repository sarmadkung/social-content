> ⚠ NOT READY — resolve these, then delete this block:
> - [FACT_CHECK: burying useful text in lots of loosely related context makes answers worse → Liu et al. 2023 "Lost in the Middle" and Chroma "Context Rot" report (2025)]
> - [FACT_CHECK: most APIs resend the entire context every turn → OpenAI Chat Completions / Responses API docs and Anthropic Messages API docs (stateless calls, prompt caching)]
> - [FACT_CHECK: teams shipping reliable agents send less context than expected → source needed, e.g. Anthropic "Effective context engineering for AI agents"]

---

The first instinct when a model gets something wrong: give it more.
More documents, more history, a bigger window.

A bigger window is not the fix.
Long context is not free memory. It is a search the model has to do before it can do your task.

Context engineering is deciding what the model sees at each step. Not what it could see, what it should see.

It is closer to cache design than to prompt writing: what enters the working set, what gets evicted, what is out of date.

What's in the images:
1. Budget the window: give each part a number
2. Four questions to ask before every step

The takeaway: measure tokens per successful task, not tokens per window.

What is in your agent's context right now that has not been read in ten steps?

#AIEngineering #LLM #AIAgents #ContextEngineering
