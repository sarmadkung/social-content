SERIES:    AI ENGINEERING #09
TITLE:     RAG: Retrieval-Augmented Generation, Plainly
PILLAR:    AI Engineering — for developers building on private or changing data
LEVEL:     INTERMEDIATE
HEADLINE:  RAG hands the model the right page
LAYOUT:    FLOW
STATUS:    draft
---
A model only knows what it saw in training. It has never read your company handbook. RAG gives it the right page at question time.

What is it?
RAG (Retrieval-Augmented Generation) means: find the relevant text first, then give it to the model with the question. Retrieval means searching. Generation means writing the answer.

Think of an open-book exam. You do not memorise the book. You find the right page, then answer from it.

Why do we need it?
Without RAG, the model answers from training data. That data can be old, and it never had your private documents. So it guesses. With RAG, the answer comes from text you chose, and you can show the source.

Key properties
• The model does not change. Only the prompt changes.
• Update a document and the next answer uses it. No retraining.
• Quality depends mostly on retrieval. Wrong text in, wrong answer out.
• Sources can be cited, so users can check the answer.

Steps
Ahead of time:
1. Split documents into chunks (small pieces of text).
2. Turn each chunk into an embedding (#06) and store it.
At question time:
3. Embed the question.
4. Find the chunks closest to it.
5. Put those chunks in the prompt with the question.
6. The model answers and cites what it used.

Link to #08: your code can always search first. Or you give the model a search tool and let it decide when to look.

Where is it used?
Internal docs assistants, support bots over help articles, policy search, coding assistants that search a repo.

When to use it / when not to
Use it when answers must come from specific, private or changing documents.
Skip it when the whole source fits easily in the prompt.

Senior detail: test retrieval on its own. Keep a set of real questions with the chunks that should come back. Check those before you blame the model. And tell the model to say "not found" when the chunks lack the answer.

[PERSONAL: one RAG answer that was wrong because retrieval returned the wrong chunk, and what fixed it]

Takeaway: RAG does not teach the model. It hands it the right page at the right time.

Next: vector databases. Where the embeddings live, and how "find the closest" stays fast.

#AIEngineering #RAG #LLM #Embeddings
