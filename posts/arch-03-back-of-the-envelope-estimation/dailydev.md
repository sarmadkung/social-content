TITLE: Size a photo app in five minutes before you design anything
COVER: cover.png
---
You are asked to design a photo-sharing app with 10 million daily users. Before drawing a single box, estimate how big it is. You want the right size, not the exact number. All numbers here are illustrative.

- **Write down assumptions.** 10M daily active users, 20 photo views each, 1 in 10 uploads one photo a day, 2 MB a photo.
- **Per day.** 10M × 20 = 200M views. 10M × 1/10 = 1M uploads.
- **Per second: divide by 100,000, not 86,400.** 200M ÷ 100,000 = 2,000 views/s, 1M ÷ 100,000 = 10 uploads/s. The exact answer is about 2,315/s, so you are about 14% low. Fine for sizing.
- **Design for the peak.** Traffic is not flat; evenings are busier. Assume 3× the average: 6,000 views/s and 30 uploads/s. A system sized for 2,000/s falls over every evening.
- **Storage.** 1M × 2 MB = 2 TB of photos a day, about 730 TB a year. Metadata (owner, time, caption) at 1 KB each is only 1 GB a day.

**What the numbers decide:** 200 views per upload means read-heavy, so make reads fast first. Photo files go in object storage (like Amazon S3), not the database. One ordinary database holds the metadata for a long time. 30 writes a second is modest: no sharding yet.

Five minutes of rough maths tells you what to design for, and what you can ignore.
