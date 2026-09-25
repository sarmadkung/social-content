SERIES:    SYSTEM ARCHITECTURE #05
TITLE:     CDNs: Moving Content Closer to Users
PILLAR:    System Design & Architecture — for students and juniors, plus mid-levels for interviews
HEADLINE:  Distance is latency. CDNs remove distance.
LAYOUT:    FLOW
---
Your server is in Virginia. A user in Karachi loads your site. Every image crosses the planet, and they wait.

What is it?
A CDN (Content Delivery Network) is a group of servers spread around the world. Each one keeps copies of your files, and each user is served from the nearest one.

Think of a store chain. You do not ship every order from one central warehouse. You stock local branches, so customers buy nearby.

Why do we need it?
Data cannot travel faster than light, and real networks are slower. Far users see higher latency (the delay before a response). One origin server (your main server) also gets overloaded by every download.

Key properties
→ Edge servers: CDN servers placed close to users, in many cities
→ Caches static files: images, video, CSS, JavaScript
→ Offloads your origin: most requests never reach your server
→ Absorbs traffic spikes, and many CDNs also help block DDoS attacks (floods of fake traffic)
→ Uses TTLs and cache headers to decide how long files stay

Where is it used?
Cloudflare, Akamai, Amazon CloudFront, Fastly. Netflix runs its own CDN, Open Connect, to deliver video.

When to use it / when not to
Use it: public files that many users download, or users spread across countries.
Less useful: private, per-user data that changes on every request.

Steps: one image request
1. User requests logo.png.
2. DNS sends them to the nearest edge server.
3. Edge has it (cache hit)? Return it right away.
4. No (cache miss)? Fetch it from the origin once.
5. Store it at the edge. The next nearby user gets it fast.

Comparison
CDN vs app cache like Redis:
A CDN caches whole files near users.
Redis caches data near your servers.
They solve different distances.

A common trap: you deploy a new app.js, but users still get the old one from the edge. Fix it with file names that include a version or hash, like app.3f9a.js.

[PERSONAL: one line on a CDN caching issue or win from a real project]

Takeaway: A CDN is a cache that lives near your users, not near your servers.

Next: database replication, and how read replicas share the load.

#SystemDesign #CDN #WebPerformance #SoftwareArchitecture
