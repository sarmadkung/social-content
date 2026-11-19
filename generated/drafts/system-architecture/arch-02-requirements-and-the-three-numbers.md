SERIES:    SYSTEM ARCHITECTURE #02
TITLE:     Requirements First: What It Must Do, How Well, and the Three Numbers
PILLAR:    System Design & Architecture — for students and juniors, mid-levels starting interview practice, and seniors who watch p99
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  First what it does, then how well
LAYOUT:    COMPARE
VISUALS:   1 = What must it do, and how well? · 2 = What are latency, throughput and availability? · 3 = How much downtime does each "nine" allow? · 4 = Why track p99, not the average? · 5 = Takeaway · rest = text
STATUS:    draft
---
Two teams build a food delivery app with the same features. One gets 100 orders a day. The other gets 100,000 orders an hour. They end up with very different systems.

The features did not decide the design. The "how well" did.

What is it?
Before drawing any boxes, write two lists.

List 1: what the system must do. "A user can order food." "A rider can see the pickup address."
List 2: how well it must do it. "The menu loads in under 1 second." "Ordering still works if one server dies."

List 1 is called functional requirements. List 2 is non-functional requirements, also called quality attributes.

Think of hiring a builder. "Three bedrooms and a kitchen" is functional. "Must survive an earthquake and stay within budget" is non-functional. Same rooms, very different building.

Why do we need it?
Without list 2, every design looks fine. One small server can "take orders". The real question is: 10 a minute or 10,000? And what happens when it fails?

What must it do, and how well?
Example: food delivery app
Functional:
→ Browse restaurants and menus
→ Place and pay for an order
→ Track the rider on a map
Non-functional:
→ Latency: menu loads in under 1 second
→ Availability: ordering works 99.9% of the time
→ Scale: 50,000 orders in the dinner hour (illustrative)
→ Correctness: a paid order is never lost or charged twice
→ Cost: fits the team's cloud budget
Takeaway: features decide the APIs; the "how well" list decides the architecture.

Key properties
→ Functional requirements decide the features and the APIs
→ Non-functional requirements decide the architecture
→ They need numbers. "Fast" is not a requirement. "Under 200 ms" is
→ They conflict. More uptime costs money. Safer data can cost speed

Common mistake
Saying "we need microservices and Kafka" before asking how many users there are. Fix: ask for the numbers first. They often show a simple design is enough.

[PERSONAL: one line on a project where a missing non-functional requirement forced a redesign]

The three numbers behind "how well"
A page takes 2 seconds to load. The server handles 500 requests a second. It was down for 9 hours last year.
Three numbers. Three different problems.

What are latency, throughput and availability?
Ask three plain questions about any system:
1. How long does one user wait?
2. How many users can it serve at once?
3. How much of the time does it work at all?
→ Latency: time for one request, start to finish. Measured in milliseconds (ms). 1 ms = 1/1000 of a second.
→ Throughput: how much work the system finishes per second. Often requests per second (RPS).
→ Availability: the share of time the system works, as a percentage.
Think of a road. Latency is how long one car takes to cross the city. Throughput is how many cars pass per hour. Availability is how many days the road is open.
Takeaway: latency is how long, throughput is how many, availability is how often it works.

Latency vs throughput
They are not the same. A bus carries 50 people but leaves every 30 minutes. A taxi carries one person, right now. The bus wins on throughput. The taxi wins on latency. Batching work often raises throughput and raises latency too.

How much downtime does each "nine" allow?
A year has about 8,760 hours.
→ 99% up: about 3.65 days down per year
→ 99.9% ("three nines"): about 8.8 hours per year
→ 99.99%: about 53 minutes per year
→ 99.999%: about 5 minutes per year
Each extra nine means 10 times less downtime, and usually much more cost.
Takeaway: every extra nine cuts downtime 10× and costs real money, so pick the one you need.

[FACT_CHECK: Downtime per year: 99% ≈ 3.65 days, 99.9% ≈ 8.8 hours, 99.99% ≈ 53 minutes, 99.999% ≈ 5 minutes → an SLA/uptime calculator (e.g. uptime.is)]

Why track p99, not the average?
An average hides slow requests. Instead, sort all response times.
→ p50 (the median): half of requests are faster than this
→ p99: 99% are faster, the slowest 1% are slower
Example: p50 = 80 ms, p99 = 1,200 ms. One request in 100 waits over a second. If one page makes 100 such calls, about 63% of page loads hit at least one slow call (1 − 0.99^100).
Takeaway: the average hides the slow 1%, and at scale most users meet it.

Common mistake
Reporting only average latency. A few very slow requests disappear inside it. Fix: track p50 and p99 together.

[PERSONAL: one line on a time p99 showed a problem the average hid]

Where is it used?
Design docs, product specs, and the first five minutes of every system design interview. The three numbers show up in requirements ("p99 under 300 ms"), in SLAs (promises of uptime to customers), and on every monitoring dashboard.

When to use it / when not to
Use it: before any design, even a small one, to turn "fast and reliable" into numbers you can test.
Do not overdo it: a weekend prototype needs a few lines, not a long spec. And do not chase five nines for an internal tool. Each nine costs real money.

Keep in mind when you write requirements
→ Give every "how well" a number and a unit: ms, RPS, %.
→ Write latency as p50 and p99, never just an average.
→ Ask which requirement wins when two conflict, before you design.
→ Match the nines to the cost of downtime, not to pride.

Takeaway
Functional says what the system does. Non-functional says how well, in three numbers: how long, how many, how often up.
The second list shapes the design.

Next: back-of-the-envelope estimation, sizing a photo app in five minutes.

#SystemDesign #SoftwareArchitecture #Requirements #Performance #SRE
