SERIES:    AI ENGINEERING #02
TITLE:     What an LLM Actually Does
PILLAR:    AI Engineering — for students and developers new to LLMs
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  An LLM predicts the next token
LAYOUT:    FLOW
STATUS:    draft
---
An LLM does one thing, over and over: it guesses the next piece of text.

Every answer you have seen from a chat model was built that way, one small piece at a time. Last post split training from inference. This is what happens at inference.

What is it?
An LLM (large language model) is a program trained on a huge amount of text. Given some text, it predicts what comes next. Each piece it predicts is called a token (a word or part of a word).

Think of the autocomplete on your phone keyboard. An LLM is that idea, trained at a much larger scale.

Why does this matter?
Once you know this, many "strange" behaviours make sense:
→ It can sound sure and still be wrong. It picks likely text, not checked facts.
→ The model itself keeps no memory between requests. Your app sends the history, or adds memory with summaries and stored notes.
→ Longer answers cost more and take longer. Each token is one more prediction.

Key properties
• Input and output are tokens.
• For each step, the model gives a probability for every possible next token.
• One token is chosen, added to the text, and the loop runs again.
• It stops at a special "end" token or a length limit.

[FACT_CHECK: generation stops at an end token or a length limit → Anthropic Messages API stop_reason and OpenAI finish_reason docs (also stop sequences)]

How it works, step by step
1. Your text is split into tokens.
2. The model scores every possible next token.
3. One token is picked from those scores.
4. That token is added to the input.
5. Repeat until it stops.

Where is it used?
Chat assistants, coding assistants, summarising tools, and agents. Same loop under all of them.

When to use it / when not to
Use it for language tasks: drafting, summarising, extracting, classifying.
Do not trust it alone for exact facts or maths. Check with code or a real data source.

[PERSONAL: one moment where knowing "it predicts, it does not look up" changed how you designed a feature]

Takeaway: an LLM does not look things up. It predicts likely text, one token at a time.

Next: tokens and context windows. What a token really is, and why the limit matters.

#AIEngineering #LLM #MachineLearning #SoftwareEngineering

