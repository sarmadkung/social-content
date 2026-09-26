SERIES:    SOFTWARE ENGINEERING #09
TITLE:     Good APIs Are Contracts, Not Just Endpoints
PILLAR:    Software Engineering — for developers designing APIs other people depend on
LEVEL:     INTERMEDIATE
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Your API is a promise to every client
LAYOUT:    ANATOMY
STATUS:    draft
---
You rename one JSON field from "total" to "amount". The code is cleaner. Every older mobile app now shows a total of $0.

What is it?
Once someone calls your API, every URL, field, status code and error shape is a promise. Clients write code against it, and you cannot see that code. Break the promise and they break.
This is called an API contract. Think of a wall socket: you can rewire the house, but the socket shape stays the same.

Why do we need it?
You can redeploy the server in minutes. Old app versions stay on phones for months, and a partner's client may never update. The contract is the only thing both sides share.

How does it work? Five parts of the contract
→ Resources: nouns in the URL, verbs in the HTTP method. POST /orders, not /createOrder.
→ Status codes tell the truth: 201 created, 400 bad input, 404 not found, 409 conflict. Never 200 with "error" inside.
→ One error shape everywhere: { "error": { "code": "ITEMS_REQUIRED" } }. Clients check the code, not the message text.
→ Retries are safe. GET, PUT and DELETE are idempotent; POST accepts an Idempotency-Key (#06).
→ Changes only add. A new optional field is safe. Renaming, removing or changing a type needs a new version.

Example (Express)
app.post("/orders", async (req, res) => {
  if (!req.body.items?.length)
    return res.status(400).json({ error: { code: "ITEMS_REQUIRED" } });
  const order = await createOrder(req.body, req.get("Idempotency-Key"));
  res.status(201).location(`/orders/${order.id}`).json(order);
});

Where is it used?
Stripe pins each account to a dated API version, so old integrations keep working. GitHub picks a version from the X-GitHub-Api-Version header.

When to use it / when not to
Treat any API with outside clients (mobile apps, partners, other teams) as a contract.
An endpoint used only by a frontend you deploy with it can change more freely.

Common mistake
Returning a list with no limit. It works with 50 rows and times out with 50,000. Adding a limit later breaks clients that expect everything, so set one from day one.

Takeaway: the code behind an API can change every day. The contract can't.

Next: REST vs GraphQL vs gRPC, and how to choose.

#SoftwareEngineering #APIDesign #BackendDevelopment #SystemDesign
