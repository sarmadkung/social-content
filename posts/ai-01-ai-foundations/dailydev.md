TITLE: A model is a function with weights: AI basics for developers
COVER: cover.png
---
You correct a chat model. Tomorrow, in a new chat, it makes the same mistake. It did not forget. It never learned. Five basic ideas explain why.

- **AI ⊃ ML ⊃ deep learning ⊃ LLMs.** AI can be hand-written rules. ML learns the rules from examples. Deep learning does that with many-layer neural networks. LLMs are deep learning trained on text.
- **A model is a function with learned numbers.** Input becomes numbers, they are multiplied by weights and added up, and the score becomes an answer. A model file is the architecture plus the weights.
- **Deep means many layers.** Early layers find edges, later ones find faces. Nobody writes those rules; they come out of training. It is all matrix maths, which is why it runs on GPUs.
- **Learning is guess, measure, adjust.** The loss says how wrong the guess was; backpropagation and gradient descent nudge each weight. Watch for overfitting: test on data the model never trained on.
- **Training changes weights. Inference doesn't.** Training is rare and expensive. Inference runs on every call, with frozen weights, billed per token. A chat only "remembers" because the app resends the whole conversation.

**Keep in mind:** send the model what it needs on every call, put new facts in the input, trim long history, and try prompts before fine-tuning.

Next in the series: what an LLM actually does at inference.
