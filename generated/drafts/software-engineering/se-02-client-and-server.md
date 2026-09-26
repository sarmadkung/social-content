SERIES:    SOFTWARE ENGINEERING #02
TITLE:     Client and Server: What Happens When Your App Calls an API
PILLAR:    Software Engineering — for students and junior developers building their first connected app
LEVEL:     BEGINNER
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Your app asks. The server answers.
LAYOUT:    FLOW
STATUS:    draft
---
You open a weather app. In under a second it shows 24°C in Lahore. Your phone did not measure that. It asked another computer.

What is it?
Your phone sends a short message: "What is the weather in Lahore?" A computer somewhere else reads it, finds the answer and sends it back.
The side that asks is the client. The side that answers is the server. The question is a request. The answer is a response.
Think of a restaurant. You order, the kitchen cooks, the waiter brings the plate. The menu lists what you are allowed to order. In software, that menu is the API (Application Programming Interface): the list of requests a server accepts and the responses it promises.

Why do we need it?
Your phone cannot store fresh weather for every city in the world. A server can. So the work is split: the client shows things and takes input, the server keeps the data and the rules. One server can then serve the iPhone app, the Android app and the website at once.

How does it work?
Client → request → Server
Client ← response ← Server

const res = await fetch("https://api.example.com/weather?city=Lahore");
const data = await res.json();
// { city: "Lahore", tempC: 24 }

Key properties
→ The client starts. The server waits and answers.
→ One request gets one response.
→ Each request carries what the server needs: the city, a login token. By default the server does not remember your last request. This is called stateless.
→ Client and server can use different languages. They only need to agree on the API.
→ A server can also be a client. The weather server may ask a weather data provider.

Where is it used?
Weather, maps, banking, chat, social feeds. Any app showing data it did not create. Also services talking to each other inside one company.

When to use it: data or rules that must be shared, kept safe or kept fresh.
When not to: things that work fully on the device, like a calculator.

Common mistake
Trusting the client. Anyone can send a request, not only your app. The server must check every request: is this user allowed, is this input valid? Hiding a button is not security.

Takeaway: the client asks, the server answers, and the API is the agreement between them.

Next: one HTTP request, step by step, from a URL to a response.

#SoftwareEngineering #WebDevelopment #BackendDevelopment #APIs
