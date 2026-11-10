# Project Log

Raw notes for BUILDING posts. Add one entry every two weeks per
project. Rough notes are fine: posts are drafted from these, and anything
missing becomes a `[PERSONAL: ...]` marker instead of being made up.

- **Project:** Pivot, a personal project, or a client (use a general label
  like "logistics client" unless you have permission to name them).
- Pivot and other client products are never named in a post; the entry can
  name them, because this file is never posted.
- Mark anything private with `(private)` so it never reaches a draft.

Newest entry on top. Copy the template below. A post's `SOURCE:` line is the
entry heading without the `## `, e.g. `2026-10-02 — Pivot`; keep headings
unique (add a suffix if two entries share a date and project).

---

## 2026-10-22 — Pivot

- Shipped: Pivot moved off one shared Expo codebase. Before: iOS, Android, web and desktop all shipped from one Expo codebase (shared UI, shared libs, shared packages, everything that could be shared). Now: iOS is native Swift, Android is native, web is its own web app (TanStack Start), desktop runs the web app.
- Broke (why we moved): performance bottlenecks; fixing one platform kept breaking another; UI compatibility problems across platforms; and more of the same. Real incidents from review lessons (review-pivot/lessons.yaml): safe-area-unwrap-route-hosted (thread composer lost bottom inset after a layout change), web/DOM APIs reachable on native paths, fixed-height-sheet-dynamic-type (join-call sheet clipped at large text size), minimized-call-dual-chrome-surfaces (two call control surfaces on native tablets), easignore-app-shared (excluding shared lib broke the EAS build), static-reachability-guard-false-green (reachability test missed web-only variants), eas-bootstrap-remount-ownership (OTA reload could start mid-session).
- Decided (and the options we did not pick): native where the platform matters (iOS, Android); web where it doesn't (desktop stays on the web app — fast enough). Options not picked: [to fill]
- Changed: during the move, rules in the agents' instruction file: new frontend work goes to web first; port to Expo only when Android users need it, in the same PR; any Expo fix must land in web too; no Expo-only features; iOS owner keeps native iOS in sync from main.
- Technical details:
- Numbers / results (only if safe to share):
- How AI helped (if it did): coding agents write and port features across the native apps; the sync rules live in the agents' instruction file so every session follows them.
- Learned: one codebase was a cost fix; agents make writing per platform cheap, so native is affordable again.
- Would do differently:

---

## YYYY-MM-DD — <Project>

- Shipped:
- Broke:
- Decided (and the options we did not pick):
- Changed:
- Technical details:
- Numbers / results (only if safe to share):
- How AI helped (if it did):
- Learned:
- Would do differently:
