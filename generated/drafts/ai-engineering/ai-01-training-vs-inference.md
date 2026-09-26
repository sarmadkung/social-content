SERIES:    AI ENGINEERING #01
TITLE:     Training vs Inference: Where a Model Learns, Where You Use It
PILLAR:    AI Engineering — for students and developers starting to build with models
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Training learns once. Inference answers every time.
LAYOUT:    COMPARE
STATUS:    draft
---
You correct a chat model. It says "thanks, noted". Tomorrow, in a new chat, it makes the same mistake. It did not forget. It never learned.

What is it?
A model's life has two parts.

First it learns. It is shown many examples. Inside it are numbers called weights. Each time it gets an example wrong, the weights are nudged so the next guess is a bit better. This is called training.

Then it is used. The weights are frozen. You send an input, the model runs its maths, you get an output. This is called inference.

Think of a student. Training is years of study. Inference is the exam. During the exam, the student answers from what they already know.

A tiny example
Model: price = w × rooms. One weight, w.
Training data: 3 rooms → 300.
Start with w = 50. Guess: 150. Too low, so raise w.
Repeat until w = 100. Training is done.
Inference: 4 rooms → 400. Ask a thousand times, w stays 100.
An LLM is the same idea with billions of weights.

Why does this matter?
→ Training is huge and rare. For a large model it takes many specialised chips (GPUs) running for weeks. Most teams never do it.
→ Inference is what you run every day. You call a model through an API and pay per token (a small piece of text, about a word or part of one), for input and output.
→ So as an AI engineer, your cost and speed are inference problems.

Why the model does not learn from your chat
At inference the weights do not change. The chat feels like it remembers because the app sends the whole conversation again with each message. Start a new chat and that history is gone. (A provider may use chats to train a future version. That is a separate training run, later.)

Fine-tuning, briefly
Fine-tuning is more training on a model that is already trained, using your own examples. It changes the weights and gives you a new version of the model. It is still training: slower and costlier than just writing a better prompt.

Common mistake
Telling a model "remember this for next time" and expecting it to stick. If it must stick, your app has to store it and send it again.

When to think about training / when not to
Consider fine-tuning when you have many good examples and prompts alone cannot get the behaviour.
Do not start there. Most products only need inference.

Takeaway: training changes the weights. Inference uses them. You pay for inference on every call.

Next: what an LLM actually does at inference. Next-token prediction, plainly.

#AIEngineering #MachineLearning #LLM #SoftwareEngineering
