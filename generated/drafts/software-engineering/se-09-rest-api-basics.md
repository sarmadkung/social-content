SERIES:    SOFTWARE ENGINEERING #09
TITLE:     REST API Design Basics: Resources, Verbs, Status Codes
PILLAR:    Software Engineering — for students and junior developers designing their first APIs
LEVEL:     INTERMEDIATE
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Nouns in the URL, verbs in the method
LAYOUT:    ANATOMY
STATUS:    draft
---
POST /getOrders. GET /deleteUser?id=7. A 200 OK with "error" inside the body. All common. All confusing for whoever calls your API.

What is it?
REST is a style for building web APIs around resources. A resource is a thing your app manages, like an order or a user, and each one has its own URL.
Think of a filing cabinet. Each drawer is a resource: /orders, /users. The actions are the same for every drawer: look, add, replace, change, remove.

Why do we need it?
When every API follows the same rules, a developer can guess how yours works without reading every page of docs. Tools like caches, proxies and client libraries also understand those rules.

Key properties
→ Resources are nouns: /orders and /orders/42. Not /createOrder.
→ HTTP methods are the verbs: GET reads, POST creates, PUT replaces, PATCH changes part, DELETE removes.
→ Status codes tell the result. 2xx means success, 4xx means the caller made a mistake, 5xx means the server failed.
→ The useful ones: 200 OK, 201 Created, 204 No Content, 400 Bad Request, 401 not logged in, 403 not allowed, 404 Not Found, 409 Conflict, 500 server error.
→ GET, PUT and DELETE are idempotent (#06). Clients can retry them safely.

Where is it used?
Most public web APIs, like GitHub's and Stripe's. Also the backend behind most web and mobile apps.

When to use it: resource-based data that many different clients use.
When not to: heavy real-time streaming, or when clients need very flexible queries. Other styles fit better there.

Example (Express)
app.post("/orders", async (req, res) => {
  if (!req.body.items?.length) {
    return res.status(400).json({ error: "items required" });
  }
  const order = await createOrder(req.body);
  res.status(201).location(`/orders/${order.id}`).json(order);
});

Bad input gets a 400. A new order gets a 201 and a Location header that points to it.

Comparison
PUT: send the whole resource. Anything you leave out is replaced.
PATCH: send only the fields that change.

Takeaway: nouns in the URL, verbs in the method, the truth in the status code.

Next: REST vs GraphQL vs gRPC, and how to choose.

#SoftwareEngineering #APIDesign #BackendDevelopment #WebDevelopment
