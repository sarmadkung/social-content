# Pillar 3 — System Design & Architecture

Series label: `SYSTEM ARCHITECTURE #NN` · Visual accent: violet `#C084FC` · Tag: `ARCHITECTURE`

## Purpose
Explain how systems are designed to scale, stay up and stay simple. Each post
teaches one building block and the trade-off it brings.

## Audience
Mid-levels preparing for system design interviews, juniors who want the big
picture, seniors who enjoy a clear trade-off.

## Roadmap (post in this order)
Each line: `#NN Title · MODE · needs <earlier posts>`. Modes are defined in the
master prompt. Never more than 4 TEACH posts in a row.

### Foundations
- #01 What system design actually is · TEACH · needs —
- #02 Requirements first: functional vs non-functional, and the three numbers (latency, throughput, availability) · TEACH · needs #01
- #03 Back-of-the-envelope estimation: a photo app in five minutes · SCENARIO · needs #02

### Building blocks
- #04 Scaling out: vertical vs horizontal scaling, and load balancers · COMPARE · needs #02
- #05 Caching and CDNs: where to cache, and when to forget · TEACH · needs #02
- #06 Your database is at 90% CPU. What do you try first? · SCENARIO · needs #04, #05
- #07 Replication and sharding: copy the data, then split it · TEACH · needs #04, #06
- #08 Message queues and pub/sub: async work and event-driven architecture · TEACH · needs —

### Trade-offs and theory
- #09 CAP theorem and consistency models: strong vs eventual · COMPARE · needs #07
- #10 Monolith vs microservices · COMPARE · needs —
- #11 Stateless services · TEACH · needs #04

### Reliability
- #12 Staying up when parts fail: single points of failure, health checks, circuit breakers and graceful degradation · TEACH · needs #02, #04
- #13 Your API gets 10× the traffic. What breaks first? · SCENARIO · needs #04, #05, #07, #08
- #14 Back-pressure · TEACH · needs #08

### Case studies
- #15 Design a URL shortener · SCENARIO · needs #03, #05, #07
- #16 Design a rate limiter · SCENARIO · needs #05
- #17 Design a chat system (real-time) · SCENARIO · needs #08
- #18 Design a notification system · SCENARIO · needs #08
- #19 How to approach a system design interview · LIST · needs #02, #03
