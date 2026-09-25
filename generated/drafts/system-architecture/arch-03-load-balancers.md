SERIES:    SYSTEM ARCHITECTURE #03
TITLE:     Load Balancers: One Address, Many Servers
PILLAR:    System Design & Architecture — for juniors who want the request path, mid-levels for interviews
HEADLINE:  One address in front, many servers behind
LAYOUT:    FLOW
---
You added three servers. But users type one address. Who decides which server gets each request?

What is it?
A load balancer is a server that sits in front of your app servers. It receives every request and passes it to one healthy server behind it.

Think of a host at a busy restaurant. Guests do not pick a table. The host sends each one to a free waiter.

Why do we need it?
Without it, one server gets all the traffic while others sit idle. And if a server crashes, users keep hitting it and get errors.

Key properties
→ Spreads traffic across servers
→ Health checks: it pings each server, and stops sending traffic to one that fails
→ Hides your servers. Users only see one address
→ Can end HTTPS (decrypt traffic) so app servers do less work
→ Is itself a single point of failure, so it usually runs as a pair or a managed service

Common ways to pick a server
• Round robin: take turns, 1, 2, 3, 1, 2, 3
• Least connections: send to the least busy server
• IP hash: the same user IP always goes to the same server

Where is it used?
Nginx and HAProxy (software you run yourself). AWS Elastic Load Balancing, Google Cloud Load Balancing (managed). Kubernetes Services also spread traffic across pods.

When to use it / when not to
Use it: as soon as you run more than one copy of a service.
Skip it: with one server and no uptime need. It is one more moving part.

Steps: one request
1. User calls api.example.com.
2. DNS points to the load balancer.
3. It checks which servers are healthy.
4. It picks one using its rule.
5. The server replies through the load balancer.

Comparison
Layer 4 load balancer: routes by IP and port only. Fast, but blind to content.
Layer 7 load balancer: reads the HTTP request, so it can route /api and /images to different servers.

[PERSONAL: one line on a health-check or routing issue you debugged]

Takeaway: A load balancer turns many servers into one reliable address.

Next: caching, and why cache invalidation is famously hard.

#SystemDesign #LoadBalancing #SoftwareArchitecture #DevOps
