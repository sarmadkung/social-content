SERIES:    AI ENGINEERING #02
TITLE:     What an LLM Actually Does
PILLAR:    AI Engineering — for students and developers new to LLMs
LEVEL:     BEGINNER
HEADLINE:  An LLM predicts the next token
LAYOUT:    FLOW
STATUS:    draft
---
An LLM does one thing, over and over: it guesses the next piece of text.

Every answer you have seen from a chat model was built that way, one small piece at a time.

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
