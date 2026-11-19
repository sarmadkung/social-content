SERIES:    AI ENGINEERING #02
TITLE:     What an LLM Actually Does
PILLAR:    AI Engineering — for students and developers new to LLMs
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  An LLM predicts the next token
LAYOUT:    FLOW
VISUALS:   1 = How does the loop work, step by step? · 2 = How do scores become odds? · 3 = How does temperature change the odds? · 4 = What do top-k and top-p cut? · 5 = Why does this matter? · 6 = Takeaway · rest = text
STATUS:    draft
---
An LLM does one thing, over and over: it guesses the next piece of text.

Every answer you have seen from a chat model was built that way, one small piece at a time. And it explains why the same prompt can give two different answers: that is not a bug, it is a setting.

Last post split training from inference. This is what happens at inference.

What is it?
An LLM (large language model) is a program trained on a huge amount of text. Given some text, it predicts what comes next.

Think of the autocomplete on your phone keyboard. An LLM is that idea, trained at a much larger scale.

How is it trained? In two steps. First it learns to predict the next word from huge amounts of text; the text holds its own answers, so nobody has to label it. Then it is tuned to give helpful answers: on example answers, and with rewards from human ratings (reinforcement learning, from post #01).

What is a token?
The pieces an LLM reads and writes are called tokens. A token is a small chunk of text: a whole word, part of a word, a space or a symbol. "unhappy" might be two tokens: "un" and "happy".

[FACT_CHECK: "unhappy" may split into "un" + "happy" → run it through the OpenAI tokenizer page / tiktoken and Anthropic token counting]

A rough rule for English: one token is about three quarters of a word. Other languages and code often use more tokens. The exact split depends on the model's tokenizer (the tool that cuts text into tokens).

[FACT_CHECK: 1 token ≈ 3/4 of an English word → OpenAI tokenizer docs / help article on tokens]
[FACT_CHECK: other languages and code often use more tokens per word → OpenAI tokenizer docs / tiktoken comparison]

Tokens are also what you pay for, and what fills the model's limit. That is the next post.

How does the loop work, step by step?
1. Your text is split into tokens.
2. The model scores every possible next token.
3. One token is picked from those scores.
4. That token is added to the input.
5. Repeat until it stops: at a special "end" token or a length limit.

Example. Ask "What is the capital of Pakistan?" The model sees tokens, something like:
What | is | the | capital | of | Pakistan | ?
(An illustrative split. A real tokenizer may cut it differently.)

It writes "The", then "capital", then "of", "Pakistan", "is". Now the text ends with "The capital of Pakistan is", and the model must predict the next token. One token per trip around the loop.

Takeaway: an answer is many small guesses, one token at a time.

How do scores become odds?
For each step, the model gives every possible next token a raw score, called a logit. Higher means more likely. Illustrative numbers, after "The capital of Pakistan is", imagining the model knows only five tokens:
→ Islamabad: 5.0
→ Lahore: 3.0
→ Karachi: 2.5
→ Peshawar: 1.5
→ Multan: 0.5

Raw scores are not percentages. They can be any number, and they do not add up to 100. A formula called softmax turns them into probabilities that do:
P(tokenᵢ) = exp(logitᵢ) / Σ exp(logitⱼ)

→ Islamabad: 79.4%
→ Lahore: 10.8%
→ Karachi: 6.5%
→ Peshawar: 2.4%
→ Multan: 0.9%

A real model does the same over every token it knows.

Then comes the pick, and it is a weighted random draw (called sampling). Run it 100 times and about 79 runs say Islamabad, about 11 say Lahore. The model never "knew" it would say Islamabad. It sampled from a probability distribution.

Takeaway: the model does not choose an answer. It draws one from odds.

How does temperature change the odds?
Temperature is a setting that changes the shape of those odds before the draw. It divides every score by T, then runs softmax:
P(tokenᵢ) = softmax(logitᵢ / T)

Low temperature makes the model stick to the most likely tokens. High temperature gives less likely tokens a bigger chance. Same five scores:

T = 0.5 (sharper):
Islamabad 97.5% · Lahore 1.8% · Karachi 0.7% · Peshawar 0.09% · Multan 0.01%

T = 1 (the model's own odds):
Islamabad 79.4% · Lahore 10.8% · Karachi 6.5% · Peshawar 2.4% · Multan 0.9%

T = 2 (flatter):
Islamabad 51.7% · Lahore 19.0% · Karachi 14.8% · Peshawar 9.0% · Multan 5.5%

At T = 2, roughly one draw in five says Lahore.

Think of ordering food. At low temperature you always order your favourite dish. At high temperature you sometimes try something new.

Why have it? Different tasks want different behaviour. Pulling a date out of an invoice needs the same answer every time. Brainstorming product names needs variety.
→ Data extraction and classification: low.
→ Code generation: usually low.
→ Writing help and brainstorming: medium to high.
Use low when there is one right answer and you need stable results. Use higher when you want options and can review them.

Key properties
• Low values → focused and repeatable.
• High values → varied, creative, and more likely to wander off.
• The allowed range and default vary by model and API.
• Temperature 0 is close to "always pick the top token". Outputs can still differ slightly between runs.
• Some models limit or ignore this setting. Check the docs.

[FACT_CHECK: allowed temperature range and default vary by API → OpenAI API reference (0–2) and Anthropic Messages API reference (0–1)]
[FACT_CHECK: temperature 0 ≈ always pick the top token, but outputs can still differ between runs → Anthropic Messages API reference (temperature) and OpenAI docs on determinism]
[FACT_CHECK: some models limit or ignore temperature → OpenAI reasoning models docs and Anthropic extended thinking docs]

Senior detail: low temperature does not make answers correct. It makes them consistent. A wrong answer at temperature 0 is wrong the same way every time. That helps with testing, not with truth.

[PERSONAL: a task where you lowered or raised temperature and what changed]

Takeaway: temperature controls variety, not accuracy.

What do top-k and top-p cut?
Temperature reshapes the odds. Top-k and top-p cut the unlikely tail off before the draw. Both start here from the T = 2 odds.

Top-k keeps only the K most likely tokens. With top-k = 3:
Islamabad 51.7% ← keep
Lahore 19.0% ← keep
Karachi 14.8% ← keep
Peshawar 9.0% ← remove
Multan 5.5% ← remove

The kept odds add up to 51.7 + 19.0 + 14.8 = 85.5%. They must add up to 100% again before the draw, so each is divided by the total (renormalised):
Islamabad 60.4% · Lahore 22.2% · Karachi 17.3%

Top-p keeps the smallest group of top tokens whose odds together reach P. With top-p = 0.80, count from the top:
Islamabad 51.7% → total 51.7%
Lahore 19.0% → total 70.7%
Karachi 14.8% → total 85.5%, past 80%: stop
Here it keeps the same three tokens, then renormalises the same way. On another prompt, where one token holds 95%, top-p keeps just that one. Top-k would still keep three.

[FACT_CHECK: top-p keeps the smallest set of tokens reaching a chosen probability → Holtzman et al. 2019, "The Curious Case of Neural Text Degeneration" (nucleus sampling)]

Usually tune temperature or top-p, not both.

[FACT_CHECK: tune temperature or top-p, not both → OpenAI and Anthropic API reference (sampling parameters)]

Then the draw. Say it picks Islamabad: from these final odds, it had a 60.4% chance. Four numbers are easy to mix up:
→ Model probability: the odds straight from softmax (79.4%).
→ After temperature: the reshaped odds (51.7% at T = 2).
→ Final probability: after top-k or top-p and renormalising (60.4%).
→ Selected token: what the random draw actually chose (Islamabad).
"Islamabad" is added to the text, and the loop runs again for the next token.

Takeaway: temperature reshapes the odds; top-k and top-p remove the long tail.

Where is it used?
Chat assistants, coding assistants, summarising tools, and agents. Same loop under all of them.

When to use it / when not to
Use it for language tasks: drafting, summarising, extracting, classifying.
Do not trust it alone for exact facts or maths. Check with code or a real data source.

Why does this matter?
Once you know this, many "strange" behaviours make sense:
→ It can sound sure and still be wrong. It picks likely text, not checked facts.
→ The model itself keeps no memory between requests. Your app sends the history, or adds memory with summaries and stored notes.
→ Longer answers cost more and take longer. Each token is one more prediction.
→ The same prompt can give new wording on a rerun. Each token is a draw from odds.

[PERSONAL: one moment where knowing "it predicts, it does not look up" changed how you designed a feature]

Takeaway: the loop explains the surprises: confident errors, no memory, cost per token.

Keep in mind when you build on an LLM
→ Put the facts it needs in the input, or check its answer with code.
→ Send the chat history on every call. The model stores none.
→ Set a max output length. Every extra token adds time and cost.
→ Use low temperature for extraction and tests; it still needs checks.
→ Change one sampling setting at a time, then compare outputs.

Takeaway
An LLM does not look things up. It turns scores into odds and draws likely text, one token at a time.

Next: what the model sees in one call. The system prompt, the chat history, documents and your question, all sharing one context window.

#AIEngineering #LLM #MachineLearning #GenerativeAI #SoftwareEngineering
