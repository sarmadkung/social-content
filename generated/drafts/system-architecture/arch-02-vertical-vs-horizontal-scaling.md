SERIES:    SYSTEM ARCHITECTURE #02
TITLE:     Vertical vs Horizontal Scaling
PILLAR:    System Design & Architecture — for juniors and mid-levels preparing for interviews
HEADLINE:  Bigger machine, or more machines?
LAYOUT:    COMPARE
---
Traffic doubled. Your server is at 100% CPU. You have two ways out.

What is it?
Scaling means giving a system more capacity so it can handle more load.

Vertical scaling (scale up): make one machine bigger. More CPU, more RAM, faster disk.
Horizontal scaling (scale out): add more machines and split the work between them.

Think of a shop with a long line. Vertical: train your one cashier to work faster. Horizontal: open more checkout counters.

Why do we need it?
Every machine has a limit. Past that limit, requests wait, time out, and users leave.

Key properties
→ Vertical is simple. No code changes. Your app still runs on one box.
→ Vertical has a ceiling. There is a largest machine you can buy, and big machines get expensive fast.
→ Vertical keeps one point of failure. If that box dies, everything dies.
→ Horizontal has no hard ceiling, and one machine dying does not take you down.
→ Horizontal needs a stateless app: no user data kept in one server's memory.

Where is it used?
Vertical: databases like PostgreSQL often start here, because splitting data is hard.
Horizontal: web and API servers behind a load balancer, AWS Auto Scaling groups, Kubernetes adding pods.

When to use it / when not to
Vertical: early on, or for parts that are hard to split, like a database.
Horizontal: when you need to survive a machine failure, or you have hit the biggest machine.

Example
Your API stores user sessions in server memory. You add a second server. Now half your users get logged out on each request.
Fix: move sessions to a shared store like Redis. Now any server can answer any request.

Comparison
Vertical = simple, limited, one point of failure.
Horizontal = more parts, near-unlimited, survives failures.

[PERSONAL: one line on when you scaled up first and why it was the right call]

Most real systems do both. Scale the database up. Scale the app servers out.

Takeaway: Scale up until it hurts. Scale out when you need to survive failure.

Next: load balancers, the piece that makes horizontal scaling work.

#SystemDesign #Scalability #SoftwareArchitecture #BackendDevelopment
