> ⚠ NOT READY — resolve these, then delete this block:
> - [PERSONAL: one moment where knowing "it predicts, it does not look up" changed how you designed a feature]


---

An LLM does one thing, over and over: it guesses the next piece of text.

Every answer you have seen from a chat model was built that way. One small piece at a time.

Last post split training from inference. This is what happens at inference, and it explains a lot of "strange" behaviour.

What's in the images:
1. The loop: one token per step, until it stops
2. Scores become odds: logits, softmax, then a weighted pick
3. Three surprises it explains: sure but wrong, no memory, cost

The key takeaway: an LLM does not look things up. It predicts likely text, one token at a time.

So the facts it needs go in the input, and anything that must be right gets checked by code.

Next: what the model sees in one call. The system prompt, the chat history, documents and your question, all sharing one context window.

#AIEngineering #LLM #MachineLearning #SoftwareEngineering
