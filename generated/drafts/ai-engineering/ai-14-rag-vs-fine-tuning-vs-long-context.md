SERIES:    AI ENGINEERING #14
TITLE:     RAG vs Fine-Tuning vs Long Context
PILLAR:    AI Engineering — for engineers choosing how to add knowledge to an LLM app
LEVEL:     ADVANCED
MODE:      COMPARE
FORMAT:    VISUAL
HEADLINE:  RAG for facts, fine-tuning for behaviour
LAYOUT:    STATEMENT
STATUS:    draft
---
"Should we fine-tune the model on our docs?" Usually, no. There are three ways to get knowledge into an LLM app, and they solve different problems.

What are they?
RAG (#11): search your documents at question time and put the relevant parts in the prompt.
Fine-tuning: train an existing model further on your own examples. Its weights (the numbers it learned) change.
Long context: put all the source text straight into the prompt.

Think of a new employee. RAG is a searchable handbook. Fine-tuning is weeks of training on how your team works. Long context is handing them the whole binder for every question.

Why does the choice matter?
Fine-tune to add facts, and the facts go stale the day a document changes. Put everything in the prompt, and every request gets slower and costs more.

Key properties
→ RAG: fresh data, cited sources, per-user access checks at search time. Quality depends on retrieval.
→ Fine-tuning: shapes tone, format and narrow tasks. Needs good examples. Any change means training again.
→ Long context: nothing to build. Cost and latency grow with every token, on every request. Models can miss details buried in long inputs.

When to use which
RAG: facts are large, private or change often.
Fine-tuning: you need a behaviour or format that prompting cannot hold, or a smaller model doing one job well.
Long context: the material is small and must be seen whole, like reviewing one contract.

In one line each
RAG changes what the model sees.
Fine-tuning changes how the model behaves.
Long context changes how much it sees.

Senior detail: access control is the quiet reason to prefer RAG. With retrieval, you can filter chunks by what each user may see. Facts trained into weights have no such filter.

These are not rivals. Many systems combine them. Try prompting and RAG first. Fine-tune last, once your evals show a gap they cannot close.

Takeaway: RAG for knowledge, fine-tuning for behaviour, long context for small sets you need whole.

Next: agent vs workflow. Before you build an "agent", check if a workflow does the job.

#AIEngineering #RAG #FineTuning #LLM
