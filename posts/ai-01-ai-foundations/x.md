You correct a chat model. Tomorrow, in a new chat, it makes the same mistake.

It didn't forget. It never learned.

5 ideas under every AI system explain why 🧵
[images: 1, 2]
---
A model is a function with learned numbers inside it.

Input → numbers → multiply by weights, add up → answer.

A model file is two things: the shape of the maths (architecture) and the weights.
---
Deep learning = many layers of that.

Early layers find edges, later ones find faces. Nobody writes those rules. They come out of training.

It's all matrix maths, which is why it runs on GPUs.
[images: 3]
---
Training is a loop: guess, measure how wrong (the loss), adjust the weights a little. Repeat millions of times.

Watch for overfitting: great on data it has seen, wrong on new data. Always test on held-out data.
[images: 4]
---
Training changes the weights. Inference uses them, frozen, on every call you pay for.

Chat only "remembers" because the app resends the whole conversation.
[images: 5]
---
So: send the model what it needs on every call. New facts go in the input, not the weights.

Next: what an LLM actually does at inference.

#AIEngineering #LLM
