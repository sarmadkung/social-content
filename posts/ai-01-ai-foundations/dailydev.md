TITLE: Your chat model never learns from you: 9 AI ideas that explain why
COVER: cover.png
---

You correct a chat model. Tomorrow, in a new chat, it makes the same mistake. It did not forget. It never learned. Nine ideas sit under every AI system and explain why.

- **AI ⊃ ML ⊃ deep learning ⊃ LLMs.** AI can be hand-written rules. ML learns the rules from examples. Deep learning does that with many-layer neural networks, straight from raw text, photos and sound.
- **A model only knows its data.** Each example has features (the input) and a label (the right answer). Wrong labels or missing cases make a quietly wrong model.
- **A model is a function with learned weights.** Input becomes numbers, each is multiplied by a weight, they are added up, and the score becomes an answer: a category, a number, or new content.
- **Training is guess, measure, adjust.** The loss says how wrong a guess was; gradient descent nudges every weight a little to lower it, over and over.
- **Memorising is not learning.** An overfit model is great on data it has seen and wrong on new data. Test on data you kept aside.
- **Training changes the weights. Inference doesn't.** A chat only seems to remember because the app resends the whole conversation on every call.

So send the model what it needs on every call: new facts go in the input, not the weights.
