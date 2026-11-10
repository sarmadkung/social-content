> ⚠ NOT READY — resolve these, then delete this block:
> - [FACT_CHECK: LLM pretraining is self-supervised next-token prediction, followed by RLHF → InstructGPT paper (Ouyang et al., 2022)]
> - [FACT_CHECK: generation stops at an end token or a length limit → Anthropic Messages API stop_reason and OpenAI finish_reason docs (also stop sequences)]
> - [PERSONAL: one moment where knowing "it predicts, it does not look up" changed how you designed a feature]
> - [FACT_CHECK: example numbers don't match softmax of logits 5.0/3.0/2.5/1.5/0.5 → T=1 gives 79.4/10.8/6.5/2.4/0.9; T=0.5 gives 97.5/1.8/0.7/0.1/0.0; T=2 gives 51.7/19.0/14.8/9.0/5.5. Recompute Top-K/Top-P tables from the corrected T=2 row.]


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

Next: tokens and context windows. What a token really is, and why the limit matters.

#AIEngineering #LLM #MachineLearning #SoftwareEngineering
