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

### Building blocks
- #05 Vertical vs horizontal scaling · COMPARE · needs #03
- #06 Load balancers · TEACH · needs #05
- #07 Caching (where to cache, and cache invalidation) · TEACH · needs #03
- #08 CDNs · TEACH · needs #07
- #09 Database replication (read replicas) · TEACH · needs —
- #10 Your database is at 90% CPU. What do you try first? · SCENARIO · needs #06, #07, #09
- #11 Sharding / partitioning · TEACH · needs #09, #10
- #12 Message queues and async processing · TEACH · needs —
- #13 Pub/Sub and event-driven architecture · TEACH · needs #12

### Trade-offs and theory
- #14 CAP theorem in plain English · TEACH · needs #09
- #15 Consistency models: strong vs eventual · COMPARE · needs #14
- #16 Monolith vs microservices · COMPARE · needs —
- #17 Stateless services · TEACH · needs #06

### Reliability
- #18 Single points of failure · TEACH · needs #03
- #19 Circuit breakers · TEACH · needs #18
- #20 Health checks and graceful degradation · TEACH · needs #06, #18
- #21 Your API gets 10× the traffic. What breaks first? · SCENARIO · needs #06, #07, #09, #12
- #22 Back-pressure · TEACH · needs #12

### Case studies
- #23 Design a URL shortener · SCENARIO · needs #04, #07, #11
- #24 Design a rate limiter · SCENARIO · needs #07
- #25 Design a chat system (real-time) · SCENARIO · needs #12, #13
- #26 Design a notification system · SCENARIO · needs #12, #13
- #27 How to approach a system design interview · LIST · needs #02, #03, #04
