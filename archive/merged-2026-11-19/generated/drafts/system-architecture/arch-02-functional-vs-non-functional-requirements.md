SERIES:    SYSTEM ARCHITECTURE #02
TITLE:     Requirements First: Functional vs Non-Functional
PILLAR:    System Design & Architecture — for students and juniors, plus mid-levels starting interview practice
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  First what it does, then how well
LAYOUT:    COMPARE
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

Example: food delivery app
Functional:
→ Browse restaurants and menus
→ Place and pay for an order
→ Track the rider on a map

Non-functional:
→ Latency: menu loads in under 1 second (latency = how long one request takes)
→ Availability: ordering works 99.9% of the time (availability = share of time the system is up)
→ Scale: 50,000 orders in the dinner hour (illustrative)
→ Correctness: a paid order is never lost or charged twice
→ Cost: fits the team's cloud budget

Key properties
→ Functional requirements decide the features and the APIs
→ Non-functional requirements decide the architecture
→ They need numbers. "Fast" is not a requirement. "Under 200 ms" is
→ They conflict. More uptime costs money. Safer data can cost speed

Where is it used?
Design docs, product specs, and the first five minutes of every system design interview.

When to use it / when not to
Use it: before any design, even a small one.
Do not overdo it: a weekend prototype needs a few lines, not a long spec.

Common mistake
Saying "we need microservices and Kafka" before asking how many users there are. Fix: ask for the numbers first. They often show a simple design is enough.

[PERSONAL: one line on a project where a missing non-functional requirement forced a redesign]

Takeaway: Functional says what the system does. Non-functional says how well. The second list shapes the design.

Next: latency, throughput and availability, the three numbers behind "how well".

#SystemDesign #SoftwareArchitecture #Requirements #SoftwareEngineering
