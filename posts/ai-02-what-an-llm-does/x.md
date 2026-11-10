An LLM does one thing, over and over: it guesses the next piece of text.

Every answer from a chat model is built that way, one token at a time.

How it works, plainly:
[images: 0, 1]
---
The loop:
1. split the text into tokens
2. score every possible next token
3. pick one
4. add it to the text
5. repeat until the answer is done
---
The scores (logits) go through softmax and become odds.

"The capital of Pakistan is ___"
Islamabad 79%, Lahore 11%, Karachi 7% (illustrative)

Then a weighted random pick. Not a lookup.
[images: 2]
---
That explains a lot:
- it can sound sure and still be wrong
- it forgets you between chats; your app resends the history
- long answers cost more: each token is one more prediction
[images: 3]
---
Takeaway: an LLM predicts likely text, one token at a time. Give it the facts it needs and check what must be right.

Next: tokens and context windows.

#AIEngineering #LLM
