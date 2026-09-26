SERIES:    SYSTEM ARCHITECTURE #03
TITLE:     Latency, Throughput and Availability: The Three Numbers
PILLAR:    System Design & Architecture — for students and juniors, plus seniors who watch p99
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  How fast, how many, how often up
LAYOUT:    GRID
STATUS:    draft
---
A page takes 2 seconds to load. The server handles 500 requests a second. It was down for 9 hours last year.

Three numbers. Three different problems.

What is it?
Ask three plain questions about any system:
1. How long does one user wait?
2. How many users can it serve at once?
3. How much of the time does it work at all?

These are latency, throughput and availability.

→ Latency: time for one request, start to finish. Measured in milliseconds (ms). 1 ms = 1/1000 of a second.
→ Throughput: how much work the system finishes per second. Often requests per second (RPS).
→ Availability: the share of time the system works, as a percentage.

Think of a road. Latency is how long one car takes to cross the city. Throughput is how many cars pass per hour. Availability is how many days the road is open.

Latency vs throughput
They are not the same. A bus carries 50 people but leaves every 30 minutes. A taxi carries one person, right now. The bus wins on throughput. The taxi wins on latency. Batching work often raises throughput and raises latency too.

Availability in "nines"
A year has about 8,760 hours.
→ 99% up: about 3.65 days down per year
→ 99.9% ("three nines"): about 8.8 hours per year
→ 99.99%: about 53 minutes per year
→ 99.999%: about 5 minutes per year
Each extra nine means 10 times less downtime, and usually much more cost.

p50 and p99
An average hides slow requests. Instead, sort all response times.
→ p50 (the median): half of requests are faster than this
→ p99: 99% are faster, the slowest 1% are slower
Example: p50 = 80 ms, p99 = 1,200 ms. One request in 100 waits over a second. If one page makes 100 such calls, about 63% of page loads hit at least one slow call (1 − 0.99^100).

Where is it used?
In requirements ("p99 under 300 ms"), in SLAs (promises of uptime to customers), and on every monitoring dashboard.

When to use it / when not to
Use them: to turn "fast and reliable" into numbers you can test.
Do not chase five nines for an internal tool. Each nine costs real money.

Common mistake
Reporting only average latency. A few very slow requests disappear inside it. Fix: track p50 and p99 together.

[PERSONAL: one line on a time p99 showed a problem the average hid]

Takeaway: Latency is how long. Throughput is how many. Availability is how often it works.

Next: back-of-the-envelope estimation, sizing a photo app in five minutes.

#SystemDesign #Performance #SoftwareArchitecture #SRE
