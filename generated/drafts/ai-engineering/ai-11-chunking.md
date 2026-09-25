SERIES:    AI ENGINEERING #11
TITLE:     Chunking Strategies for RAG
PILLAR:    AI Engineering — for developers whose RAG finds the wrong text
LEVEL:     INTERMEDIATE
HEADLINE:  Retrieval only finds what you cut
LAYOUT:    GRID
STATUS:    draft
---
Last post: finding the closest vectors fast. But a fast search over badly cut text still returns the wrong text.

What is it?
Chunking means splitting documents into smaller pieces before you embed them. Each piece, a chunk, gets its own embedding and is found on its own.

Think of cutting a cake. Slices too big and nobody can eat one. Too small and you get crumbs. The cut decides what each person gets.

Why do we need it?
One embedding for a long document blends many topics into one vector. It matches everything a little and nothing well. But tiny chunks lose context. "It must be signed within 30 days" means little if the chunk never says what "it" is.

Key properties
• Size is a trade-off. Small: sharp match, little context. Large: more context, blurrier match.
• Overlap repeats a little text between neighbouring chunks, so a sentence at the edge is not lost.
• Splitting on structure beats blind cuts, when the text has structure.
• Metadata on each chunk (title, section, source) helps filtering and citing.

Four common strategies
→ Fixed size: every N tokens, with overlap. Simple, a fair baseline.
→ Recursive: split by section, then paragraph, then sentence, until pieces fit.
→ Structure-based: headings, sections or code functions become the borders.
→ Semantic: start a new chunk where the meaning shifts, measured with embeddings. Slower to build.

Steps to choose
1. Start with recursive splitting and a small overlap.
2. Collect real questions with the passages that answer them.
3. Try two or three sizes. Keep the one that returns the right passages.

Where is it used?
Every RAG pipeline: docs search, support bots, code search.

When to use it / when not to
Chunk long documents you need to search.
Skip it for short items that are already one idea each, like FAQ entries.

Senior detail: add context before you embed. Putting the title and section heading in front of each chunk is cheap, and fixes many chunks that make no sense alone.

Takeaway: retrieval can only return what your chunks contain. Cut with care.

Next: RAG vs fine-tuning vs long context. Three ways to give a model knowledge.

#AIEngineering #RAG #LLM #SoftwareEngineering
