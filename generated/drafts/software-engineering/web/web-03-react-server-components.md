SERIES:    SOFTWARE ENGINEERING · WEB #03
TITLE:     React Server Components: What Actually Runs Where
PILLAR:    Software Engineering · Web — for mid-level and senior React engineers
LEVEL:     ADVANCED
MODE:      WHY
FORMAT:    VISUAL
HEADLINE:  "use client" is a boundary, not a label
LAYOUT:    ANATOMY
STATUS:    draft
---
Your blog page imports a big markdown library, say 200 KB.
With Server Components, users download none of it. Add "use client" in the wrong file, and they download all of it.

The plain question
In a Server Components app, where does each component run, and what reaches the browser?

The reason, step by step
1. Server Components (the default) run only on the server. They can await the database directly. Their code never ships to the browser.
2. The server sends their output, not their code: a description of the UI tree that React merges on the page.
3. A file that starts with "use client" is a Client Component. It is still rendered to HTML on the server first, then its JS ships and it becomes interactive in the browser (hydration).
4. "use client" marks a boundary. Everything that file imports becomes client code too.

Proof, in code
// page.tsx: server, runs once, ships no JS
export default async function Page() {
  const post = await db.post.find(1);
  return <Tabs><Markdown text={post.body} /></Tabs>;
}

// Tabs.tsx: client, only the tab switching ships
"use client";
export function Tabs({ children }) { /* useState */ }

Markdown is passed as children, so it stays a Server Component, even inside a client one.

What goes wrong if you ignore it
→ "use client" at the top of a layout: the whole subtree and its imports ship to the browser
→ Passing a function or a class instance as a prop from server to client: it cannot be sent over the wire, so it fails
→ Importing database or secret code into a client file: it can end up in the bundle. Add import "server-only" to make that a build error.

[FACT_CHECK: importing a module that imports "server-only" into a Client Component fails the build → React / Next.js docs on server-only]

A common myth
"Server Components are just SSR." They are not. SSR turns components into HTML once. Server Components decide which code ever leaves the server. Client Components still get SSR.

Takeaway: "use client" is a boundary. Push it down to the smallest interactive leaf.

Next: TanStack Query vs Redux Toolkit vs Zustand.

#React #NextJS #WebDevelopment #Frontend
