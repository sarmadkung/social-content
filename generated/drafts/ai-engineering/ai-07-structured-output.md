SERIES:    AI ENGINEERING #07
TITLE:     Structured Output: Getting JSON You Can Trust
PILLAR:    AI Engineering — for developers connecting LLMs to real code
LEVEL:     INTERMEDIATE
HEADLINE:  Never trust JSON you did not validate
LAYOUT:    FLOW
STATUS:    draft
---
"Reply only in JSON." Most of the time, it does. Then one day it adds a friendly sentence first, and your parser crashes.

What is it?
Structured output means getting the model to reply in a fixed shape, usually JSON, that your code can read. The shape is described by a schema (a written rule for which fields exist and what type each one is).

Think of a paper form with labelled boxes. A free-text letter is hard to process. A filled-in form is easy.

Why do we need it?
Your code cannot read a paragraph. It needs fields. Without structure you get missing fields, wrong types, extra text, or cut-off JSON when the answer hits a length limit.

Key properties
• Asking in the prompt → works often, fails sometimes.
• JSON mode → many APIs promise valid JSON, but not your exact fields.
• Schema-constrained output → many APIs can force the reply to match your schema. Support varies by model and provider.
• None of these checks that the values are correct.

Steps
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

Where is it used?
Data extraction from documents, classification, form filling, and the first step of tool calling.

When to use it / when not to
Use it whenever code reads the output.
Skip it when a human reads the output, like a chat reply.

Senior detail: valid is not the same as true. The schema can pass while the total is wrong. Add business checks too, like "line items add up to the total".

Takeaway: treat model output like user input. Validate it before you trust it.

Next: tool calling. How a model asks your code to run a function.

#AIEngineering #LLM #TypeScript #SoftwareEngineering
