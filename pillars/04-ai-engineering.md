# Pillar 4 — AI Engineering

Series label: `AI ENGINEERING #NN` · Visual accent: indigo `#8AA4FF` · Tag: `AI ENGINEERING`

## Purpose
AI engineering is software engineering applied to systems that use models.
Teach how LLM systems work and how to make them reliable in production.

## Audience
Developers moving into AI engineering, engineers adding LLMs to products,
seniors thinking about architecture, cost and reliability.

## Roadmap (post in this order)
Each line: `#NN Title · MODE · needs <earlier posts>`. Modes are defined in the
master prompt. Never more than 4 TEACH posts in a row.

### Foundations
- #01 AI foundations: AI vs ML vs deep learning, what a model is, neural networks, how a model learns, training vs inference (one post, one image per idea) · TEACH · needs —
- #02 What an LLM actually does: tokens, the next-token loop, logits and softmax, temperature, top-k and top-p · TEACH · needs #01
- #03 What the model sees in one call: system prompt, user prompt, chat history, documents and the context window · TEACH · needs #02

### Building LLM apps
- #04 Structured output and tool calling: JSON you can trust, and how a model asks your code to act · TEACH · needs #03
- #05 Agents are software: the loop, and agent vs workflow · COMPARE · needs #04
- #06 Embeddings and vector search: similarity, ANN indexes (IVF, HNSW), vector databases · TEACH · needs #02
- #07 RAG and chunking: retrieval at question time, how to cut documents, testing retrieval · TEACH · needs #03, #06
- #08 RAG vs fine-tuning vs long context · COMPARE · needs #01, #07

### Agents
- #09 Context engineering · TEACH · needs #03, #05
- #10 AI memory: short-term vs long-term · COMPARE · needs #09
- #11 Multi-agent systems (and when not to use them) · TEACH · needs #05
- #12 MCP (Model Context Protocol) in plain English · TEACH · needs #04
- #13 5 reasons AI agents fail in production · LIST · needs #05, #09–#12

### Production
- #14 Evaluating LLM output (evals) · TEACH · needs #02
- #15 Hallucinations: why they happen and how to defend · WHY · needs #02, #07
- #16 Your LLM app is accurate but too expensive. What do you change first? (caching, model choice, batching, latency) · SCENARIO · needs #03, #14
- #17 Prompt injection and AI security basics · TEACH · needs #03, #04
- #18 Observability for AI systems · TEACH · needs #14
- #19 Choosing a model · LIST · needs #14, #16

Merged on 2026-11-19 (old → new): #02 + #05 + the token half of #03 → #02 · #03 (context window) + #04 → #03 · #07 + #08 → #04 · #09 + #14 → #05 · #06 + #11 → #06 · #10 + #12 → #07 · #13 → #08 · #15 → #09 · roadmap #22 (cost and latency) + #25 (too-expensive scenario) → #16. Old drafts are in `archive/merged-2026-11-19/`.

## Content opportunities
A project decision [PERSONAL] · A failure mode · Architecture diagram · Cost trade-off
