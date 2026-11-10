---
title: "An LLM doesn't look things up. It predicts the next token."
description: "What an LLM actually does at inference: score every possible next token, turn the scores into odds, pick one, add it, repeat."
date: 2026-11-05
series: "AI Engineering"
seriesNumber: 2
slug: ai-02-what-an-llm-does
tags: [llm, ai, machine-learning, inference]
cover: cover.png
lab: https://optimallab.dev/next-token
---

An LLM does one thing, over and over: it guesses the next piece of text.

Every answer you have seen from a chat model was built that way, one small piece at a time. The last post split training from inference. This one is about what happens at inference, and once you see it, a lot of "strange" model behaviour starts to make sense.

## What we'll cover

![In this post: the loop, how scores become odds, and three surprises the loop explains](0.png)

1. **The loop:** one token per step, until it stops.
2. **Scores become odds:** logits, softmax, then a weighted pick.
3. **Three surprises, explained:** sure but wrong, no memory, cost.

## What an LLM is

An **LLM (large language model)** is a program trained on a huge amount of text. Given some text, it predicts what comes next. Each piece it predicts is a **token**: a word or part of a word. For example, "Pakistan?" is two tokens, "Pakistan" and "?".

Think of the autocomplete on your phone keyboard. An LLM is that idea, trained at a much larger scale.

## The loop, step by step

![The next-token loop: split into tokens, score every token, pick one, add it to the text, repeat](1.png)

1. Your text is split into tokens.
2. The model scores every possible next token.
3. One token is picked from those scores.
4. That token is added to the text, so it becomes input too.
5. Repeat until the answer is done.

Ask "What is the capital of Pakistan?" and the model writes "The", then "capital", then "of", "Pakistan", "is". At that point the text it sees ends with "The capital of Pakistan is", and it picks "Islamabad". Then ".", and the answer is complete. One token per trip around the loop.

## Where the odds come from

![Scores for five candidate tokens become probabilities through softmax, then one is picked at random by weight](2.png)

For each step, the model gives every possible next token a raw score, called a **logit**. Higher means more likely. With illustrative numbers, after "The capital of Pakistan is":

- Islamabad: 5.0
- Lahore: 3.0
- Karachi: 2.5
- Peshawar: 1.5
- Multan: 0.5

Raw scores are not percentages. A formula called **softmax** turns them into probabilities that add up to 100%. Imagine the model knows only these five tokens: softmax gives Islamabad 79.4%, Lahore 10.8%, Karachi 6.5%, Peshawar 2.4% and Multan 0.9%. A real model does the same over every token it knows.

Then comes the pick, and it is a **weighted random draw**. Run it 100 times and about 79 runs say Islamabad, about 11 say Lahore. The model never "knew" it would say Islamabad. It sampled from a probability distribution. That is also why the same prompt can give a different wording on a rerun.

Settings like temperature, top-K and top-P reshape these odds before the pick: they make the likely tokens even more likely, or cut the unlikely ones out. That is the topic of post #05.

## Why this matters

![Three surprises the loop explains: sounding sure while wrong, forgetting between calls, and long answers costing more](3.png)

- **It can sound sure and still be wrong.** It picks likely text, not checked facts. Ask for a book's page count and you get a number that sounds right, but nothing checked it.
- **It keeps no memory between requests.** The model stores nothing. Your app sends the chat history, or adds memory with summaries and stored notes.
- **Longer answers cost more and take longer.** Each token is one more prediction. A 300-token reply takes 300 trips around the loop.

## Where it's used, and where not to trust it alone

The same loop runs under chat assistants, coding assistants, summarising tools and agents.

Use it for language tasks: drafting, summarising, extracting, classifying. Do not trust it alone for exact facts or maths. Check those with code or a real data source.

## Try it on Optimal Lab

[How an LLM picks the next token](https://optimallab.dev/next-token): run one inference step yourself, see the scores turn into odds, and drag the temperature to watch them change.

## Keep in mind when you build on an LLM

- Put the facts it needs in the input, or check its answer with code.
- Send the chat history on every call. The model stores none.
- Set a max output length. Every extra token adds time and cost.
- Expect new wording on a rerun. Each token is picked from odds.

**In one line:** an LLM does not look things up. It predicts likely text, one token at a time.

## Next in the series

Tokens and context windows: what a token really is, and why the limit matters.
