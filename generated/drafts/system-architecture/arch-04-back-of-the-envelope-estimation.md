SERIES:    SYSTEM ARCHITECTURE #04
TITLE:     Back-of-the-Envelope Estimation: A Photo App in Five Minutes
PILLAR:    System Design & Architecture — for mid-levels preparing for interviews, juniors learning to size systems
LEVEL:     INTERMEDIATE
MODE:      SCENARIO
FORMAT:    VISUAL
HEADLINE:  Five minutes of maths before any design
LAYOUT:    FLOW
STATUS:    draft
---
You are asked to design a photo-sharing app. 10 million people use it every day. Before drawing a single box: how big is this?

What would you do?
Estimate. Rough maths that fits on the back of an envelope. You want the right size, not the exact number. All numbers below are illustrative.

Step 1: write down assumptions
→ 10 million daily active users (people who open the app each day)
→ Each user views 20 photos a day
→ 1 in 10 users uploads 1 photo a day
→ An average photo is 2 MB

Step 2: requests per day
Views: 10M × 20 = 200 million a day.
Uploads: 10M × 1/10 = 1 million a day.

Step 3: requests per second
A day has 86,400 seconds. Round it to 100,000. The maths gets easy. Your answer comes out about 14% low, which is fine for sizing.
Views: 200M ÷ 100,000 = 2,000 per second on average.
Uploads: 1M ÷ 100,000 = 10 per second on average.

Step 4: the peak
Traffic is not flat. Evenings are busier. A common rule is peak ≈ 2 to 3 times the average. Take 3×.
Peak views: about 6,000 per second.
Peak uploads: about 30 per second.
Design for the peak, not the average.

Step 5: storage
Per day: 1M photos × 2 MB = 2 TB.
Per year: 2 TB × 365 ≈ 730 TB, close to 1 PB (petabyte = 1,000 TB).
The data about each photo (owner, time, caption) is maybe 1 KB. 1M × 1 KB = 1 GB a day. Small.

What the numbers tell you
→ 200 views for every upload. This system is read-heavy. Make reading fast first.
→ Photo files grow by hundreds of TB a year. Keep them in object storage (like Amazon S3), not in the database.
→ The metadata is small. One ordinary database can hold it for a long time.
→ 30 uploads a second is modest. Writes are not the hard part here.

What I would NOT do first
Pick tools before the maths. "We need sharding" means nothing until you know writes are only about 30 a second.

Common mistake
Designing for the average. At 3× peak, a system sized for 2,000 a second falls over every evening.

[PERSONAL: one line on an estimate that changed a real design decision]

Takeaway: Five minutes of rough maths tells you what to design for, and what you can ignore.

Next: vertical vs horizontal scaling, the first choice when traffic grows.

#SystemDesign #SoftwareArchitecture #SystemDesignInterview #Scalability
