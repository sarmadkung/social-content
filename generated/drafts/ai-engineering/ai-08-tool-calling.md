SERIES:    AI ENGINEERING #08
TITLE:     Tool Calling: How a Model Asks Your Code to Act
PILLAR:    AI Engineering — for developers connecting LLMs to real systems
LEVEL:     INTERMEDIATE
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  The model asks. Your code runs.
LAYOUT:    FLOW
STATUS:    draft
---
A model cannot check your order status. It has no access to your database. Tool calling is how it asks your code to check.

What is it?
Tool calling (also called function calling) lets a model request that your code run a function. You describe the tools you offer. The model replies with a tool name and arguments, as structured output (#07). Your code runs the function and sends the result back.

Think of a waiter. The waiter does not cook. They write your order on a ticket and pass it to the kitchen. The model writes the ticket. Your code is the kitchen.

Why do we need it?
A model only produces text. On its own it cannot read live data, call an API or change anything. Without tools it guesses. A guessed order status is a wrong answer said with confidence.

Key properties
• The model never runs anything. Your code does.
• Each tool has a name, a description and a schema for its arguments.
• The model picks a tool from its description. Write descriptions with care.
• Arguments can still be wrong. Validate them like any model output.
• Many APIs let the model request several tools in one reply.

Steps
1. Send the user message plus your list of tools.
2. The model replies: call getOrder with { "id": "A123" }.
3. Your code checks the arguments and permissions, then runs getOrder.
4. You send the result back to the model.
5. The model writes the answer, or asks for another tool.

Where is it used?
Support bots that look up orders, coding assistants that read files and run tests, assistants that book meetings. Every agent is built on it.

When to use it / when not to
Use it when the answer needs live data or an action.
Skip it when the prompt already holds everything the model needs.

Senior detail: treat every tool call as untrusted input. Check permissions in your code, not in the prompt. For tools that change things, like refunds or deletes, add limits or a human approval step.

Takeaway: the model decides what to ask for. Your code decides what runs.

Next: agents are software, not magic. Put tool calling in a loop and you have an agent.

#AIEngineering #LLM #ToolCalling #SoftwareEngineering
