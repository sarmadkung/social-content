SERIES:    AI ENGINEERING #01
TITLE:     Agents Are Software, Not Magic
PILLAR:    AI Engineering — for developers worried they are late to AI
LEVEL:     BEGINNER
FORMAT:    VISUAL
HEADLINE:  Agents are software, not magic
LAYOUT:    STATEMENT
STATUS:    draft
---
Strip away the framing and an AI agent is a loop.

while (res.stop === 'tool_use') {
  const out = await run(res.tool)
  msgs.push(toolResult(out))
  res = await model(msgs)
}

That's it. The model asks for a tool, you run it, you hand back the result, you ask again. Everything else — planning, memory, orchestration — is structure built around that loop.

Which means the hard parts aren't AI problems. They're the problems you already know:

What happens when the tool call fails? You need retries and timeouts, same as any network call.
What happens when the loop doesn't terminate? You need a step ceiling, same as any while loop.
What happens when context fills up? You need an eviction strategy, same as any cache.
What happens when it does the wrong thing at step 14? You need traces, same as any distributed system.

Every one of those is ordinary engineering. The model is a component with unusually high variance — it isn't a different category of software.

That's the good news for engineers worried about being late to AI. The loop takes an afternoon to understand. Making it reliable takes everything you already learned building systems that don't fall over.

AI engineering is software engineering applied to systems that use models. The fundamentals didn't get replaced. They got more load.

Next: what an LLM actually does, in plain words.

#AIEngineering #LLM #AIAgents #SoftwareEngineering #SystemDesign
