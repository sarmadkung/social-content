SERIES:    AI ENGINEERING #05
TITLE:     Temperature and Why Outputs Change
PILLAR:    AI Engineering — for developers debugging inconsistent LLM output
LEVEL:     BEGINNER
MODE:      WHY
FORMAT:    VISUAL
HEADLINE:  Same prompt, different answer. Here's why.
LAYOUT:    COMPARE
STATUS:    draft
---
You send the same prompt twice and get two different answers. That is not a bug. It is a setting.

Quick recap from #02: for each step, an LLM gives a score to every possible next token. Then one token is picked.

What is temperature?
Temperature controls how that pick is made. Low temperature makes the model stick to the most likely tokens. High temperature gives less likely tokens a bigger chance.

Think of ordering food. At low temperature you always order your favourite dish. At high temperature you sometimes try something new.

Why do we need it?
Different tasks want different behaviour. Pulling a date out of an invoice needs the same answer every time. Brainstorming product names needs variety.

Key properties
• Low values → focused and repeatable.
• High values → varied, creative, and more likely to wander off.
• The allowed range and default vary by model and API.
• Temperature 0 is close to "always pick the top token". Outputs can still differ slightly between runs.
• Some models limit or ignore this setting. Check the docs.

[FACT_CHECK: allowed temperature range and default vary by API → OpenAI API reference (0–2) and Anthropic Messages API reference (0–1)]
[FACT_CHECK: temperature 0 ≈ always pick the top token, but outputs can still differ between runs → Anthropic Messages API reference (temperature) and OpenAI docs on determinism]
[FACT_CHECK: some models limit or ignore temperature → OpenAI reasoning models docs and Anthropic extended thinking docs]

Where is it used?
→ Data extraction and classification: low.
→ Code generation: usually low.
→ Writing help and brainstorming: medium to high.

When to use low / when to use high
Use low when there is one right answer and you need stable results.
Use higher when you want options and can review them.

Comparison
Temperature → reshapes the scores so rare tokens get more or less chance.
Top-p → a related setting. It keeps only the smallest set of top tokens that together reach a chosen probability, like 90%. Usually tune one of the two, not both.

[FACT_CHECK: top-p keeps the smallest set of tokens reaching a chosen probability → Holtzman et al. 2019, "The Curious Case of Neural Text Degeneration" (nucleus sampling)]
[FACT_CHECK: tune temperature or top-p, not both → OpenAI and Anthropic API reference (sampling parameters)]

Senior detail: low temperature does not make answers correct. It makes them consistent. A wrong answer at temperature 0 is wrong the same way every time. That helps with testing, not with truth.

[PERSONAL: a task where you lowered or raised temperature and what changed]

Takeaway: temperature controls variety, not accuracy.

Next: embeddings. How text becomes numbers a computer can compare.

#AIEngineering #LLM #GenerativeAI #MachineLearning