[FACT_CHECK: example numbers don't match softmax of logits 5.0/3.0/2.5/1.5/0.5 → T=1 gives 79.4/10.8/6.5/2.4/0.9; T=0.5 gives 97.5/1.8/0.7/0.1/0.0; T=2 gives 51.7/19.0/14.8/9.0/5.5. Recompute Top-K/Top-P tables from the corrected T=2 row.]

# How LLMs Predict the Next Token

> A visual, beginner-friendly explanation of how an LLM goes from a question like “What is the capital of Pakistan?” to a generated answer.

---

## 1. The Question

**Prompt:**

> What is the capital of Pakistan?

### What the LLM actually sees

[TODO: Explain that the text is tokenized.]

```text
What | is | the | capital | of | Pakistan | ?
```

---

## 2. The LLM Predicts the Next Token

[TODO: Explain that an LLM generates text one token at a time.]

For example:

```text
The capital of Pakistan is ...
```

The model now needs to predict the next token.

Possible candidates might include:

| Token | Probability |
|---|---:|
| Islamabad | XX% |
| Lahore | XX% |
| Karachi | XX% |
| Peshawar | XX% |

> [TODO: Explain that these probabilities are illustrative.]

---

## 3. Where Do These Probabilities Come From?

### Logits

[TODO: Explain logits.]

Example:

| Token | Raw logit |
|---|---:|
| Islamabad | 5.0 |
| Lahore | 3.0 |
| Karachi | 2.5 |
| Peshawar | 1.5 |
| Multan | 0.5 |

### Logits → Softmax → Probabilities

```text
Raw logits
    ↓
Softmax
    ↓
Probability distribution
```

Formula:

```text
P(tokenᵢ) = exp(logitᵢ) / Σ exp(logitⱼ)
```

Example:

| Token | Probability |
|---|---:|
| Islamabad | 84.1% |
| Lahore | 11.4% |
| Karachi | 6.9% |
| Peshawar | 1.5% |
| Multan | 0.6% |

> [TODO: Explain why the model does not initially produce percentages directly.]

---

# 4. Temperature

Temperature changes the shape of the probability distribution.

```text
P(tokenᵢ) = softmax(logitᵢ / T)
```

### Low Temperature

Example:

```text
T = 0.5
```

| Token | Probability |
|---|---:|
| Islamabad | 97.1% |
| Lahore | 1.8% |
| Karachi | 1.1% |
| Peshawar | 0.05% |
| Multan | 0.01% |

**Idea:**

> Lower temperature → sharper / more concentrated distribution.

### Higher Temperature

Example:

```text
T = 2.0
```

| Token | Probability |
|---|---:|
| Islamabad | 50.3% |
| Lahore | 18.5% |
| Karachi | 14.4% |
| Peshawar | 8.7% |
| Multan | 8.1% |

**Idea:**

> Higher temperature → flatter / more random distribution.

---

# 5. Top-K

Top-K keeps only the K most probable tokens.

Example:

```text
Top-K = 3
```

Before filtering:

```text
Islamabad   50.3%   ← keep
Lahore      18.5%   ← keep
Karachi     14.4%   ← keep
Peshawar     8.7%   ← remove
Multan       8.1%   ← remove
```

The remaining probabilities are then normalized.

Total:

```text
50.3 + 18.5 + 14.4 = 83.2%
```

After renormalization:

| Token | Final probability |
|---|---:|
| Islamabad | 60.5% |
| Lahore | 22.2% |
| Karachi | 17.3% |

> [TODO: Explain why renormalization is necessary.]

---

# 6. Top-P

Top-P works differently from Top-K.

Instead of saying:

> Keep exactly 3 tokens.

Top-P says:

> Keep the smallest group of tokens whose cumulative probability reaches P.

Example:

```text
Top-P = 0.80
```

Starting from the highest probability:

```text
Islamabad   50.3%   cumulative = 50.3%
Lahore      18.5%   cumulative = 68.8%
Karachi     14.4%   cumulative = 83.2%  ← reached 80%
```

So the candidate set becomes:

```text
Islamabad
Lahore
Karachi
```

Then the probabilities are normalized again.

---

# 7. Sampling

After temperature and filtering, the model samples one token from the final distribution.

Example:

| Token | Final probability |
|---|---:|
| Islamabad | 60.5% |
| Lahore | 22.2% |
| Karachi | 17.3% |

Suppose the sampler chooses:

> **Islamabad**

The probability of selecting Islamabad from this final distribution was:

**60.5%**

Important:

> The model did not “know” that Islamabad would be selected. It sampled from a probability distribution.

---

# 8. The Complete Pipeline

```text
User prompt
    ↓
Tokenization
    ↓
Neural network / Transformer
    ↓
Logits
    ↓
Temperature
    ↓
Top-K / Top-P filtering
    ↓
Final probability distribution
    ↓
Sampling
    ↓
Selected token
    ↓
Append token to context
    ↓
Predict the next token
    ↓
Repeat
```

---

# 9. What About France?

Prompt:

> What is the capital of France?

The model might arrive at something conceptually like:

```text
"The capital of France is ..."
```

Possible candidates:

| Token | Probability |
|---|---:|
| Paris | XX% |
| Lyon | XX% |
| Marseille | XX% |
| Nice | XX% |

[TODO: Replace with an illustrative numerical example.]

The same process happens:

```text
Prompt
  ↓
Tokens
  ↓
Transformer
  ↓
Logits
  ↓
Temperature
  ↓
Top-K / Top-P
  ↓
Sampling
  ↓
Paris
```

---

# 10. One Important Distinction

There are several different things that are easy to confuse:

### Model probability

The probability produced by the model's distribution before sampling/filtering.

### Temperature-adjusted probability

The probability after temperature changes the distribution.

### Final sampling probability

The probability after temperature and any Top-K / Top-P filtering and renormalization.

### Selected token

The token that the random sampling process actually chose.

```text
Model prediction
      ↓
   logits
      ↓
 probability
      ↓
 temperature
      ↓
 filtering
      ↓
 final probability
      ↓
    sampling
      ↓
 selected token
```

---

# 11. The Key Idea

An LLM is not simply doing:

```text
Question → Answer
```

It is repeatedly doing something closer to:

```text
Context
   ↓
Predict probability distribution
   ↓
Modify distribution
   ↓
Sample next token
   ↓
Add token to context
   ↓
Repeat
```

That is how:

> **“What is the capital of Pakistan?”**

can eventually become:

> **“Islamabad.”**

---

# 12. Questions to Explore Next

- What exactly are logits?
- How does softmax convert logits into probabilities?
- Why does temperature use division?
- What is the difference between Top-K and Top-P?
- Why can an LLM sometimes choose a lower-probability token?
- How does tokenization actually work?
- Why can the same prompt produce different answers?
- How does greedy decoding differ from sampling?
- What is beam search?
- How does the Transformer produce the logits?

---

## TL;DR

```text
Prompt
  ↓
Tokenization
  ↓
Transformer
  ↓
Logits
  ↓
Softmax / probability distribution
  ↓
Temperature
  ↓
Top-K / Top-P
  ↓
Sampling
  ↓
Next token
  ↓
Repeat
```

> **An LLM generates text one token at a time by repeatedly predicting a probability distribution over possible next tokens and selecting one according to the chosen decoding strategy.**
