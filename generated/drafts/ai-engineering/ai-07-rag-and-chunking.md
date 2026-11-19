SERIES:    AI ENGINEERING #07
TITLE:     RAG and Chunking: Handing the Model the Right Page
PILLAR:    AI Engineering — for developers building on private or changing data
LEVEL:     INTERMEDIATE
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Retrieval only finds what you cut
LAYOUT:    FLOW
VISUALS:   1 = How does RAG give the model the right page? · 2 = What happens ahead of time, and at question time? · 3 = Why does the way you cut documents matter? · 4 = Which chunking strategy should you start with? · 5 = How do you know retrieval works? · 6 = Takeaway · rest = text
STATUS:    draft
---
A model only knows what it saw in training. It has never read your company handbook.

So you add search. And the bot still answers wrong, because the search returned half a paragraph that never says what "it" refers to.

RAG gives the model the right page at question time. Chunking decides what a "page" is.

How does RAG give the model the right page?
RAG (Retrieval-Augmented Generation) means: find the relevant text first, then give it to the model with the question. Retrieval means searching. Generation means writing the answer.

Think of an open-book exam. You do not memorise the book. You find the right page, then answer from it.

Why do we need it? Without RAG, the model answers from training data. That data can be old, and it never had your private documents. So it guesses. With RAG, the answer comes from text you chose, and you can show the source.

Key properties
• The model does not change. Only the prompt changes.
• Update a document and the next answer uses it. No retraining.
• Quality depends mostly on retrieval. Wrong text in, wrong answer out.
• Sources can be cited, so users can check the answer.

Takeaway: RAG does not teach the model. It hands it the right page at the right time.

What happens ahead of time, and at question time?
Ahead of time:
1. Split documents into chunks (small pieces of text).
2. Turn each chunk into an embedding (#06) and store it.
At question time:
3. Embed the question.
4. Find the chunks closest to it.
5. Put those chunks in the prompt with the question (they take room in the window, #03).
6. The model answers and cites what it used.

Link to tool calling (#04): your code can always search first. Or you give the model a search tool and let it decide when to look.

Where is it used? Internal docs assistants, support bots over help articles, policy search, coding assistants that search a repo.
Use it when answers must come from specific, private or changing documents.
Skip it when the whole source fits easily in the prompt.

Takeaway: RAG is search first, then answer from what was found.

Why does the way you cut documents matter?
Step 1 above decides everything after it. A fast search (#06) over badly cut text still returns the wrong text.

Chunking means splitting documents into smaller pieces before you embed them. Each piece, a chunk, gets its own embedding and is found on its own.

Think of cutting a cake. Slices too big and nobody can eat one. Too small and you get crumbs. The cut decides what each person gets.

Both extremes fail:
→ Too big: one embedding for a long document blends many topics into one vector. It matches everything a little and nothing well.
→ Too small: chunks lose context. "It must be signed within 30 days" means little if the chunk never says what "it" is.

Key properties
• Size is a trade-off. Small: sharp match, little context. Large: more context, blurrier match.
• Overlap repeats a little text between neighbouring chunks, so a sentence at the edge is not lost.
• Splitting on structure beats blind cuts, when the text has structure.
• Metadata on each chunk (title, section, source) helps filtering and citing.

Takeaway: retrieval can only return what your chunks contain.

Which chunking strategy should you start with?
Four common strategies
→ Fixed size: every N tokens, with overlap. Simple, a fair baseline.
→ Recursive: split by section, then paragraph, then sentence, until pieces fit.
→ Structure-based: headings, sections or code functions become the borders.
→ Semantic: start a new chunk where the meaning shifts, measured with embeddings. Slower to build.

[FACT_CHECK: recursive splitting goes section → paragraph → sentence until pieces fit → LangChain RecursiveCharacterTextSplitter docs (default separators)]

Steps to choose
1. Start with recursive splitting and a small overlap.
2. Collect real questions with the passages that answer them.
3. Try two or three sizes. Keep the one that returns the right passages.

Chunk long documents you need to search. Skip it for short items that are already one idea each, like FAQ entries.

Senior detail: add context before you embed. Putting the title and section heading in front of each chunk is cheap, and fixes many chunks that make no sense alone. The "30 days" chunk becomes "Supplier contract › Renewal: It must be signed within 30 days".

[FACT_CHECK: putting the title/section before each chunk improves retrieval → Anthropic "Introducing Contextual Retrieval" (Sept 2024)]

Takeaway: start recursive, then let real questions pick the size.

How do you know retrieval works?
Test retrieval on its own. Keep a set of real questions with the chunks that should come back. Check those before you blame the model.

When the chunks lack the answer, the model should not guess. Tell it to say "not found".

[PERSONAL: one RAG answer that was wrong because retrieval returned the wrong chunk, and what fixed it]

Takeaway: test the search before you blame the model.

Keep in mind when you ship a RAG feature
→ Re-index a document when it changes, or answers quote the old one.
→ Show the cited chunks to users, so they can check the answer.
→ Re-run your retrieval test set after every chunking change.
→ Log which chunks each answer used: you need them to debug a wrong one.

Takeaway
RAG hands the model the right page at question time. Chunking decides what a page is, and testing retrieval tells you if it worked.

Next: RAG vs fine-tuning vs long context. Three ways to give a model knowledge, and which problem each one solves.

#AIEngineering #RAG #LLM #Embeddings #SoftwareEngineering
