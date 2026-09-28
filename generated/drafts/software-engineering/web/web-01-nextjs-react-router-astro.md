SERIES:    SOFTWARE ENGINEERING · WEB #01
TITLE:     Next.js vs React Router 7 vs Astro
PILLAR:    Software Engineering · Web — for mid-level and senior engineers choosing a web framework
LEVEL:     INTERMEDIATE
MODE:      COMPARE
FORMAT:    VISUAL
HEADLINE:  Three frameworks, three ideas of the web
LAYOUT:    COMPARE
STATUS:    draft
---
Choosing a React framework is not about syntax.
It decides where your code runs, how much JavaScript users download, and where you can deploy.

Next.js
The biggest ecosystem. React Server Components, server actions, static pages that refresh themselves (ISR).
The cost: many moving parts, especially caching. Easiest to run on Vercel; self-hosting works, but some features need extra setup.

[FACT_CHECK: Next.js 15 changed fetch/route caching defaults to uncached → Next.js 15 release notes]

React Router 7 (formerly Remix)
Each route has a loader (reads data) and an action (handles form posts).
Built on web standards: Request, Response, forms. Runs on Node, Cloudflare or other JS servers.
Simpler to reason about: data for a page is loaded in one place, per route.

[FACT_CHECK: Remix was merged into React Router v7 (framework mode) → React Router / Remix blog]

Astro
Content first. Pages ship as plain HTML with zero JavaScript by default.
Only the interactive parts load JS. These are called islands.
You can still write those islands in React, Vue or Svelte.

Same page, three outputs
A pricing page with one signup form:
→ Next.js: HTML + the React runtime + your components' JS
→ React Router 7: HTML + the React runtime + route JS
→ Astro: HTML + only the form island's JS

The trade-off
→ App-like dashboards with shared client state: Next.js or React Router 7
→ Marketing sites, docs, blogs: Astro
→ Portability across hosts and a simple data model: React Router 7
→ Server Components today and the most libraries and examples: Next.js

Common wrong choice
Astro for a SaaS dashboard. Islands do not share state easily, so you end up rebuilding app state across them.
The reverse happens too: a docs site in Next.js, then weeks spent trimming client JavaScript.

A common setup that works: Astro for the marketing site, Next.js or React Router for the app behind login.

[PERSONAL: optional — which framework I use for client apps and one reason why]

Takeaway: choose the framework by how interactive your pages are, not by popularity.

Next: SSR vs SSG vs ISR vs CSR, and why you choose per page.

#WebDevelopment #NextJS #React #Frontend
