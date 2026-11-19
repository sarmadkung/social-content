SERIES:    AI ENGINEERING #04
TITLE:     Structured Output and Tool Calling: How a Model Talks to Your Code
PILLAR:    AI Engineering — for developers connecting LLMs to real code and systems
LEVEL:     INTERMEDIATE
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  The model asks. Your code checks and runs.
LAYOUT:    FLOW
VISUALS:   1 = Why does "reply only in JSON" break? · 2 = How do you get JSON you can trust? · 3 = How does a model ask your code to run a function? · 4 = Who checks a tool call before it runs? · 5 = Takeaway · rest = text
STATUS:    draft
---
"Reply only in JSON." Most of the time, it does. Then one day it adds a friendly sentence first, and your parser crashes.

And even perfect JSON cannot answer "Where is my order?" The model has no access to your database.

Code needs two things from a model: replies it can read, and a way for the model to ask for live data. The first is structured output. The second is tool calling, and it is built on the first.

Why does "reply only in JSON" break?
Structured output means getting the model to reply in a fixed shape, usually JSON, that your code can read. The shape is described by a schema (a written rule for which fields exist and what type each one is).

Think of a paper form with labelled boxes. A free-text letter is hard to process. A filled-in form is easy.

Your code cannot read a paragraph. It needs fields. The model writes likely text (#02), so asking nicely is not a guarantee. Without structure you get:
→ extra text before or after the JSON
→ missing fields
→ wrong types, like "12.50" as a string instead of a number
→ cut-off JSON when the answer hits a length limit

[FACT_CHECK: JSON can be cut off when the reply hits a length limit → OpenAI structured outputs / JSON mode docs (finish_reason "length")]

There are three levels of control:
• Asking in the prompt → works often, fails sometimes.
• JSON mode → many APIs promise valid JSON, but not your exact fields.
• Schema-constrained output → many APIs can force the reply to match your schema. Support varies by model and provider.
• None of these checks that the values are correct.

[FACT_CHECK: JSON mode promises valid JSON but not your exact fields → OpenAI JSON mode docs]
[FACT_CHECK: many APIs can force the reply to match a schema, support varies by model → OpenAI Structured Outputs docs and Anthropic structured outputs docs]

Takeaway: a prompt asks for a shape. Only a schema check proves you got it.

How do you get JSON you can trust?
1. Define a schema in code.
2. Send it to the model, using the API's structured output feature if it has one.
3. Parse and validate the reply against the same schema.
4. If it fails, retry once with the error message included.
5. If it still fails, fall back safely. Do not pass bad data on.

Example (TypeScript with Zod, a validation library)
const Invoice = z.object({
  total: z.number(),
  currency: z.string().length(3),
  dueDate: z.string(),
});
const result = Invoice.safeParse(JSON.parse(reply));
if (!result.success) { /* retry or fall back */ }

(JSON.parse can also throw, so wrap it in try/catch.)

Senior detail: valid is not the same as true. The schema can pass while the total is wrong. Add business checks too, like "line items add up to the total".

Where is it used? Data extraction from documents, classification, form filling, and the first step of tool calling.
Use it whenever code reads the output. Skip it when a human reads the output, like a chat reply.

Takeaway: treat model output like user input. Validate it before you trust it.

How does a model ask your code to run a function?
Tool calling (also called function calling) lets a model request that your code run a function. You describe the tools you offer. The model replies with a tool name and arguments, as structured output. Your code runs the function and sends the result back.

Think of a waiter. The waiter does not cook. They write your order on a ticket and pass it to the kitchen. The model writes the ticket. Your code is the kitchen.

Why do we need it? A model only produces text. On its own it cannot read live data, call an API or change anything. Without tools it guesses. A guessed order status is a wrong answer said with confidence.

Steps
1. Send the user message plus your list of tools.
2. The model replies: call getOrder with { "id": "A123" }.
3. Your code checks the arguments and permissions, then runs getOrder.
4. You send the result back to the model.
5. The model writes the answer, or asks for another tool.

Each tool has a name, a description and a schema for its arguments. The tool list goes into the window with everything else (#03). The model picks a tool from its description, so write descriptions with care. Many APIs also let the model request several tools in one reply.

[FACT_CHECK: many APIs let the model request several tools in one reply → OpenAI parallel function calling docs and Anthropic parallel tool use docs]

Where is it used? Support bots that look up orders, coding assistants that read files and run tests, assistants that book meetings. Every agent is built on it.
Use it when the answer needs live data or an action. Skip it when the prompt already holds everything the model needs.

Takeaway: the model writes the ticket. Your code is the kitchen.

Who checks a tool call before it runs?
Your code. Always.
• The model never runs anything. Your code does.
• Arguments can still be wrong. Validate them like any model output, with the same schema check as above.
• Permissions belong in your code, not in the prompt (#03). Run the tool with this user's rights.
• For tools that change things, like refunds or deletes, add limits or a human approval step.

[FACT_CHECK: the model never runs anything itself → Anthropic tool use docs (client tools vs provider-run server tools like web search)]

Senior detail: treat every tool call as untrusted input. "Refund order A123" from the model is a request, not an instruction. Your code decides if it is allowed.

Takeaway: the model decides what to ask for. Your code decides what runs.

Keep in mind when you give a model tools
→ Offer only the tools this task needs. Fewer tools, fewer wrong picks.
→ Send tool errors back as results, so the model can retry or explain.
→ Cap tool calls per request, so a confused model can't loop forever.
→ Log every call with its arguments. You'll need them to debug.
→ Run tools with the user's permissions, never an admin key.

Takeaway
Structured output gives your code fields it can check. Tool calling lets the model ask for actions. In both, the model proposes and your code validates.

Next: agents. Put tool calling in a loop and you have an agent, and often a plain workflow would do the job better.

#AIEngineering #LLM #ToolCalling #TypeScript #SoftwareEngineering
