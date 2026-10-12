You correct a chat model. Tomorrow, in a new chat, it makes the same mistake.

It didn't forget. It never learned.

9 ideas under every AI system explain why 🧵
[images: 0, 1, 2, 3]
---
A model is a function with learned numbers inside it.

Input becomes numbers, each is multiplied by a weight, they're added up, and the score becomes an answer.

A category (spam), a number (a price), or new content (a reply).
[images: 4, 5]
---
Training is a loop: guess, measure how wrong (the loss), adjust the weights a little. Repeat over many examples.

Watch for overfitting: great on data it has seen, wrong on new data. Always test on data you kept aside.
[images: 6, 7, 8]
---
Training changes the weights. Inference uses them, frozen, on every call.

A chat only seems to remember because the app resends the whole conversation each time. New chat, no history, same mistake.
[images: 9]
---
So: send the model what it needs on every call. New facts go in the input, not the weights.

Next: what an LLM actually does at inference.

#AIEngineering #LLM
