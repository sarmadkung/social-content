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
- #01 Training vs inference: where a model learns, where you use it · TEACH · needs —
- #02 What an LLM actually does (next-token prediction, plainly) · TEACH · needs #01
- #03 Tokens and context windows · TEACH · needs #02
- #04 Prompts vs system prompts · COMPARE · needs #03
- #05 Temperature: why the same prompt gives different answers · WHY · needs #02
- #06 Embeddings: turning text into numbers · TEACH · needs #03

### Building LLM apps
- #07 Structured output (getting JSON you can trust) · TEACH · needs #04
- #08 Tool calling (function calling) · TEACH · needs #07
- #09 Agents are software, not magic · WHY · needs #08
- #10 RAG: Retrieval-Augmented Generation · TEACH · needs #03, #06
- #11 Vector databases and similarity search · TEACH · needs #06, #10
- #12 Chunking strategies for RAG · TEACH · needs #10, #11
- #13 RAG vs fine-tuning vs long context · COMPARE · needs #01, #10

### Agents
- #14 Agent vs workflow: which one do you need · COMPARE · needs #09
- #15 Context engineering · TEACH · needs #03, #14
- #16 AI memory: short-term vs long-term · COMPARE · needs #15
- #17 Multi-agent systems (and when not to use them) · TEACH · needs #14
- #18 MCP (Model Context Protocol) in plain English · TEACH · needs #08
- #19 5 reasons AI agents fail in production · LIST · needs #14–#18

### Production
- #20 Evaluating LLM output (evals) · TEACH · needs #02
- #21 Hallucinations: why they happen and how to defend · WHY · needs #02, #10
- #22 Cost and latency: caching, model choice, batching · TEACH · needs #03
- #23 Prompt injection and AI security basics · TEACH · needs #04, #08
- #24 Observability for AI systems · TEACH · needs #20
- #25 Your LLM app is accurate but too expensive. What do you change first? · SCENARIO · needs #22
- #26 Choosing a model · LIST · needs #20, #22

## Content opportunities
A project decision [PERSONAL] · A failure mode · Architecture diagram · Cost trade-off
