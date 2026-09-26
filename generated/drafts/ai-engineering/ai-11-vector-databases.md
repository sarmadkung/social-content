SERIES:    AI ENGINEERING #11
TITLE:     Vector Databases and Similarity Search
PILLAR:    AI Engineering — for developers scaling search and RAG
LEVEL:     INTERMEDIATE
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Find similar without checking everything
LAYOUT:    COMPARE
STATUS:    draft
---
RAG needs "find the chunks closest to this question". With a few thousand chunks, a loop is fine. With millions, checking every one on every request gets slow.

What is it?
A vector database stores embeddings (#06) and finds the ones closest to a query vector. That search is called similarity search, or nearest-neighbour search.

Think of a library. You do not check every shelf for a cookery book. Books are grouped by topic. You walk to the right section and look there.

Why do we need it?
The simple way compares the query with every vector. It is exact, but it costs O(n × d) per query: n vectors, each with d numbers. The cost grows with every chunk you add.

Key properties
• It uses an ANN index (approximate nearest neighbour). It checks a small part of the data, not all of it.
• Approximate means it can miss a true best match. You trade a little accuracy for a lot of speed.
• Recall measures that trade: of the true top results, how many came back.
• It stores metadata (source, date, team) with each vector, so you can filter.
• The distance measure (cosine, dot product, Euclidean) should match what your embedding model expects.

Two common index types
→ IVF: groups vectors into clusters, then searches only the nearest clusters. The library idea.
→ HNSW: a graph that links each vector to close neighbours. Fast and accurate, but memory-hungry.

Where is it used?
The retrieval step of RAG, semantic search, recommendations, duplicate detection. You can use a dedicated vector database or a vector extension for a database you already run, like pgvector for PostgreSQL.

When to use it / when not to
Use an ANN index when exact search is too slow for your data.
Skip it for small collections. Exact search is simple and never misses.

Senior detail: filters and ANN can clash. Filter after the search, and a strict filter may leave too few results. Check how your database handles filtering before you rely on it.

Takeaway: a vector database gives up a little accuracy to find "similar" fast.

Next: chunking. What you store matters more than where you store it.

#AIEngineering #VectorDatabase #RAG #SystemDesign
