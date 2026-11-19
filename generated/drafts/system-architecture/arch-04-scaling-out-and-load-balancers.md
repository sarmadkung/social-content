SERIES:    SYSTEM ARCHITECTURE #04
TITLE:     Scaling Out: Bigger Machine or More Machines, and the Load Balancer in Front
PILLAR:    System Design & Architecture — for juniors who want the request path, mid-levels preparing for interviews
LEVEL:     BEGINNER
MODE:      COMPARE
FORMAT:    VISUAL
HEADLINE:  Bigger machine, or more machines?
LAYOUT:    COMPARE
VISUALS:   1 = Should you scale up or scale out? · 2 = Why does a second server log users out? · 3 = How does a load balancer pass one request to a server? · 4 = How does a load balancer pick a server? · 5 = Takeaway · rest = text
STATUS:    draft
---
Traffic doubled. Your one app server is at 100% CPU. You have two ways out.
And if you pick "more servers", users still type one address. Who decides which server gets each request?

What is scaling?
Scaling means giving a system more capacity so it can handle more load.

Vertical scaling (scale up): make one machine bigger. More CPU, more RAM, faster disk.
Horizontal scaling (scale out): add more machines and split the work between them.

Think of a shop with a long line. Vertical: train your one cashier to work faster. Horizontal: open more checkout counters.

Why do we need it?
Every machine has a limit. Past that limit, requests wait, time out, and users leave.

Should you scale up or scale out?
Scale up (vertical):
→ Simple. No code changes. Your app still runs on one box.
→ Has a ceiling. There is a largest machine you can buy, and big machines get expensive fast.
→ Keeps one point of failure. If that box dies, everything dies.
Scale out (horizontal):
→ No hard ceiling, and one machine dying does not take you down.
→ Needs a stateless app: no user data kept in one server's memory.
→ More parts to run.
Vertical = simple, limited, one point of failure. Horizontal = more parts, near-unlimited, survives failures.
Takeaway: scale up until it hurts; scale out when you need to survive failure.

Where is each used?
Vertical: databases like PostgreSQL often start here, because splitting data is hard.
Horizontal: web and API servers behind a load balancer, AWS Auto Scaling groups, Kubernetes adding pods.

[FACT_CHECK: PostgreSQL databases often start with vertical scaling because splitting data is hard → PostgreSQL docs (no built-in sharding) / common practice write-ups]

When to use which
Vertical: early on, or for parts that are hard to split, like a database.
Horizontal: when you need to survive a machine failure, or you have hit the biggest machine.
Most real systems do both. Scale the database up. Scale the app servers out.

[PERSONAL: one line on when you scaled up first and why it was the right call]

Why does a second server log users out?
Your API stores user sessions in server memory. You add a second server. Now half your users get logged out on each request.
Fix: move sessions to a shared store like Redis. Now any server can answer any request.
Takeaway: scaling out only works once no server keeps user state to itself.

The load balancer
You added three servers. A load balancer is a server that sits in front of your app servers. It receives every request and passes it to one healthy server behind it.
Think of a host at a busy restaurant. Guests do not pick a table. The host sends each one to a free waiter.

Why do we need it?
Without it, one server gets all the traffic while others sit idle. And if a server crashes, users keep hitting it and get errors.

How does a load balancer pass one request to a server?
1. User calls api.example.com.
2. DNS points to the load balancer.
3. It checks which servers are healthy.
4. It picks one using its rule.
5. The server replies through the load balancer.
→ Spreads traffic across servers
→ Health checks: it pings each server, and stops sending traffic to one that fails
→ Hides your servers. Users only see one address
→ Can end HTTPS (decrypt traffic) so app servers do less work
Takeaway: a load balancer turns many servers into one reliable address.

How does a load balancer pick a server?
• Round robin: take turns, 1, 2, 3, 1, 2, 3
• Least connections: send to the least busy server
• IP hash: the same user IP always goes to the same server
Layer 4 load balancer: routes by IP and port only. Fast, but blind to content.
Layer 7 load balancer: reads the HTTP request, so it can route /api and /images to different servers.
Takeaway: the rule decides who gets the next request; the layer decides what it can see.

Where is it used?
Nginx and HAProxy (software you run yourself). AWS Elastic Load Balancing, Google Cloud Load Balancing (managed). Kubernetes Services also spread traffic across pods.

When to use it / when not to
Use it: as soon as you run more than one copy of a service.
Skip it: with one server and no uptime need. It is one more moving part.

Watch out: what a load balancer adds
→ It is itself a single point of failure → one box in front of everything → run it as a pair or a managed service.
→ IP hash pins users to one server → that server dies and they lose their state → keep state in a shared store instead.

[PERSONAL: one line on a health-check or routing issue you debugged]

Keep in mind before you scale out
→ Move sessions and uploads out of server memory first.
→ Point health checks at a real endpoint, not just an open port.
→ Scale the database up while the app servers scale out.

Takeaway
Scale up until it hurts. Scale out when you need to survive failure.
A load balancer turns those many servers into one reliable address.

Next: caching and CDNs: where to cache, and when to forget.

#SystemDesign #Scalability #LoadBalancing #SoftwareArchitecture #BackendDevelopment
