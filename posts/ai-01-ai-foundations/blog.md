---
title: "A model is a function with weights: AI basics for developers"
description: "AI vs ML vs deep learning, what a model is, how it learns, and why training and inference are different jobs. The five ideas under every AI system."
date: 2026-10-13
series: "AI Engineering"
seriesNumber: 1
slug: ai-01-ai-foundations
tags: [ai, machine-learning, deep-learning, llm]
cover: cover.png
---

You correct a chat model. It says "thanks, noted". Tomorrow, in a new chat, it makes the same mistake. It did not forget. It never learned.

That makes sense once you know five basic ideas. Most developers have heard all of them, but rarely in one place and in order. This post puts them together before the series goes into LLMs, so every later post can build on the same picture.

## 1. AI vs ML vs deep learning

These three words get used as if they mean the same thing. They don't. Each one sits inside the one before it.

![AI contains machine learning, which contains deep learning, which contains LLMs](1.png)

- **AI** is any system that does a task we would call smart. It can be plain hand-written rules: if the email says "free money", mark it spam. No learning involved.
- **Machine learning** is when the system learns the rules from examples instead of you writing them. Show it 10,000 labelled emails and it finds what spam looks like on its own.
- **Deep learning** is machine learning with neural networks of many layers. It works directly on raw text, images and audio, where hand-picking features is hard.
- **LLMs** are deep learning models trained on text.

| | Who writes the rules | Example |
| --- | --- | --- |
| Rule-based AI | You | `if "free money" in email: spam` |
| Machine learning | Learned from examples | Spam filter trained on labelled emails |
| Deep learning | Learned, many layers, raw input | Image classifier, speech recognition |
| LLM | Learned from huge amounts of text | Chat models, code assistants |

## 2. What a model actually is

A model is a function with learned numbers inside it. Take the spam example:

1. **Input becomes numbers.** An email becomes counts, like how many links it has and how many times "free" appears.
2. **The numbers are multiplied by weights and added up.**
3. **The score becomes an answer.** Above 0.5, spam.

In code, the whole model is this:

```python
def spam_score(links, free_count, known_sender):
    return 0.9 * links + 1.4 * free_count - 2.0 * known_sender

is_spam = spam_score(links=3, free_count=2, known_sender=0) > 0.5
```

The numbers `0.9`, `1.4` and `-2.0` are the **weights**. Nobody typed them in by hand. Training found them.

![A model: input numbers, multiplied by weights, summed into a score, turned into an answer](2.png)

So a model file is two things: the shape of the maths (the **architecture**) and the **weights**. When people say a model is "open weights", they mean you can download that second part.

## 3. Neural networks and deep learning

A neural network is the same idea, repeated many times.

- **A neuron** does what the spam model did: multiply inputs by weights, add them up, then pass the result through a simple function.
- **A layer** is many neurons side by side.
- **A network** is layers stacked, each one feeding the next.

![Neurons form layers, layers stack into a network, and each layer finds more complex patterns](3.png)

**Deep** just means many layers. In an image model, early layers find edges, middle layers find shapes, and late layers find faces. Nobody writes those rules. They come out of training.

Why does everyone talk about GPUs? Because all of this is matrix multiplication. Each layer multiplies a grid of inputs by a grid of weights. A GPU does thousands of those multiplications in parallel, which a CPU can't.

Size grows fast. GPT-2, released in 2019, had 1.5 billion weights. Today's large models have far more. It is the same basic maths, done at a much bigger scale.

## 4. How a model learns

Training is a loop: guess, measure, adjust. Here it is on a tiny model with one weight, `price = w × rooms`:

1. **Guess.** `w` starts at 50. A 3-room house → 150. The real price is 300.
2. **Measure.** The error, called the **loss**, is 150.
3. **Adjust.** The loss says `w` is too low, so raise it a little.
4. **Repeat** over many examples, many times, until `w` settles at 100.

![The training loop: guess, measure the loss, adjust the weights, repeat](4.png)

A real network has billions of weights, not one. **Backpropagation** works out how much each weight contributed to the error, and **gradient descent** nudges each one in the direction that makes the loss smaller. It is the same loop, applied to every weight at once.

There are three broad ways a model learns:

| Type | Learns from | Example |
| --- | --- | --- |
| Supervised | Labelled examples | Emails marked spam / not spam |
| Unsupervised | Unlabelled data, by finding patterns | Grouping customers by behaviour |
| Reinforcement | Rewards for good actions | Game-playing agents |

### What breaks without care: overfitting

A model can memorise its training data instead of learning the pattern. It scores 99% on examples it has seen and gets new ones wrong. It looks great in testing and fails in production.

The fix is simple and not optional: **keep some data aside that the model never trains on, and measure on that.** Good results on seen data and bad results on held-out data means the model memorised. You are measuring its memory, not its skill.

## 5. Training vs inference

This is the idea that explains the chat model from the opening.

![Training changes the weights and is rare and expensive. Inference uses frozen weights on every call](5.png)

- **Training changes the weights.** For a large model it is huge and rare: many GPUs running for weeks. Most teams never do it.
- **Inference uses the weights, frozen.** You send an input, the model runs its maths, you get an output. That happens on every call, and APIs bill for it per **token** (a small piece of text, about a word or part of one), with input and output tokens priced separately.

So the chat model never learned from your correction. At inference, the weights do not change. A chat only *feels* like it remembers because the app sends the whole conversation again with every message. Start a new chat, and there is no history to send.

**Fine-tuning** is more training on an already-trained model, with your own examples. It gives you a new version of the model with new weights. Don't start there: most products only need inference with a good prompt.

## Keep in mind when you start building with models

- **The model won't learn from use.** Send what it needs on every call.
- **New facts go in the input, not the weights.** The weights are fixed after training.
- **Long chat history costs tokens on every call.** Trim or summarise it.
- **Test on data the model never saw**, or you are measuring its memory.
- **Try prompts and examples before fine-tuning.** It is cheaper and faster to change.

## Takeaway

A model is a function with learned weights. Training finds them. Inference uses them, on every call you pay for.

## Next in the series

What an LLM actually does at inference: next-token prediction, explained plainly.
