SERIES:    AI ENGINEERING #06
TITLE:     Embeddings: Turning Text into Numbers
PILLAR:    AI Engineering — for developers building search and RAG
HEADLINE:  Embeddings turn meaning into numbers
LAYOUT:    ANATOMY
---
Search for "cheap flights" and a keyword search misses a page titled "low-cost airfare". Embeddings fix that.

What is it?
An embedding is a list of numbers that represents the meaning of a piece of text. That list is called a vector. Texts with similar meaning get vectors that sit close together.

Think of a map. Every city has coordinates. Cities near each other have close numbers. Embeddings do the same for meaning, just with hundreds or thousands of coordinates instead of two.

Why do we need it?
Computers compare numbers well. They do not compare meaning well. Embeddings turn "is this similar?" into a maths question: how close are these two vectors?

Key properties
• An embedding model makes them. It is a different job from a chat model. It returns numbers, not text.
• Every vector from one model has the same length. The length varies by model.
• Vectors from different models cannot be compared. Use the same model for your documents and your queries.
• Closeness is usually measured with cosine similarity (how much two vectors point the same way).

Example
function cosine(a, b) {
  let dot = 0, na = 0, nb = 0;
  for (let i = 0; i < a.length; i++) {
    dot += a[i] * b[i]; na += a[i] ** 2; nb += b[i] ** 2;
  }
  return dot / (Math.sqrt(na) * Math.sqrt(nb));
}

Close to 1 means similar direction. Near 0 means unrelated.

Where is it used?
→ Semantic search (search by meaning, not exact words).
→ RAG, to find the right documents to give a model.
→ Recommendations and "related items".
→ Grouping similar tickets and finding duplicates.

When to use it / when not to
Use it when meaning matters more than exact words.
Do not use it alone for exact matches like IDs, error codes or product numbers. Keyword search wins there. Many systems combine both.

Senior detail: change your embedding model and you must re-embed everything. Old and new vectors live in different spaces.

Takeaway: embeddings let you compare meaning with maths.

Next: structured output. How to get JSON from a model that you can actually trust.

#AIEngineering #Embeddings #RAG #LLM
