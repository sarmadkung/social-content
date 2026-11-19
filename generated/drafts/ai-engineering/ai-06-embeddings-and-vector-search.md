SERIES:    AI ENGINEERING #06
TITLE:     Embeddings and Vector Search: Finding Text by Meaning, Fast
PILLAR:    AI Engineering — for developers building search and RAG
LEVEL:     INTERMEDIATE
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Find similar meaning without checking everything
LAYOUT:    ANATOMY
VISUALS:   1 = How does text become a list of numbers? · 2 = How do you measure "close"? · 3 = Why does exact search get slow? · 4 = How does an ANN index search less? · 5 = Takeaway · rest = text
STATUS:    draft
---
Search for "cheap flights" and a keyword search misses a page titled "low-cost airfare". Embeddings fix that.

Then a second problem shows up. With a few thousand texts, comparing the query with each one is fine. With millions, checking every one on every request gets slow. Vector search fixes that.

How does text become a list of numbers?
An embedding is a list of numbers that represents the meaning of a piece of text. That list is called a vector. Texts with similar meaning get vectors that sit close together.

Think of a map. Every city has coordinates. Cities near each other have close numbers. Embeddings do the same for meaning, just with hundreds or thousands of coordinates instead of two.

Why do we need it? Computers compare numbers well. They do not compare meaning well. Embeddings turn "is this similar?" into a maths question: how close are these two vectors?

Key properties
• An embedding model makes them. It is a different job from a chat model. It returns numbers, not text.
• Every vector from one model has the same length. The length varies by model.
• Vectors from different models cannot be compared. Use the same model for your documents and your queries.

[FACT_CHECK: every vector from one model has the same length → OpenAI embeddings docs (some models allow a chosen `dimensions` size)]

Takeaway: an embedding turns meaning into a position you can measure.

How do you measure "close"?
Closeness is usually measured with cosine similarity: how much two vectors point the same way.

function cosine(a, b) {
  let dot = 0, na = 0, nb = 0;
  for (let i = 0; i < a.length; i++) {
    dot += a[i] * b[i]; na += a[i] ** 2; nb += b[i] ** 2;
  }
  return dot / (Math.sqrt(na) * Math.sqrt(nb));
}

Close to 1 means similar direction. Near 0 means unrelated.

Other measures are dot product and Euclidean distance. The one you use should match what your embedding model expects.

[FACT_CHECK: distance measure should match what the embedding model expects → embedding model docs (e.g. OpenAI embeddings FAQ on normalised vectors)]

Where is it used?
→ Semantic search (search by meaning, not exact words).
→ RAG, to find the right documents to give a model (next post).
→ Recommendations and "related items".
→ Grouping similar tickets and finding duplicates.

Do not use it alone for exact matches like IDs, error codes or product numbers. Keyword search wins there. Many systems combine both.

Takeaway: similar meaning becomes a number close to 1.

Why does exact search get slow?
RAG needs "find the texts closest to this question". The simple way compares the query with every vector, using the function above. It is exact, but it costs O(n × d) per query: n vectors, each with d numbers. The cost grows with every text you add.

A vector database stores embeddings and finds the ones closest to a query vector. That search is called similarity search, or nearest-neighbour search.

Think of a library. You do not check every shelf for a cookery book. Books are grouped by topic. You walk to the right section and look there.

Takeaway: checking every vector is exact, but its cost grows with your data.

How does an ANN index search less?
A vector database uses an ANN index (approximate nearest neighbour). It checks a small part of the data, not all of it.

Approximate means it can miss a true best match. You trade a little accuracy for a lot of speed. Recall measures that trade: of the true top results, how many came back.

Two common index types
→ IVF: groups vectors into clusters, then searches only the nearest clusters. The library idea.
→ HNSW: a graph that links each vector to close neighbours. Fast and accurate, but memory-hungry.

[FACT_CHECK: IVF clusters vectors and searches only the nearest clusters → FAISS docs / wiki (IndexIVF)]
[FACT_CHECK: HNSW is a neighbour graph, fast and accurate but memory-hungry → Malkov & Yashunin 2016 HNSW paper and FAISS / pgvector docs]

It also stores metadata (source, date, team) with each vector, so you can filter.

Senior detail: filters and ANN can clash. Filter after the search, and a strict filter may leave too few results. Check how your database handles filtering before you rely on it.

[FACT_CHECK: filtering after ANN search can leave too few results → pgvector README (filtering, iterative index scans) and your vector DB's filtering docs]

Takeaway: an ANN index gives up a little accuracy to find "similar" fast.

Where does it run, and when do you need it?
You can use a dedicated vector database or a vector extension for a database you already run, like pgvector for PostgreSQL.
Use an ANN index when exact search is too slow for your data.
Skip it for small collections. Exact search is simple and never misses.

Senior detail: change your embedding model and you must re-embed everything. Old and new vectors live in different spaces.

Keep in mind when you add vector search
→ Store the embedding model's name with every vector, for the day you re-embed.
→ Start with exact search; add an index when it is measurably slow.
→ Measure recall on real queries after you add or tune an index.
→ Keep keyword search next to it for IDs, codes and names.

Takeaway
Embeddings let you compare meaning with maths. A vector index makes that comparison fast, at the price of sometimes missing a match.

Next: RAG and chunking. How to hand the model the right text at question time, and why the way you cut documents decides what it finds.

#AIEngineering #Embeddings #VectorDatabase #RAG #LLM
