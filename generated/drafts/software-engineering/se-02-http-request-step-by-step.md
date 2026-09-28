SERIES:    SOFTWARE ENGINEERING #02
TITLE:     One HTTP Request, Step by Step (DNS, Connection, Request, Response)
PILLAR:    Software Engineering — for students and junior developers who call APIs every day
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  What happens inside one API call
LAYOUT:    CAROUSEL
SLIDES:
  02 · FLOW · The arrow hides five steps · fetch() → DNS → TCP → TLS → request → response, five numbered boxes in one row
  03 · ANATOMY · DNS turns a name into a number · api.example.com → 203.0.113.7, with a "cached" tag on the repeat lookup
  04 · FLOW · TCP costs one round trip · client ⇄ server arrows, one round trip labelled 50 ms
  05 · COMPARE · TLS: one round trip, or two · TLS 1.3 = 1 round trip vs TLS 1.2 = 2, certificate check marked
  06 · ANATOMY · The request and the response · the GET text and the 200 OK text, method, path, headers and status labelled
  07 · STAT · New call 150 ms, reused 50 ms · timing bars: TCP 50 + TLS 50 + request 50 vs a reused connection at 50
  08 · END · Five steps, and any of them can stall
STATUS:    draft
---
You call fetch("https://api.example.com/weather"). A moment later you have JSON. Five things happened in between.

Request goes out, response comes back. That arrow hides five steps, and each one can be slow or fail.

1. DNS lookup
Your code knows a name, api.example.com. The network needs a number, an IP address like 203.0.113.7. DNS (Domain Name System) is the internet's phone book: it turns names into addresses. Answers are cached, so repeat lookups are fast.

2. TCP connection
Client and server open a connection. TCP is the set of rules that makes bytes arrive complete and in order. Opening it costs one round trip: a message there and a reply back.

3. TLS handshake
The "s" in https. TLS encrypts the traffic and uses a certificate to prove the server really is api.example.com. One more round trip with TLS 1.3, two with the older TLS 1.2.

[FACT_CHECK: TLS 1.3 full handshake takes one round trip, TLS 1.2 takes two → RFC 8446 §1.2 and §2 (and RFC 5246 handshake flow)]

4. The request
GET /weather?city=Lahore HTTP/1.1
Host: api.example.com
Accept: application/json
→ Method: what you want. GET reads, POST sends new data.
→ Path: which thing you want.
→ Headers: extra "key: value" details, like the format you accept.
→ Body: data you send. GET usually has none. POST usually carries JSON.

5. The response
HTTP/1.1 200 OK
Content-Type: application/json
{"city":"Lahore","tempC":24}
→ Status code: a number for the result. 2xx success, 4xx the client made a mistake, 5xx the server failed.
→ Headers, then the body with the data.

The numbers
Say one round trip takes 50 ms. A brand-new HTTPS call pays TCP (50) + TLS 1.3 (50) + request and response (50) = about 150 ms, plus DNS. A reused connection skips steps 1 to 3 and pays only 50.

Where is it used?
Every browser page load, every mobile app call, fetch, axios. Run curl -v on any URL to watch these steps.

Common mistake
Opening a new connection for every call. You pay steps 1 to 3 each time. Reuse one HTTP client so connections stay open (keep-alive).

Every step can be slow or fail
→ DNS cannot find the name.
→ The connection hangs because the server is down or overloaded.
→ The connection opens, then the server takes 30 seconds to answer.
Waiting to connect and waiting for an answer are different problems. Each needs its own limit.

Takeaway: one "simple" API call is five steps, and any of them can stall.

Next: timeouts, connect timeout vs read timeout, and why every network call needs one.

#SoftwareEngineering #WebDevelopment #Networking #BackendDevelopment
