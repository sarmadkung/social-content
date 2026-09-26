SERIES:    SYSTEM ARCHITECTURE #05
TITLE:     The Simplest System That Works: Client, Server, Database
PILLAR:    System Design & Architecture — for students and juniors who want the starting picture
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Every big system started as three boxes
LAYOUT:    FLOW
STATUS:    draft
---
Load balancers, caches, queues, shards. Big systems have many parts. But almost every one started as three boxes.

What is it?
A user taps "Order" in an app. Three things happen:
1. The app sends a message over the internet: "save this order".
2. A program on another computer checks it and decides what to do.
3. That program stores the order somewhere safe, and replies "done".

Those three parts are the client, the server and the database.

→ Client: the thing the user touches. A browser, a phone app.
→ Server: a computer running your code. It holds the business logic (the rules of your app).
→ Database: where data is stored for good, even after a restart.

Client → HTTP request → Server → SQL query → Database
Client ← JSON response ← Server ← rows ← Database

Think of a restaurant. The customer (client) orders from the waiter. The kitchen (server) cooks. The storeroom (database) holds the ingredients.

Why start here?
It is cheap, easy to debug, and has one source of truth. Everything later in this series is a fix for one place where this picture breaks.

Key properties
→ The client never talks to the database directly. The server checks every request first
→ The server does the work. The database remembers
→ Keep data in the database, not in server memory. Then you can add servers later

How far does it go?
Further than most people think. An illustrative example: each request uses 10 ms of CPU. One CPU core handles about 100 requests a second. An 8-core server handles about 800 a second. That is over 60 million requests a day, in theory.

Where it breaks
→ The server's CPU fills up
→ The database slows down under too many reads or writes
→ The server dies, and the whole app goes down with it

When to use it / when not to
Use it: for almost every new product.
Do not start with 20 services "for scale" you do not have yet.

Common mistake
Saving uploaded files or user sessions on the server's own disk or memory. It works with one server. With two, users see missing files and get logged out. Fix: keep state in the database or shared storage.

[PERSONAL: one line on how far a simple three-box setup carried a real product]

Takeaway: Start with client, server, database. Add parts only where it breaks.

Next: vertical vs horizontal scaling, the first choice when this setup runs out of room.

#SystemDesign #SoftwareArchitecture #BackendDevelopment #WebDevelopment
