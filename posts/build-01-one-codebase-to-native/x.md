We shipped iOS, Android, web and desktop from one codebase.

Then we took it apart and went native.

Cross-platform gave us a lot. It also took a lot.
[images: 0, 1, 2]
---
It gave us one codebase, one team, every platform at once.

It took performance, native feel, and the safety of fixing one platform without breaking another. One browser-only line in a shared config crashed every iOS and Android launch.
---
Now: iOS in Swift and SwiftUI, Android in Kotlin and Compose. Web is its own app. Desktop runs the web app in a native window, because it is fast enough there.

Native where the platform matters. Web where it doesn't.
[images: 3]
---
The scary part was sync. The framework kept the apps in sync because there was only one copy of the code.

Now coding agents port every feature and fix, following rules in one file. Shared tests check the ports: skip one and CI goes red.
[images: 4]
---
Every gain kept. Every loss won back.

The price moved from our users to us: more review, more releases, more tests to keep.

Where else is cross-platform dead now, and where does it still win?
[images: 5, 6, 7]
