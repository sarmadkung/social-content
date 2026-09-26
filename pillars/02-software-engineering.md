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
- #02 Client and server: what happens when your app calls an API · TEACH · needs —
- #03 One HTTP request, step by step (DNS, connection, request, response) · TEACH · needs #02

### Engineering basics
- #04 Timeouts: the setting every network call needs · TEACH · needs #03
- #05 Retries with backoff (and why infinite retries cause outages) · TEACH · needs #04
- #06 A payment request times out. What should your code do? · SCENARIO · needs #04, #05
- #07 Idempotency: making "try again" safe · TEACH · needs #05, #06
- #08 Error handling: fail loudly, recover deliberately · TEACH · needs #04
- #09 Logging vs metrics vs traces (observability basics) · COMPARE · needs #08

### Backend and APIs
- #10 REST API design basics (resources, verbs, status codes) · TEACH · needs #03
- #11 REST vs GraphQL vs gRPC · COMPARE · needs #10
- #12 Pagination: offset vs cursor · COMPARE · needs #10
- #13 Authentication vs Authorization · COMPARE · needs #03
- #14 WebSockets vs polling vs Server-Sent Events · COMPARE · needs #03
- #15 Rate limiting · TEACH · needs #03
- #16 7 things I check before shipping an API · LIST · needs #04–#15

### Data
- #17 SQL vs NoSQL: how to actually choose · COMPARE · needs —
- #18 Why database indexes make queries fast (and what they cost) · WHY · needs #17
- #19 Transactions and ACID in plain English · TEACH · needs #17
- #20 N+1 query problem · TEACH · needs #18
- #21 5 database mistakes that show up in production · LIST · needs #17–#20

### Frontend and mobile
- #22 State management: local, shared, server state · TEACH · needs —
- #23 React rendering: why components re-render · WHY · needs #22
- #24 Data fetching and caching on the client · TEACH · needs #22
- #25 Offline-first mobile apps · TEACH · needs #24

### Quality and delivery
- #26 The testing pyramid (unit, integration, e2e) · TEACH · needs —
- #27 Code review: what to look for · LIST · needs —
- #28 CI/CD in plain English · TEACH · needs #26
- #29 Technical debt: when to pay it · WHY · needs —
- #30 Writing code others can maintain · TEACH · needs —

## Content opportunities
A production bug · A trade-off decision · Before/after refactor · A checklist
