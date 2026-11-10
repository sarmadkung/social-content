---
title: "System design is choosing which trade-off you can live with"
description: "What system design actually is, in plain words: the parts of a system, the five properties every design trades, and five steps to design any system."
date: 2026-10-30
series: "System Architecture"
seriesNumber: 1
slug: arch-01-what-is-system-design
tags: [system-design, architecture, scalability, backend]
cover: cover.png
---

Your code works on your laptop. Then 10,000 people use it at once, and it falls over.

Often the code did not change. The load did, and it found the weak spot: a slow database, a lock, a limit you never hit alone. That gap is what system design is about.

## What we'll cover

![In this post: the parts, five properties, five steps](0.png)

1. **The parts:** servers, databases, caches, queues, and the network between them.
2. **Five properties:** what every design trades.
3. **Five steps:** how to design any system, then repeat.

## What is it?

![Users reach app servers over the network; the app servers use a cache, a database and a queue, and a worker takes jobs from the queue](1.png)

System design is deciding how the parts of a software system fit together: servers, databases, caches, queues, and the network between them.

- A **server** is a computer that runs your code and answers requests, like the machine that sends back your feed when you open an app.
- A **database** stores data so it is still there after a restart, like every order a shop has ever taken.
- A **cache** is a fast, short-lived copy of data that is read often, like today's top products kept in memory.
- A **queue** is a waiting line of jobs to do later, so the user doesn't wait. A worker picks up "send the receipt email" after the order is saved.

Every arrow between those parts is a trip over the network. Each trip adds time, and each one can fail.

Think of cooking one meal at home versus running a restaurant kitchen. Same recipes. But now you need more cooks, a clear order flow, a backup fridge, and a plan for the dinner rush.

## Why do we need it?

Code answers "does it work?" System design answers "does it keep working?" With more users, more data, and parts that fail on a bad day.

## Key properties we design for

![Five properties: scalability, availability, latency, consistency, cost and simplicity, with two example trade-offs](2.png)

- **Scalability:** handling more users by adding resources.
- **Availability:** staying up when a part fails.
- **Latency:** how long one request takes.
- **Consistency:** every user seeing the same, correct data.
- **Cost and simplicity:** what it takes to run the system and to change it.

You can't max them all. Every choice trades one property for another. Faster reads can cost fresher data: a cache answers quickly, but its copy can be old. More servers cost more money.

## Where is it used?

Every product with real users: Instagram, Uber, your bank app.

## When to use it, and when not to

- **Use it** before building something that must grow or must not go down.
- **Not yet** for a prototype with ten users. Ship first, then measure.

## Steps to design any system

![Five steps on a photo-sharing app: what it must do, how well, the simplest version, where it breaks, fix that part, then back to step 4](3.png)

1. Ask what it must do (features).
2. Ask how well (users, speed, uptime).
3. Draw the simplest version that works.
4. Find where it breaks under load.
5. Fix that one part. Repeat.

Take a photo-sharing app. It must let people post a photo and see their friends' photos. Say it needs to serve a million users, open the feed in under a second, and stay up if a server dies. The simplest version is one app server and one database. Under load, the weak spot is the database: every feed open reads it. So you fix that one part, for example by keeping each feed in a cache. Then more users find the next weak spot, and you go round again.

## Keep in mind when you design your first system

- Write numbers down: "lots of users" is not a requirement.
- Start with one server and one database. Add parts later.
- Every part you add is one more thing that can fail.
- Find the weak spot by measuring, not by guessing.
- For each choice, name what it costs, not just what it gains.

**In one line:** system design is not about knowing tools. It is about choosing which trade-off you can live with.

## Next in the series

Requirements first: what a system must do versus how well it must do it.
