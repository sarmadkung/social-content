A model can't check your order status. It has no access to your database.

Tool calling is how it asks your code to check.

The model asks. Your code runs.
[images: 0, 1]
---
The round trip:
1. send the message + your list of tools
2. model replies: getOrder { "id": "A123" }
3. your code checks it, then runs it
4. send the result back
5. model answers, or asks for another tool
---
Each tool has a name, a description and a schema for its arguments.

The model picks a tool from its description. Write descriptions with care.

The arguments can still be wrong. Validate them like any model output.
[images: 2]
---
Treat every tool call as untrusted input.

Check permissions in your code, not in the prompt. For refunds and deletes, add limits or a human approval step.
[images: 3]
---
The model decides what to ask for. Your code decides what runs.

Next: agents are software, not magic. Put tool calling in a loop and you have an agent.

#AIEngineering #LLM
