> ⚠ NOT READY — resolve these, then delete this block:
> - [FACT_CHECK: Common rule: peak traffic ≈ 2 to 3 times the average → system design estimation references (e.g. Alex Xu, System Design Interview, back-of-the-envelope chapter)]
> - [PERSONAL: one line on an estimate that changed a real design decision]

---

You are asked to design a photo-sharing app.
10 million people use it every day.
Before drawing a single box: how big is this?

Most people jump to tools. Load balancers, caches, "we'll need sharding".
But you can't pick tools until you know the size of the problem.

Five minutes of rough maths answers that. The slides walk through it, one step each:

1. Write down your assumptions
2. Requests per day
3. Requests per second (divide by 100,000, not 86,400)
4. Design for the peak, not the average
5. Storage per year
6. What the numbers decide

The result: about 6,000 views a second at peak, 30 uploads a second, and 730 TB of new photos a year.
So reads and photo storage are the hard parts. Writes are not, and sharding can wait.

Rough maths tells you what to design for, and what you can ignore.

What number do you estimate first?

#SystemDesign #SoftwareArchitecture #SystemDesignInterview #Scalability
