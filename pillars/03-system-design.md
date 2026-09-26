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
- #02 Requirements first: functional vs non-functional · TEACH · needs #01
- #03 Latency, throughput and availability: the three numbers · TEACH · needs #02
- #04 Back-of-the-envelope estimation: a photo app in five minutes · SCENARIO · needs #03
- #05 The simplest system that works: client, server, database · TEACH · needs #01

### Building blocks
- #06 Vertical vs horizontal scaling · COMPARE · needs #03, #05
- #07 Load balancers · TEACH · needs #06
- #08 Caching (where to cache, and cache invalidation) · TEACH · needs #03, #05
- #09 CDNs · TEACH · needs #08
- #10 Database replication (read replicas) · TEACH · needs #05
- #11 Your database is at 90% CPU. What do you try first? · SCENARIO · needs #07, #08, #10
- #12 Sharding / partitioning · TEACH · needs #10, #11
- #13 Message queues and async processing · TEACH · needs #05
- #14 Pub/Sub and event-driven architecture · TEACH · needs #13

### Trade-offs and theory
- #15 CAP theorem in plain English · TEACH · needs #10
- #16 Consistency models: strong vs eventual · COMPARE · needs #15
- #17 Monolith vs microservices · COMPARE · needs #05
- #18 Stateless services · TEACH · needs #07

### Reliability
- #19 Single points of failure · TEACH · needs #03
- #20 Circuit breakers · TEACH · needs #19
- #21 Health checks and graceful degradation · TEACH · needs #07, #19
- #22 Your API gets 10× the traffic. What breaks first? · SCENARIO · needs #07, #08, #10, #13
- #23 Back-pressure · TEACH · needs #13

### Case studies
- #24 Design a URL shortener · SCENARIO · needs #04, #08, #12
- #25 Design a rate limiter · SCENARIO · needs #08
- #26 Design a chat system (real-time) · SCENARIO · needs #13, #14
- #27 Design a notification system · SCENARIO · needs #13, #14
- #28 How to approach a system design interview · LIST · needs #02, #03, #04
