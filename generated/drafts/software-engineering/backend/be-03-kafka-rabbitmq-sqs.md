SERIES:    SOFTWARE ENGINEERING · BACKEND #03
TITLE:     Kafka vs RabbitMQ vs SQS
PILLAR:    Software Engineering · Backend — for mid-level and senior engineers adding async messaging
LEVEL:     INTERMEDIATE
MODE:      COMPARE
FORMAT:    VISUAL
HEADLINE:  A queue forgets. A log remembers.
LAYOUT:    COMPARE
STATUS:    draft
---
You need to hand work from one service to another without making the user wait.
Three popular choices. They look alike, but two of them are queues and one is a log.

The key difference
A queue deletes a message once a consumer confirms it handled it. Work gets done, then it is gone.
A log keeps every message for a set time. Each reader tracks its own position and can go back and read again (replay).

RabbitMQ (queue)
Rich routing: send one message to many queues by rules (exchanges, topics).
Low latency, per-message acknowledgements, dead-letter queues.
You run it yourself or pay for a managed version.

Amazon SQS (queue)
Fully managed. No servers, scales on its own, pay per request.
Standard queues: huge throughput, but order is best effort and a message can arrive twice.
FIFO queues: strict order per group, lower throughput limits.

[FACT_CHECK: SQS standard = at-least-once, best-effort ordering; FIFO = ordered per message group, lower throughput quota → AWS SQS docs]

Apache Kafka (log)
Messages are kept for days or weeks. Many teams can read the same stream, each at its own pace.
Order is kept within a partition (one slice of a topic).
Very high throughput, but more to operate: partitions, consumer lag, rebalancing.

Picture it
Queue: order placed → [ email job ] → worker sends it → message deleted
Log:   order placed → [ event #1041 ] → billing reads it
                                     → analytics reads it
                                     → a new service next month replays from #1

When to pick each
→ SQS: background jobs on AWS, and you want zero ops
→ RabbitMQ: complex routing, low latency, or you are not on AWS
→ Kafka: events that many services consume, replay, stream processing, very high volume

The rule all three share
In normal use, each gives at-least-once delivery. A message can be handled twice. Make consumers idempotent: handling it twice must equal handling it once (store a processed message ID, use upserts).

[FACT_CHECK: Kafka exactly-once applies within Kafka transactions, not to external side effects like emails → Kafka docs on exactly-once semantics]

Common wrong choice
Kafka as a job queue for 50 jobs a minute. You take on partitions and consumer lag, and you still build per-message retries and dead-lettering yourself.

Takeaway: need work done once? Use a queue. Need a history many readers can replay? Use a log.

Next: Redis caching done right.

#BackendDevelopment #Kafka #DistributedSystems #SoftwareArchitecture
