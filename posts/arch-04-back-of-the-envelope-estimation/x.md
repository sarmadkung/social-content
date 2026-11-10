Design a photo app with 10 million daily users.

Before drawing a single box: how big is it?

Five minutes of rough maths answers that. Here's the whole estimate, step by step 🧵
---
Step 1: write down assumptions.

10M daily users. Each views 20 photos a day. 1 in 10 uploads one photo. A photo is 2 MB.

Per day: 10M × 20 = 200M views. 10M × 1/10 = 1M uploads.
---
Step 2: per second. A day has 86,400 seconds. Round it to 100,000.

200M ÷ 100,000 = 2,000 views/s.
1M ÷ 100,000 = 10 uploads/s.

About 14% low. Fine for sizing.
---
Step 3: design for the peak. Evenings are busier. Assume 3× the average:

6,000 views/s and 30 uploads/s.

A system sized for 2,000/s falls over every evening.
---
Step 4: storage. 1M × 2 MB = 2 TB a day, about 730 TB a year. The metadata is only 1 GB a day.

So: make reads fast, keep photos in object storage, and skip sharding for now. 30 writes/s is modest.
---
Rough maths tells you what to design for, and what you can ignore.

Next: vertical vs horizontal scaling, the first choice when traffic grows.

#SystemDesign
