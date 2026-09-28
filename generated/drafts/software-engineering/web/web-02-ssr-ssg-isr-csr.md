SERIES:    SOFTWARE ENGINEERING · WEB #02
TITLE:     SSR vs SSG vs ISR vs CSR: Choose per Page, Not per App
PILLAR:    Software Engineering · Web — for mid-level and senior engineers tuning page speed and server cost
LEVEL:     INTERMEDIATE
MODE:      COMPARE
FORMAT:    VISUAL
HEADLINE:  Rendering is a per-page decision
LAYOUT:    GRID
STATUS:    draft
---
One e-commerce app. Four pages. Four different right answers.
Teams that pick one rendering mode for the whole app pay for it in speed or in server bills.

The four modes
CSR (client-side rendering): the browser downloads JS, then fetches data, then draws. Slow first paint, weak SEO.
SSR (server-side rendering): the server builds HTML on every request. Always fresh, but every visit costs server time.
SSG (static site generation): HTML is built once at deploy and served from a CDN. Fastest and cheapest, stale until the next build.
ISR (incremental static regeneration): static, but rebuilt in the background after N seconds or on demand.

The two questions for each page
1. Who sees it? Everyone the same, or each user something different?
2. How fresh must it be? Per deploy, per hour, or per request?

Map the pages
→ About / pricing: same for all, changes weekly → SSG
→ Product page (10k products, price changes hourly) → ISR, revalidate every hour, or on demand when a price changes
→ Search results: depend on the query → SSR
→ Account dashboard: private, behind login → CSR or SSR, no SEO needed

In Next.js (App Router), this is one line per route:
export const revalidate = 3600;          // ISR: rebuild at most hourly
export const dynamic = "force-dynamic";  // SSR: render every request

[FACT_CHECK: route segment config `revalidate` and `dynamic = "force-dynamic"` → Next.js route segment config docs]

The hidden costs
→ SSR: page speed (time to first byte) is as slow as your slowest data call
→ SSG: build time grows with page count; 100k pages is a long deploy
→ ISR: one visitor may see the old version while the new one builds
→ CSR: users on slow phones stare at a spinner

Common mistake
Reading cookies or headers in a shared layout. In Next.js this turns every page under it into SSR, including pages meant to be static. Your CDN hit rate drops and nobody notices why.

[FACT_CHECK: using cookies()/headers() opts the route into dynamic rendering in Next.js App Router → Next.js dynamic APIs docs]

Takeaway: decide rendering per page, by who sees it and how fresh it must be.

Next: React Server Components, and what actually runs where.

#WebDevelopment #NextJS #WebPerformance #Frontend
