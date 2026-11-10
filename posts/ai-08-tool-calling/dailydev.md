TITLE: Tool calling: the model asks, your code decides what runs
COVER: cover.png
---
A model cannot check your order status. It has no access to your database. On its own it only produces text, so without tools it guesses, and a guessed order status is a wrong answer said with confidence.

Tool calling (also called function calling) is how a model asks your code to run a function. You describe the tools; the model replies with a tool name and arguments, as structured output; your code runs the function and sends the result back.

**The round trip**

1. Send the user message plus your list of tools.
2. The model replies: call `getOrder` with `{ "id": "A123" }`.
3. Your code checks the arguments and permissions, then runs `getOrder`.
4. You send the result back to the model.
5. The model writes the answer, or asks for another tool.

**What to get right**

- **Each tool has a name, a description and a schema.** The model picks a tool from its description, so write it with care.
- **Arguments can still be wrong.** Validate them like any model output.
- **Treat every call as untrusted input.** Check permissions in your code, not in the prompt.
- **Guard actions that change things.** Refunds and deletes get limits or a human approval step.

Use tools when the answer needs live data or an action. Skip them when the prompt already holds everything. The model decides what to ask for; your code decides what runs.
