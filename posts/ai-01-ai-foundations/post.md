You correct a chat model. It says "thanks, noted". Tomorrow, in a new chat, it makes the same mistake. It did not forget. It never learned.

That makes sense once you know five basic ideas. Most of you know them already. This post puts them in one place, in order, before this series goes into LLMs.

The five ideas are in the images, one per image:
1. AI vs ML vs deep learning
2. What a model actually is
3. Neural networks and deep learning
4. How a model learns
5. Training vs inference

Three details the images don't show:
→ Deep networks can be huge. GPT-2 (2019) had 1.5 billion weights. Today's large models have far more.
→ Training can go wrong in a quiet way: overfitting. The model memorises its examples. 99% right on data it has seen, wrong on new data. You catch it by keeping some data aside that it never trains on, and measuring on that.
→ Fine-tuning is more training on a trained model, with your own examples. It gives you a new version of the model. Do not start there: most products only need inference.

Keep in mind when you start building with models
→ The model won't learn from use. Send what it needs on every call.
→ New facts go in the input, not the weights. The weights are fixed.
→ Long chat history costs tokens on every call. Trim it.
→ Test on data the model never saw, or you measure its memory.
→ Try prompts and examples before fine-tuning. It is cheaper.

Takeaway: a model is a function with learned weights. Training finds them. Inference uses them, on every call you pay for.

Next: what an LLM actually does at inference. Next-token prediction, plainly.

#AIEngineering #MachineLearning #DeepLearning #LLM #SoftwareEngineering
