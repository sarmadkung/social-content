SERIES:    AI ENGINEERING #05
TITLE:     Prompts vs System Prompts
PILLAR:    AI Engineering — for developers building chat and assistant features
LEVEL:     BEGINNER
MODE:      COMPARE
FORMAT:    VISUAL
HEADLINE:  System prompt sets rules. Prompt asks.
LAYOUT:    COMPARE
STATUS:    draft
---
Two messages go into most LLM calls. Many developers treat them the same. They are not.

What is it?
A system prompt is the instruction you, the developer, set for the whole conversation. A user prompt is the request for this one turn.

Think of a new shop assistant. The system prompt is the job description from the manager. The user prompt is what a customer asks at the counter.

Why do we need both?
Without a system prompt, every user message must repeat the rules. Tone, format and limits drift from turn to turn. With one, the rules live in one place, owned by your code.

Key properties
• The system prompt is written by the app, not the user.
• It stays the same across turns. User prompts change each turn.
• Models are trained to give it extra weight.
• It still costs tokens on every call.
• It is not a security wall. A user can try to talk the model out of it.

Example
const messages = [
  { role: "system", content: "You are a support bot for Acme. Answer only about orders. Reply in under 80 words." },
  { role: "user", content: "Where is my order #1042?" },
];

(Some APIs take the system prompt as its own field. The idea is the same.)

Where is it used?
Customer support bots, coding assistants, and agents. The system prompt holds the role, the rules, the output format and the tool list.

When to use it / when not to
Put stable rules in the system prompt: role, tone, format, limits.
Do not put secrets or access checks there. Enforce those in your code.

Comparison
System prompt → set by you, stable, sets rules.
User prompt → set by the user, changes, asks for something.

Senior detail: a system prompt is a strong hint, not a guarantee. Anything that must never happen, like reading another user's data, needs a real check outside the model.

Takeaway: the system prompt sets the rules. The user prompt asks the question. Your code enforces what matters.

Next: temperature. Why the same prompt gives a different answer each time.

#AIEngineering #PromptEngineering #LLM #SoftwareEngineering
