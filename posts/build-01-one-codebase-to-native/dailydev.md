TITLE: We split one cross-platform codebase into native apps. Here's why.
COVER: cover.png
---
We shipped iOS, Android, web and desktop from one Expo codebase: shared UI, shared libraries, shared packages. It gave us one team and every platform at once. It also took performance, native feel, and the safety of fixing one platform without breaking another.

What that looked like day to day:

- **Fixing one platform broke another.** One browser-only line in a shared config crashed every iOS and Android launch. The tests passed, because the test environment pretends to be a browser.
- **UI that never quite fit.** A fixed-height sheet cut off its own buttons at larger text sizes. On tablets, a minimized call showed two sets of controls at once.

So we split it: iOS in Swift and SwiftUI, Android in Kotlin and Compose, web as its own app, and desktop on the web app in a native window.

**Who keeps the apps in sync?** Coding agents port every feature and fix, following rules in the agents' instruction file. **Shared fixtures check the ports:** routes, server messages and strings are pinned once, and every app's tests read them. Skip a port and CI fails.

Every gain kept, every loss won back. The price moved to us: more review, more releases, more fixtures to keep.
