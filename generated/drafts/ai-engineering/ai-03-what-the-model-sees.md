SERIES:    AI ENGINEERING #03
TITLE:     What the Model Sees in One Call: Prompts, System Prompts and the Context Window
PILLAR:    AI Engineering — for developers building their first chat or assistant feature
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Everything the model sees shares one window
LAYOUT:    ANATOMY
VISUALS:   1 = What does the model see in one call? · 2 = System prompt or user prompt: who sets what? · 3 = What happens when the window fills up? · 4 = Can a system prompt keep data safe? · 5 = Takeaway · rest = text
STATUS:    draft
---
A chat app sends the full history on every turn. It works fine at first. Then one long conversation hits the limit, and the request fails.

The cause is not the model. It is what the app put in front of it.

Your LLM bill is not counted in words or requests. It is counted in tokens (#02). So are your speed and your limits. And every token the model reads in one call sits in one shared space: the context window.

What does the model see in one call?
The model has no memory between calls (#02). Each call, your app sends everything again, and the model sees only that:
1. The system prompt: the rules your app sets (role, tone, format, often the list of tools).
2. The chat history: earlier user messages and earlier answers.
3. Documents: any text your app adds, like a help article or an order record.
4. The user prompt: this turn's question.
5. The answer being written: every token the model writes is part of the window too.

The context window is the most tokens a model can see at once. It includes all five parts.

[FACT_CHECK: the context window includes input and output (the answer being written) → Anthropic context windows docs and OpenAI models page]

Think of a desk. Only so many pages fit on it. The model can only work with what is on the desk right now.

Example. One support-bot call, with illustrative sizes:
→ System prompt: "You are a support bot for Acme…" say 60 tokens
→ Chat history: the last eight turns, say 1,500 tokens
→ Document: the order record for #1042, say 300 tokens
→ User prompt: "Where is my order #1042?" about 10 tokens
→ Answer: up to the max output length you set
All of it is sent and paid for on this call, and again, with the new turn added, on the next one.

Key properties
• Window size varies a lot by model.
• Input and output share the same window.
• The model sees nothing outside the window. No hidden memory.

Takeaway: the model's whole world is what you send in this one call.

System prompt or user prompt: who sets what?
Two kinds of message go into most calls. Many developers treat them the same. They are not.

A system prompt is the instruction you, the developer, set for the whole conversation. A user prompt is the request for this one turn.

Think of a new shop assistant. The system prompt is the job description from the manager. The user prompt is what a customer asks at the counter.

Why do we need both? Without a system prompt, every user message must repeat the rules. Tone, format and limits drift from turn to turn. With one, the rules live in one place, owned by your code.

const messages = [
  { role: "system", content: "You are a support bot for Acme. Answer only about orders. Reply in under 80 words." },
  { role: "user", content: "Where is my order #1042?" },
];

(Some APIs take the system prompt as its own field. The idea is the same.)

[FACT_CHECK: some APIs take the system prompt as its own field → Anthropic Messages API reference (top-level system parameter)]

Key properties
• The system prompt is written by the app, not the user.
• It stays the same across turns. User prompts change each turn.
• Models are trained to give it extra weight.
• It still costs tokens on every call, because it is sent on every call.

[FACT_CHECK: models are trained to give the system prompt extra weight → OpenAI Model Spec / "The Instruction Hierarchy" paper (Wallace et al. 2024), Anthropic system prompts docs]

Comparison
System prompt → set by you, stable, sets rules: role, tone, format, limits, tools.
User prompt → set by the user, changes, asks for something.

Takeaway: the system prompt sets the rules. The user prompt asks the question.

What happens when the window fills up?
Every part of the call competes for the same space. As it fills:
→ Cost: most APIs charge per input and output token.
→ Speed: more tokens usually means slower answers.
→ Limits: go over the window and the request fails, or old text has to be cut.
→ Quality: in very long inputs, models can miss details, often in the middle.

[FACT_CHECK: going over the window fails the request or forces old text to be cut → Anthropic and OpenAI API error docs (context length exceeded)]
[FACT_CHECK: models miss details in the middle of long inputs → Liu et al. 2023, "Lost in the Middle" (arXiv 2307.03172)]

Back to the chat app from the start. It sends the full history on every turn. After enough turns, it hits the limit. The fix: keep the latest messages, and replace older ones with a short summary.

Where is this used?
Chat apps trimming old messages. RAG systems, which fetch only the relevant text instead of whole documents (#07). Agents that summarise their own history to keep going.

When to care / when not to
Care when you send long documents, long chats, or run agents for many steps.
For short one-off prompts, it rarely matters.

Takeaway: a fuller window costs more, runs slower and can answer worse.

Can a system prompt keep data safe?
No. A system prompt is a strong hint, not a guarantee. It is not a security wall: a user can try to talk the model out of it.

Put stable rules in the system prompt: role, tone, format, limits.
Do not put secrets or access checks there. Enforce those in your code.

Anything that must never happen, like reading another user's data, needs a real check outside the model. In the support bot, your code checks that order #1042 belongs to this user before the order record ever enters the window.

Takeaway: the prompt asks the model to behave. Your code enforces what matters.

Keep in mind when you build what the model sees
→ Count the tokens of each part, not just the user's question.
→ Keep the system prompt short: you pay for it on every call.
→ Trim or summarise old turns before the limit, not after the error.
→ Check access in code before any data enters the window.
→ Set a max output length: the answer uses the window too.

Takeaway
Everything the model sees, rules, history, documents, question and answer, shares one window. Choose what goes in, and enforce the rules in code.

Next: structured output and tool calling. How to get JSON you can trust, and how a model asks your code to act.

#AIEngineering #LLM #PromptEngineering #GenerativeAI #SoftwareEngineering
