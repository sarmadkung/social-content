SERIES:    SOFTWARE ENGINEERING #08
TITLE:     REST vs GraphQL vs gRPC — three answers to different questions
PILLAR:    Software Engineering — for juniors choosing their first API style and mid-levels defending the choice in review
LEVEL:     INTERMEDIATE
HEADLINE:  Choose who absorbs the change
LAYOUT:    COMPARE
STATUS:    draft
VARIANT:   D (flow + points)
---
Every API argument I have sat through was really an argument about coupling.

What is it?
Three ways for one program to ask another program for something.

REST — resources and HTTP verbs. GET /orders/42. The server decides the shape of the response. Cacheable by any proxy on the way, because the URL is the identity.

GraphQL — one endpoint, and the client sends the query. Ask for exactly the three fields you need, across two resources, in one round trip. The server stops guessing what the client wants.

gRPC — a typed contract in a .proto file, binary over HTTP/2. Both sides generate code from the same schema. Fastest on the wire, and streaming is native rather than bolted on.

Why do we need three?
Because they move the cost to different places.

REST pushes work onto the client: three screens need three different shapes, so you either over-fetch or you add three endpoints. GraphQL pushes it onto the server: now you own query cost, depth limits and the N+1 problem. gRPC pushes it onto tooling: regenerate on every schema change, and you cannot open it in a browser tab.

Key properties
→ REST: cacheable, debuggable with curl, over-fetches
→ GraphQL: one round trip, client-driven, caching is now your problem
→ gRPC: fastest, typed end to end, needs codegen and a proxy for browsers

How to choose
Public API for people you have never met — REST. Mobile client on a bad network with many screens — GraphQL. Service-to-service inside your own cluster — gRPC.

The mistake I see most is picking GraphQL for a backend nobody else consumes, and inheriting the query-cost problem for free.

Which one are you running in production, and would you pick it again?
