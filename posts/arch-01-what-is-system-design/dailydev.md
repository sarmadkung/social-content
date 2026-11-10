TITLE: System design is choosing which trade-off you can live with
COVER: cover.png
---

Your code works on your laptop. Then 10,000 people use it at once, and it falls over. Often the code did not change. The load did, and it found the weak spot: a slow database, a lock, a limit you never hit alone.

Code answers "does it work?" System design answers "does it keep working?" with more users, more data, and parts that fail on a bad day.

- **What it is.** Deciding how the parts of a system fit together: servers, databases, caches, queues, and the network between them.
- **What you design for.** Scalability (more users by adding resources), availability (staying up when a part fails), latency (how long one request takes), consistency (everyone sees the same, correct data), and cost and simplicity.
- **Every choice trades one for another.** A cache makes reads faster but data can be old. More servers serve more users but cost more.
- **The loop.** Ask what it must do. Ask how well. Draw the simplest version that works. Find where it breaks under load. Fix that one part. Repeat.
- **When not yet.** A prototype with ten users needs shipping, not a design. Ship first, then measure.

System design is not about knowing tools. It is about choosing which trade-off you can live with.
