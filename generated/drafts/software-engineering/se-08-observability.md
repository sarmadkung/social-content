SERIES:    SOFTWARE ENGINEERING #08
TITLE:     Logging vs Metrics vs Traces (Observability Basics)
PILLAR:    Software Engineering — for junior and mid-level developers running code in production
LEVEL:     INTERMEDIATE
MODE:      COMPARE
FORMAT:    VISUAL
HEADLINE:  Logs, metrics, traces: three different questions
LAYOUT:    ANATOMY
STATUS:    draft
---
In production you cannot pause the code and step through it. You only see what your system chose to record.

What is it?
Observability means you can understand what your system is doing from the outside, using the data it sends out. That data comes in three types:
→ Logs: a written record of one event. "Order 123 saved."
→ Metrics: numbers measured over time. "Error rate is 2% this minute."
→ Traces: the full path of one request through your services, split into spans (one timed step each).
Think of a road trip. Metrics are the dashboard gauges. Logs are your trip diary. A trace is the GPS route showing where you stopped, and for how long.

Why do we need it?
Each one answers a different question. Metrics: "Is something wrong?" Traces: "Where is it slow or failing?" Logs: "Why did it happen?" With only one, you are guessing.

Key properties
→ Logs are detailed but costly at volume. Write them as structured JSON, not free text, so you can search them.
→ Metrics are cheap but low in detail. Avoid labels with many unique values, like user IDs (high cardinality). They get expensive fast.
→ Traces show where time goes across services. They are usually sampled, meaning only some requests are kept.
→ A trace ID in every log line links them together.

Where is it used?
OpenTelemetry (one open standard for all three), Prometheus for metrics, Jaeger for traces, Grafana Loki or Elasticsearch for logs.

When to use it: from the first deploy. Adding it during an outage is too late.
When not to: do not log secrets, passwords or personal data.

Example (a structured log line)
console.log(JSON.stringify({
  level: "error",
  msg: "payment failed",
  orderId: "o_123",
  traceId: "4bf92f3577b34da6",
}));

Steps in a real incident
1. A metric alert fires: errors are up.
2. A trace shows the slow or failing service.
3. Logs with the same trace ID explain why.

[PERSONAL: one line about an incident where one of these three signals found the cause]

Takeaway: metrics tell you something is wrong, traces tell you where, logs tell you why.

Next: REST API design basics, resources, verbs and status codes.

#SoftwareEngineering #Observability #DevOps #BackendDevelopment
