SERIES:    SYSTEM ARCHITECTURE #01
TITLE:     What System Design Actually Is
PILLAR:    System Design & Architecture — for students and juniors who want the big picture
HEADLINE:  System design is choosing what can break
LAYOUT:    ANATOMY
---
Your code works on your laptop. Then 10,000 people use it at once, and it falls over.

The code did not change. The load did. That gap is what system design is about.

What is it?
System design is deciding how the parts of a software system fit together: servers, databases, caches, queues, and the network between them.

Think of cooking one meal at home versus running a restaurant kitchen. Same recipes. But now you need more cooks, a clear order flow, a backup fridge, and a plan for the dinner rush.

Why do we need it?
Code answers "does it work?" System design answers "does it keep working?" With more users, more data, and parts that fail on a bad day.

Key properties we design for
→ Scalability: handling more users by adding resources
→ Availability: staying up when a part fails
→ Latency: how long one request takes
→ Consistency: every user seeing the same, correct data
→ Cost and simplicity: what it takes to run and change

Where is it used?
Every product with real users. Instagram, Uber, your bank app. It is also the standard senior interview round at most tech companies.

When to use it / when not to
Use it: before building something that must grow or must not go down.
Not yet: for a prototype with ten users. Ship first, then measure.

Steps to design any system
1. Ask what it must do (features).
2. Ask how well (users, speed, uptime).
3. Draw the simplest version that works.
4. Find where it breaks under load.
5. Fix that one part. Repeat.

[PERSONAL: one line on a real system where load, not code, was the problem]

There is no perfect design. Every choice trades one property for another. Faster reads can cost fresher data. More servers cost more money.

Takeaway: System design is not about knowing tools. It is about choosing which trade-off you can live with.

This series covers one building block per post, in order.

Next: vertical vs horizontal scaling, the first choice when traffic grows.

#SystemDesign #SoftwareArchitecture #SoftwareEngineering #BackendDevelopment
