SERIES:    SOFTWARE ENGINEERING · MOBILE #01
TITLE:     React Native vs Flutter vs Native Swift and Kotlin
PILLAR:    Software Engineering · Mobile — for mid-level and senior engineers choosing a mobile stack
LEVEL:     INTERMEDIATE
MODE:      COMPARE
FORMAT:    VISUAL
HEADLINE:  Who draws the pixels decides everything
LAYOUT:    COMPARE
STATUS:    draft
---
Two platforms. One team. A deadline.
The real difference between these stacks is who draws the pixels on screen.

React Native
You write TypeScript. React Native renders real native iOS and Android views.
The New Architecture (JSI, Fabric) replaced the old async bridge, so JS can call native code directly.
Big win: shared code, and developers, with your React web app.

[FACT_CHECK: New Architecture is enabled by default since React Native 0.76 → React Native blog]

Flutter
You write Dart. Flutter draws every pixel itself with its own rendering engine.
Pixel-identical UI on both platforms, and very smooth custom animation.
The cost: native look and feel is imitated, not inherited, and the Dart hiring pool is smaller.

[FACT_CHECK: Flutter renders with its own engine (Impeller, default on iOS) rather than platform UI widgets → Flutter docs]

Native (Swift / SwiftUI, Kotlin / Jetpack Compose)
Day-one access to every new OS feature.
Best for apps built around the platform: widgets, watch apps, background audio, advanced camera, AR.
The cost: two codebases, and often two teams.

The trade-off
→ Native look and feel: Native best, React Native close, Flutter imitates
→ Custom, brand-heavy UI: Flutter strongest
→ Code sharing with the web: React Native
→ New OS APIs on day one: Native only
→ Cost for a small team: React Native or Flutter

The honest part
Most cross-platform apps still have some native code. Home screen widgets, share extensions and some SDKs need Swift or Kotlin. Plan for about 10% native work, not 0%.

When to pick each
→ React Native: product apps, a team that knows React, a web app to share logic with
→ Flutter: custom visual design, no web codebase to share, a team happy with Dart
→ Native: the platform is the product, or performance is the product

Common wrong choice
A camera-first or AR app built cross-platform. The core ends up in native modules anyway, and you maintain three layers instead of two.

[PERSONAL: which stack I ship mobile apps with today, and the main reason]

Takeaway: choose by how much of your app is the platform itself.

Next: Expo vs bare React Native, and whether ejecting still makes sense.

#MobileDevelopment #ReactNative #Flutter #iOSDev
