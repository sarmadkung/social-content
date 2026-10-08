SERIES:    AI ENGINEERING #01
TITLE:     AI Foundations: From "What Is AI" to Inference
PILLAR:    AI Engineering — for students and developers starting to build with models
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Five ideas under every AI system
LAYOUT:    GRID
VISUALS:   1 = AI vs ML vs Deep Learning · 2 = What a model actually is · 3 = Neural networks and deep learning · 4 = How a model learns · 5 = Training vs inference · rest = text
STATUS:    draft
---
You correct a chat model. It says "thanks, noted". Tomorrow, in a new chat, it makes the same mistake. It did not forget. It never learned.

That makes sense once you know five basic ideas. Most of you know them already. This post puts them in one place, in order, before this series goes into LLMs.

AI vs ML vs Deep Learning
→ AI: any system that does a task we would call smart. It can be hand-written rules: if the email says "free money", mark it spam.
→ Machine learning: the system learns the rules from examples instead of you writing them. Show it 10,000 labelled emails, it finds what spam looks like.
→ Deep learning: machine learning with neural networks of many layers. It works on raw text, images and audio. LLMs are deep learning.
Each one sits inside the one before it.

What a model actually is
A model is a function with learned numbers inside it.
→ Input becomes numbers: an email becomes counts, like how many links and how many times "free" appears.
→ The numbers are multiplied by weights and added up: score = 0.9 × links + 1.4 × "free" − 2.0 × known sender.
→ The score becomes an answer: above 0.5, spam.
A model file is two things: the shape of that maths (the architecture) and the weights. Training finds the weights.

Neural networks and deep learning
→ A neuron does what the spam model did: multiply inputs by weights, add them up, then pass the result through a simple function.
→ A layer is many neurons side by side. A network is layers stacked, each feeding the next.
→ Deep means many layers. In an image model, early layers find edges, middle layers find shapes, late layers find faces. Nobody writes those rules. They come out of training.
→ Why GPUs: all of this is matrix multiplication. A GPU does thousands of those in parallel.
→ Size: GPT-2 (2019) had 1.5 billion weights. Today's large models have far more.

[FACT_CHECK: GPT-2 largest version had 1.5B parameters → OpenAI "Language Models are Unsupervised Multitask Learners" (2019)]

How a model learns
The training loop, on a tiny model: price = w × rooms. One weight, w.
→ Guess: w starts at 50. 3 rooms → 150. The real price is 300.
→ Measure: the error (the loss) is 150.
→ Adjust: the loss says w is too low, so raise it a little. In a big network, backpropagation works out how much each weight caused the error, and gradient descent nudges each one.
→ Repeat over many examples, many times, until w = 100.
Three ways to learn: from labelled examples (supervised), from unlabelled data by finding patterns (unsupervised), from rewards for good actions (reinforcement).
What breaks without care: overfitting. The model memorises the training data. 99% right on examples it has seen, wrong on new ones. How you catch it: keep some data aside that the model never trains on, and measure on that. Good on seen data and bad on the held-out data means it memorised.

Training vs inference
→ Training changes the weights. It is huge and rare: for a large model, many GPUs running for weeks. Most teams never do it.
→ Inference uses the weights, frozen. You send an input, the model runs its maths, you get an output. You do this on every call, and pay for it per token (a small piece of text, about a word or part of one).
→ So the chat model never learned from your correction. At inference the weights do not change. A chat feels like it remembers because the app sends the whole conversation again with each message. New chat, no history.
→ Fine-tuning is more training on a trained model, with your own examples. It gives you a new version of the model. Do not start there: most products only need inference.

[FACT_CHECK: APIs bill per token, with input and output tokens priced separately → OpenAI and Anthropic pricing pages]

Keep in mind when you start building with models
→ The model won't learn from use. Send what it needs on every call.
→ New facts go in the input, not the weights. The weights are fixed.
→ Long chat history costs tokens on every call. Trim it.
→ Test on data the model never saw, or you measure its memory.
→ Try prompts and examples before fine-tuning. It is cheaper.

Takeaway: a model is a function with learned weights. Training finds them. Inference uses them, on every call you pay for.

Next: what an LLM actually does at inference. Next-token prediction, plainly.

#AIEngineering #MachineLearning #DeepLearning #LLM #SoftwareEngineering
