---
title: "Size a photo app in five minutes before you design anything"
description: "Back-of-the-envelope estimation, step by step: users to requests per second, the evening peak, storage per year, and what the numbers decide."
date: 2026-11-30
series: "System Architecture"
seriesNumber: 4
slug: arch-04-back-of-the-envelope-estimation
tags: [system-design, estimation, scalability, interviews]
cover: cover.png
---

You are asked to design a photo-sharing app. 10 million people use it every day. Before drawing a single box: how big is this?

You estimate. Rough maths that fits on the back of an envelope. You want the right size, not the exact number. It takes five minutes, and it decides what the rest of the design has to handle. All numbers below are illustrative.

## Step 1: write down assumptions

![Four assumptions: 10M daily active users, 20 photo views each, 1 in 10 uploads a photo, 2 MB a photo](slide-02.png)

- **10 million daily active users:** people who open the app at least once a day.
- Each user views **20 photos** a day.
- **1 in 10** users uploads one photo a day.
- An average photo is **2 MB**.

Say them out loud. Every later step is built on them, and in an interview someone may change one.

## Step 2: requests per day

![10M users × 20 views = 200M views a day; 10M × 1/10 = 1M uploads a day](slide-03.png)

Multiply users by what each one does in a day.

- Views: 10M × 20 = **200 million** a day.
- Uploads: 10M × 1/10 = **1 million** a day.

## Step 3: requests per second

![1 day = 86,400 seconds, rounded to 100,000: 2,000 views and 10 uploads a second](slide-04.png)

People use an app per day, but servers feel it per second. A day has 86,400 seconds. Round it to 100,000, so dividing is just dropping five zeros.

- Views: 200M ÷ 100,000 = **2,000 a second** on average.
- Uploads: 1M ÷ 100,000 = **10 a second** on average.

The exact answer is 200M ÷ 86,400 ≈ 2,315 a second. Rounding makes you about 14% low, which is fine for sizing.

## Step 4: the peak

![Views a second over one day: average 2,000, evening peak 6,000; peak uploads 30 a second](slide-05.png)

Traffic is not flat. Evenings are busier. Assume the peak is 3× the average.

- Peak views: 2,000 × 3 = **6,000 a second**.
- Peak uploads: 10 × 3 = **30 a second**.

Design for the peak, not the average. This is the most common mistake: a system sized for 2,000 a second falls over every evening.

## Step 5: storage

![2 TB of photos a day, 730 TB a year; metadata only 1 GB a day](slide-06.png)

- Photos per day: 1M × 2 MB = **2 TB**.
- Photos per year: 2 TB × 365 ≈ **730 TB**, close to 1 PB (a petabyte is 1,000 TB).

**Metadata** is the small record about each photo: owner, time, caption. Say 1 KB each. 1M × 1 KB = 1 GB a day, about 365 GB a year. Small next to the photos.

## What the numbers tell you

![What the numbers decide: read-heavy, object storage for photos, one database for metadata, no sharding yet](slide-07.png)

- **200 views for every upload.** The system is read-heavy. Make reading fast first.
- **Photo files grow by hundreds of TB a year.** Keep them in object storage (a service that stores files by name, like Amazon S3), not in the database.
- **The metadata is small.** One ordinary database can hold it for a long time.
- **30 uploads a second is modest.** Writes are not the hard part here.

## What not to do first

Don't pick tools before the maths. "We need sharding" (splitting one database across many machines) means nothing until you know writes are only about 30 a second.

## Keep in mind when you estimate in an interview

- Say each assumption out loud: the interviewer may change it.
- Write the unit on every number: per day or per second, MB or TB.
- Storage counts every copy: keep 3 copies, store 3× the bytes.
- Round to one or two digits. Precision here is wasted time.

**In one line:** five minutes of rough maths tells you what to design for, and what you can ignore.

## Next in the series

Vertical vs horizontal scaling: the first choice when traffic grows.
