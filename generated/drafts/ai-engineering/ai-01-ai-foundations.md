SERIES:    AI ENGINEERING #01
TITLE:     AI Foundations: From "What Is AI" to Inference
PILLAR:    AI Engineering — for students and developers starting to build with models
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Nine ideas under every AI system
LAYOUT:    GRID
VISUALS:   1 = AI vs ML vs deep learning · 2 = Data: what a model learns from · 3 = What a model actually is · 4 = What a model can give back · 5 = Neural networks: why deep means many layers · 6 = How a model learns: guess, measure, adjust · 7 = Three ways a model can learn · 8 = Memorising is not learning · 9 = Training vs inference · rest = text
STATUS:    draft
---
You correct a chat model. It says "thanks, noted". Tomorrow, in a new chat, it makes the same mistake. It did not forget. It never learned.

That makes sense once you know nine basic ideas. This post puts them in one place, in order, before this series goes into LLMs.

AI vs ML vs deep learning
Each one sits inside the one before it.
→ AI: any program that does a task we would call smart. It does not have to learn. Example: a spam filter with one hand-written rule: if an email says "free money", mark it spam.
→ Machine learning: the program learns the rules from examples instead of you writing them. Example: show it 10,000 emails marked "spam" or "not spam"; it finds what spam looks like.
→ Deep learning: machine learning with neural networks of many layers. It learns straight from raw text, photos and sound, without people first deciding what to look for. Example: a photo app that finds faces in your pictures.
→ LLMs (large language models): deep learning models trained on huge amounts of text, so they can read and write language. Example: the model behind a chat app.

Data: what a model learns from
Machine learning learns from examples. A set of examples is a dataset.
→ Features: the facts about each example that the model gets as input. For an email: number of links, whether it says "free", whether the sender is known.
→ Label: the right answer for that example, like "spam" or "not spam".
→ For the spam filter, the dataset is a table: one row per email, a column per feature, one label column.
What breaks without care: the model only knows what the data shows it. If half the labels are wrong, it learns the wrong pattern. If every training email is in English, it has no idea what Spanish spam looks like. Bad data in, bad model out, and no error message tells you.

What a model actually is
A model is a function with learned numbers inside it.
→ Input becomes numbers: the features. The email "Claim your free prize" with 2 links, from a saved contact, becomes: links = 2, "free" = 1, known sender = 1.
→ Each number is multiplied by a weight and added up: score = 0.9 × 2 + 1.4 × 1 − 2.0 × 1 = 1.2.
→ The score becomes an answer. The threshold (the cut-off) is 0.5. 1.2 is above it, so: spam.
Weight: a number that says how much one signal matters. A big number means it matters a lot; a minus number pushes away from spam.
A model is two parts: the architecture (the steps: which numbers get multiplied and added, in what order) and the weights (the numbers used in those steps). Training finds the weights. Nobody types them in.
Parameters: all the learned numbers in a model. Almost all of them are weights, so people use the two words loosely. A "7B model" has about 7 billion parameters.

What a model can give back
The same idea (numbers in, maths, answer out) gives three kinds of answer.
→ A category (classification): pick one from a fixed list. Example: the spam filter answers "spam" or "not spam".
→ A number (regression): any value on a scale. Example: a house-price model looks at a house and answers 300 (thousand dollars).
→ New content (generative AI): new text, images or audio that did not exist before. Example: a chat app writes an email reply for you. LLMs are generative. How they write, one small piece at a time, is the next post.

Neural networks: why deep means many layers
→ Neuron: the spam model's maths in one small unit. Multiply inputs by weights, add them up, then a small fixed rule (an activation function) shapes the result.
→ Layer: many neurons side by side. A network is layers stacked, each one feeding the next.
→ Deep means many layers. In an image model, early layers tend to find edges, middle layers shapes, late layers whole faces. Nobody writes those rules. They come out of training.
→ Why GPUs: all of this is multiply and add, billions of times for one answer from a big model. A GPU does thousands of those at once.

How a model learns: guess, measure, adjust
A tiny model: price = w × rooms. One weight, w. A 3-room house really costs 300.
→ Guess: w starts at 50. 50 × 3 = 150.
→ Measure: 300 − 150 = 150. That gap is the loss: one number for how wrong the guess was. Real models use a formula for it, but the idea is the same.
→ Adjust: the guess was too low, so raise w a little.
→ Repeat over many examples, many times: w goes 50 → 70 → 85 → 95 → 100. Now 100 × 3 = 300.
Four words for the four parts of that loop:
→ Prediction: the model's guess (150).
→ Loss: how wrong it was (150).
→ Gradient: which way, and how strongly, each weight pushes the loss. Here: raising w lowers the loss.
→ Update: the small change to the weight. The learning rate sets how big "a little" is. Too big and w jumps past 100; too small and training takes forever.
Gradient descent is this loop: compute the gradient, update every weight a little against it, repeat.
Backpropagation is how a big network computes the gradient for millions of weights at once, working back from the loss through every layer.

Three ways a model can learn
→ Supervised: learns from examples that come with the right answer. Example: 10,000 emails, each marked "spam" or "not spam". The spam filter and house-price model above learn this way.
→ Unsupervised: learns from data with no answers. It finds groups and patterns by itself. Example: a shop's model sorts customers into groups that buy similar things, without being told what the groups are.
→ Reinforcement: learns from rewards. It tries actions and does more of what gets rewarded. Example: a game player that gets points for winning and slowly learns which moves win.

Memorising is not learning
What breaks without care: overfitting. The model memorises its training examples instead of learning the real pattern.
→ Memorised: like a student who memorised last year's exam answers. 99% right on questions it has seen. Fails on new ones.
→ Learned: like a student who understood the topic. Good on both.
→ The opposite problem, underfitting: the model is too simple or trained too little, so it is bad on both. Like a student who did not study.
→ How to catch it: keep some data aside that the model never trains on (held-out data, often called the test set), and test on that. Good on training data but bad on held-out data means it memorised.

Training vs inference
→ Training changes the weights. It is the guess-measure-adjust loop. For a large model it is huge and rare: many GPUs running for weeks. Model labs do it; most teams never do.
→ Inference uses the weights, frozen. Inference means prediction: you give the trained model a new input it has never seen, it runs its maths, you get an answer. It learns nothing new.
   House price, w = 100: a 4-room house → 100 × 4 → 400. w stays 100.
   Spam filter, same weights as before: a new email with 0 links, no "free", from a known sender → 0.9 × 0 + 1.4 × 0 − 2.0 × 1 = −2.0. Below 0.5, so: not spam.
→ Inference happens on every call. With a hosted model API you pay for it per token (a small piece of text, about a word or part of one). A big model runs billions of weights for each answer, so every call costs real compute.
→ So the chat model never learned from your correction. A chat feels like it remembers because the app sends the whole conversation again with each message. New chat, no history, same mistake. Some apps also save notes about you and add them to the input, but that is still input. The weights never change.
→ Fine-tuning is more training on a trained model, with your own examples. It gives you a new version of the model. Do not start there: most products only need inference with good prompts.

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
