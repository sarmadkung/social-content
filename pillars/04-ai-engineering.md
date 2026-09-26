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
- #01 AI vs ML vs LLM: what each word actually means · COMPARE · needs —
- #02 Training vs inference: where a model learns, where you use it · TEACH · needs #01
- #03 What an LLM actually does (next-token prediction, plainly) · TEACH · needs #02
- #04 Tokens and context windows · TEACH · needs #03
- #05 Prompts vs system prompts · COMPARE · needs #04
- #06 Temperature: why the same prompt gives different answers · WHY · needs #03
- #07 Embeddings: turning text into numbers · TEACH · needs #04

### Building LLM apps
- #08 Structured output (getting JSON you can trust) · TEACH · needs #05
- #09 Tool calling (function calling) · TEACH · needs #08
- #10 Agents are software, not magic · WHY · needs #09
- #11 RAG: Retrieval-Augmented Generation · TEACH · needs #04, #07
- #12 Vector databases and similarity search · TEACH · needs #07, #11
- #13 Chunking strategies for RAG · TEACH · needs #11, #12
- #14 RAG vs fine-tuning vs long context · COMPARE · needs #02, #11

### Agents
- #15 Agent vs workflow: which one do you need · COMPARE · needs #10
- #16 Context engineering · TEACH · needs #04, #15
- #17 AI memory: short-term vs long-term · COMPARE · needs #16
- #18 Multi-agent systems (and when not to use them) · TEACH · needs #15
- #19 MCP (Model Context Protocol) in plain English · TEACH · needs #09
- #20 5 reasons AI agents fail in production · LIST · needs #15–#19

### Production
- #21 Evaluating LLM output (evals) · TEACH · needs #03
- #22 Hallucinations: why they happen and how to defend · WHY · needs #03, #11
- #23 Cost and latency: caching, model choice, batching · TEACH · needs #04
- #24 Prompt injection and AI security basics · TEACH · needs #05, #09
- #25 Observability for AI systems · TEACH · needs #21
- #26 Your LLM app is accurate but too expensive. What do you change first? · SCENARIO · needs #23
- #27 Choosing a model · LIST · needs #21, #23

## Content opportunities
A project decision [PERSONAL] · A failure mode · Architecture diagram · Cost trade-off
