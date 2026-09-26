# Pillar 2 — Software Engineering

Series label: `SOFTWARE ENGINEERING #NN` · Visual accent: green `#4ADE80` · Tag: `ENGINEERING`

## Purpose
Share practical engineering knowledge from building real products across
frontend, mobile, backend and infrastructure. Hands-on, not framework tutorials.

## Audience
Juniors becoming professional engineers, mid-levels taking ownership, seniors
comparing trade-offs.

## Roadmap (post in this order)
Each line: `#NN Title · MODE · needs <earlier posts>`. Modes are defined in the
master prompt. Never more than 4 TEACH posts in a row.

### Foundations
- #01 Ship the boring architecture first · WHY · needs —
- #02 One HTTP request, step by step (DNS, connection, request, response) · TEACH · needs —

### Engineering basics
- #03 Timeouts: the setting every network call needs · TEACH · needs #02
- #04 Retries with backoff (and why infinite retries cause outages) · TEACH · needs #03
- #05 A payment request times out. What should your code do? · SCENARIO · needs #03, #04
- #06 Idempotency: making "try again" safe · TEACH · needs #04, #05
- #07 Error handling: fail loudly, recover deliberately · TEACH · needs #03
- #08 Logging vs metrics vs traces (observability basics) · COMPARE · needs #07

### Backend and APIs
- #09 REST API design basics (resources, verbs, status codes) · TEACH · needs #02
- #10 REST vs GraphQL vs gRPC · COMPARE · needs #09
- #11 Pagination: offset vs cursor · COMPARE · needs #09
- #12 Authentication vs Authorization · COMPARE · needs #02
- #13 WebSockets vs polling vs Server-Sent Events · COMPARE · needs #02
- #14 Rate limiting · TEACH · needs #02
- #15 7 things I check before shipping an API · LIST · needs #03–#14

### Data
- #16 SQL vs NoSQL: how to actually choose · COMPARE · needs —
- #17 Why database indexes make queries fast (and what they cost) · WHY · needs #16
- #18 Transactions and ACID in plain English · TEACH · needs #16
- #19 N+1 query problem · TEACH · needs #17
- #20 5 database mistakes that show up in production · LIST · needs #16–#19

### Frontend and mobile
- #21 State management: local, shared, server state · TEACH · needs —
- #22 React rendering: why components re-render · WHY · needs #21
- #23 Data fetching and caching on the client · TEACH · needs #21
- #24 Offline-first mobile apps · TEACH · needs #23

### Quality and delivery
- #25 The testing pyramid (unit, integration, e2e) · TEACH · needs —
- #26 Code review: what to look for · LIST · needs —
- #27 CI/CD in plain English · TEACH · needs #25
- #28 Technical debt: when to pay it · WHY · needs —
- #29 Writing code others can maintain · TEACH · needs —

## Content opportunities
A production bug · A trade-off decision · Before/after refactor · A checklist
