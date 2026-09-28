SERIES:    AI ENGINEERING #03
TITLE:     Tokens and Context Windows
PILLAR:    AI Engineering — for developers building their first LLM feature
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Tokens are the unit of everything
LAYOUT:    ANATOMY
STATUS:    draft
---
Your LLM bill is not counted in words or requests. It is counted in tokens.

So are your speed and your limits.

What is a token?
A token is a small chunk of text the model reads and writes. It can be a whole word, part of a word, a space or a symbol. "unhappy" might be two tokens: "un" and "happy".

[FACT_CHECK: "unhappy" may split into "un" + "happy" → run it through the OpenAI tokenizer page / tiktoken and Anthropic token counting]

A rough rule for English: one token is about three quarters of a word. Other languages and code often use more tokens. The exact split depends on the model's tokenizer (the tool that cuts text into tokens).

[FACT_CHECK: 1 token ≈ 3/4 of an English word → OpenAI tokenizer docs / help article on tokens]
[FACT_CHECK: other languages and code often use more tokens per word → OpenAI tokenizer docs / tiktoken comparison]

What is a context window?
The context window is the most tokens a model can see at once. It includes everything: your instructions, the chat history, any documents, and the answer being written.

[FACT_CHECK: the context window includes input and output (the answer being written) → Anthropic context windows docs and OpenAI models page]

Think of a desk. Only so many pages fit on it. The model can only work with what is on the desk right now.

Why does this matter?
→ Cost: most APIs charge per input and output token.
→ Speed: more tokens usually means slower answers.
→ Limits: go over the window and the request fails, or old text has to be cut.
→ Quality: in very long inputs, models can miss details, often in the middle.

[FACT_CHECK: going over the window fails the request or forces old text to be cut → Anthropic and OpenAI API error docs (context length exceeded)]
[FACT_CHECK: models miss details in the middle of long inputs → Liu et al. 2023, "Lost in the Middle" (arXiv 2307.03172)]

Key properties
• Window size varies a lot by model.
• Input and output share the same window.
• The model sees nothing outside the window. No hidden memory.

Where is it used?
Chat apps trimming old messages. RAG systems (they fetch only the relevant text). Agents that summarise their own history to keep going.

When to care / when not to
Care when you send long documents, long chats, or run agents for many steps.
For short one-off prompts, it rarely matters.

Example
A chat app sends the full history on every turn. After enough turns, it hits the limit. The fix: keep the latest messages, and replace older ones with a short summary.

Takeaway: the context window is the model's whole world. Anything not in it does not exist.

Next: prompts vs system prompts. Who is actually giving the model its instructions?

#AIEngineering #LLM #GenerativeAI #SoftwareEngineering
