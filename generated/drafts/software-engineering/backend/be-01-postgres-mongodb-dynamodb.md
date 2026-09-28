SERIES:    SOFTWARE ENGINEERING · BACKEND #01
TITLE:     Postgres vs MongoDB vs DynamoDB: Choose by Access Pattern
PILLAR:    Software Engineering · Backend — for mid-level and senior engineers picking a primary database
LEVEL:     INTERMEDIATE
MODE:      COMPARE
FORMAT:    VISUAL
HEADLINE:  Pick the database your reads need
LAYOUT:    COMPARE
STATUS:    draft
---
"SQL or NoSQL?" is the wrong first question.
The right one: how will you read this data, and will that change next month?

The shared problem
All three store data safely. They differ in what they make cheap.
An access pattern is one way your app reads data, like "the last 20 orders for one customer".

Postgres
Tables, joins and transactions. Its real strength: queries you did not plan for.
A new report next month is one SQL query and maybe one index.
JSONB columns cover the semi-structured parts.

MongoDB
Documents: store together what you read together.
One order with its items and address, read in one call.
Joins ($lookup) and multi-document transactions exist, but they are not its sweet spot.

[FACT_CHECK: MongoDB supports multi-document transactions (since 4.0 on replica sets) → MongoDB transactions docs]

DynamoDB
A key-value store that stays fast at almost any scale.
You design keys around your reads before you write any code.
A read that does not match a key needs a new index (GSI) or a full table scan.

[FACT_CHECK: DynamoDB is designed for single-digit millisecond latency at any scale → AWS DynamoDB docs]

Same question, three answers
"Last 20 orders for customer 42"
→ Postgres: WHERE customer_id = 42 ORDER BY created_at DESC LIMIT 20, with an index
→ MongoDB: one query on an indexed customerId field
→ DynamoDB: PK = CUSTOMER#42, sort key = ORDER#<date>, read 20. Fastest of the three.

Now product asks: "all orders over $500 last week, across customers"
→ Postgres: one query
→ MongoDB: one query, maybe a new index
→ DynamoDB: a new GSI, a backfill, or a scan

When to pick each
→ Postgres: the default. Most products, and any product whose questions still change.
→ MongoDB: data that is naturally a document and read whole, with fields that vary a lot (catalogs, CMS content).
→ DynamoDB: access patterns known and stable, huge or spiky traffic, already deep in AWS.

Common wrong choice
DynamoDB for a v1 product "because it scales". Every new feature needs a new index, and the team spends its time on key design instead of the product.

[PERSONAL: optional — a time a database choice helped or hurt a project I worked on]

Takeaway: choose the database whose strengths match your reads, not your hype budget.

Next: Node vs Go vs Python for API services.

#BackendDevelopment #Databases #PostgreSQL #SoftwareEngineering
