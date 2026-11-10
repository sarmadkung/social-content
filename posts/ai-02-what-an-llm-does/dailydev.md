TITLE: An LLM doesn't look things up. It predicts the next token.
COVER: cover.png
---
An LLM (large language model) does one thing, over and over: it guesses the next piece of text. Every answer from a chat model is built that way, one token (a word or part of a word) at a time.

**The loop**

1. Split the text so far into tokens.
2. Score every token the model knows. These raw scores are called logits.
3. Softmax turns the scores into probabilities that add up to 100%.
4. Pick one token from those odds, add it to the text, and repeat.

Ask "What is the capital of Pakistan?" and, by the time the text reads "The capital of Pakistan is", Islamabad might get 79% and Lahore 11% (illustrative numbers). The pick is a weighted random draw, not a lookup.

**What that explains**

- **It can sound sure and still be wrong.** It picks likely text, not checked facts.
- **It keeps no memory between calls.** Your app sends the chat history every time.
- **Longer answers cost more and take longer.** Each token is one more prediction.

Put the facts the model needs in the input, and check anything that must be exact with code or a real data source.
