> ⚠ NOT READY — resolve these, then delete this block:
> - [FACT_CHECK: the model never runs anything itself → Anthropic tool use docs (client tools vs provider-run server tools like web search)]
> - [FACT_CHECK: many APIs let the model request several tools in one reply → OpenAI parallel function calling docs and Anthropic parallel tool use docs]


---

A model cannot check your order status.
It has no access to your database.

Tool calling is how it asks your code to check.

The model replies with a request: a tool name and arguments. Your code decides whether to run it, runs it, and sends the result back.

Think of a waiter. The waiter writes the ticket. Your code is the kitchen.

What's in the images:
1. The round trip: request, run, result, answer
2. Anatomy of a tool: name, description, schema
3. The trust boundary: validate, check, approve

The key takeaway: the model decides what to ask for. Your code decides what runs.

Next: agents are software, not magic. Put tool calling in a loop and you have an agent.

#AIEngineering #LLM #ToolCalling #SoftwareEngineering
