---
title: "We split one cross-platform codebase into native apps. Here's why."
description: "We shipped iOS, Android, web and desktop from one codebase, then split it. What it cost us, what native fixed, and how agents and tests keep the apps in sync."
date: 2026-10-29
series: "Building"
seriesNumber: 1
slug: build-01-one-codebase-to-native
tags: [mobile, cross-platform, native, coding-agents, testing]
cover: cover.png
---

We shipped iOS, Android, web and desktop from one codebase. Shared UI, shared libraries, shared packages. Everything that could be shared, was.

Then we took it apart.

Cross-platform gave us a lot. It also took a lot. Here is how we kept what it gave and won back what it took.

## What we'll cover

![The six parts of this post](0.png)

1. What cross-platform gave us, and what it took
2. What one codebase cost us
3. What did we migrate to?
4. Who keeps the apps in sync now
5. Rules are not enough: tests hold the line
6. What we have now

## Context

The product is a real-time collaboration app I work on: chat, calls and shared documents. One Expo codebase served all four platforms. Expo is a framework for building iOS and Android apps (and web) from one React Native codebase.

On paper, that was the dream: write once, ship everywhere. In practice, "write once" became "debug everywhere".

## What cross-platform gave us, and what it took

![What cross-platform gave us on one side, what it took on the other](1.png)

It gave us:

- **One codebase:** write a feature once, ship it everywhere.
- **One team:** nobody had to know Swift, Kotlin and web at the same time.
- **Every platform at once:** a feature reached all four together.
- **Apps that matched:** same screens, same behaviour everywhere.

It took from us:

- **Performance:** everything waited on one JavaScript thread.
- **Native feel:** the UI was close to each platform, never exactly right.
- **Independence:** a fix for one platform could break another.
- **Simple builds:** shared plumbing broke one app while another built fine.

For a while, the gains were worth it. Then the losses started to win. Here is what they looked like day to day.

## Did cross-platform manage everything for us?

![The per-platform work we still did by hand inside one codebase](2.png)

No. It was one codebase on paper. Underneath, we still handled each platform by hand:

- **Libraries:** many packages work only on native or only on web, so each one needed a fallback.
- **Web vs native APIs:** web APIs (localStorage, window) and native APIs (camera, file system) need separate code paths.
- **Logs and crashes:** Xcode for iOS, Logcat for Android, the browser console for web. Native crash reports need their own symbol files per platform.
- **Permissions:** an Info.plist entry on iOS, the manifest on Android, a browser prompt on web.
- **Notifications:** APNs on iOS, FCM on Android, web push on the web.
- **Platform actions:** the share sheet, deep links and background tasks work differently on each OS.
- **UI details:** safe areas, the keyboard, the Android back button versus the iOS back gesture.
- **Testing:** each platform still needed its own devices and simulators.

That per-platform work is the work native apps do anyway. So going native cost less than it looked.

## What one codebase cost us


**Performance we could not fix from shared code.** Heavy screens and real-time updates competed for the same JavaScript thread: the single thread that runs all of the app's JavaScript. When it was busy, the whole app lagged. The fix was often native code anyway, hidden behind a shared wrapper.

**Fixing one platform broke another.**
- A browser-only line in a shared config file crashed every iOS and Android launch before the first screen. The tests passed, because the test environment pretends to be a browser.
- A control built for the desktop web was reused in the call screen. Phones were fine, but tablets crashed, because the check looked at screen width, not at the kind of device.
- A layout change on one screen removed the bottom spacing on another, and the message box slid under the phone's home bar.
- Every change had to be checked on four surfaces, because all four shared it.

**UI that never quite fit.**
- A bottom sheet with a fixed height cut off its own buttons when users set a larger text size in their phone settings.
- On tablets, a minimized call showed two sets of controls at once: one built for phones, one built for desktop.
- Safe areas (the parts of the screen the notch and home bar don't cover), keyboards, gestures and screen sizes behaved differently on each platform. Shared components grew a pile of "if this platform" checks.

**Shared build plumbing.** Shared packages are wired into each app through path settings. One folder left out of the mobile build upload broke the whole mobile build, while web built fine. A check that asked "can this code reach that screen?" kept passing while it was blind: it couldn't see platform-specific file variants, and it walked only 4.6% of the code's import links.


## What did we migrate to?

Native where the platform matters. Web where it doesn't.

![One shared codebase before, separate apps after](3.png)

- **iOS:** native Swift and SwiftUI
- **Android:** native Kotlin and Jetpack Compose
- **Web:** its own web app
- **Desktop:** the web app in a native window

Desktop stayed on web because it is fast enough there, and the OS is not part of the product. Going native on desktop would cost a lot and give users almost nothing. Native is a choice per platform, not a rule.

## Who keeps the apps in sync now

![The framework synced the code; agents sync the behaviour](4.png)

This was the scary part. With one codebase, the framework kept the apps in sync for free: there was only one copy of the code. Split it into separate apps, and someone has to make sure a feature or a fix reaches every one of them.

A few years ago, that someone would have been more people: a Swift developer, a Kotlin developer, a web developer, and every feature built three times by hand.

Now coding agents do the porting. We wrote the rules once, in the agents' instruction file, the file every agent session reads before it starts:

- A new feature is built in the web app first, then ported to the native apps.
- A fix lands in every app it affects.
- When a shared behaviour changes (how links open, how search ranks, how a page lays out its blocks), the instruction file names the native code that must change with it.

People still own the apps. Agents do the porting; each native app has an owner who keeps it in step with main and checks what lands.

## Rules are not enough. Tests hold the line.


An instruction file tells an agent what to do. Tests check that it was done. Every app runs against the same fixtures. A fixture is one saved test case that every app must handle the same way. For example, the link to room 42 must open room 42 on web, iOS and Android.

- **Routes:** every link the web app opens has a test case the native apps must parse the same way.
- **Wire formats:** the messages the server sends are recorded once, and the native apps' tests read the same recordings.
- **Content rules:** a native app may be stricter than the server about what it sends, never looser, and a test fails if it is looser.
- **Strings and analytics:** change a user-facing string or a tracked event without regenerating the native copy, and CI fails.

If a port is skipped, a test goes red before the apps drift.

## Why this beats a cross-platform tool

- The framework kept the apps in sync by forcing the same code on every platform. Every app got the same compromises, and a bug in shared code reached every app too.
- Agents and fixtures keep the behaviour in sync, not the code. Same feature, same rules, but each app is written the way its platform expects.
- The rules are plain text in one file. Changing how we sync is an edit, not a framework migration.

## What we have now

![Every gain kept thanks to agents, every loss won back thanks to native](5.png)

Every gain cross-platform gave us, we kept, thanks to agents:

- **One codebase:** one set of contracts, rules and fixtures; agents write each app from them.
- **One team:** agents write the Swift and the Kotlin; people review and own each app.
- **Every platform at once:** a feature built on web reaches the native apps within days, not quarters.
- **Apps that match:** shared fixtures fail the build when an app's behaviour drifts.

Every loss, we won back, thanks to native:

- **Performance:** the native apps talk to the OS directly, with no JavaScript layer in between.
- **Native feel:** each platform's own UI system handles safe areas, keyboards and text size. Calls keep running in the background on Android and show on the lock screen on iOS.
- **Independence:** each app has its own code. An Android fix cannot touch iOS, and browser code lives only in the web app.
- **Simple builds:** each app builds on its own, with its own tools and its own CI.

And the move itself took weeks, not years. With agents writing the native code from the same rules and fixtures, a native rewrite stopped being a multi-year project.

## The price we pay now

We didn't get this for free. The price moved from our users to us:

- More code to review: three apps instead of one.
- More pipelines and more store releases. iOS UI tests need a Mac in CI.
- Some bugs now live on one platform only, so we test each app on its own.
- Fixtures only cover what someone pinned. A behaviour nobody wrote a fixture for can still drift.

## Keep in mind if you build something like this

- Move one platform at a time; the old app keeps shipping meanwhile.
- Put sync rules in the agents' instruction file, not in people's heads.
- Back every rule with a shared fixture, so a skipped port fails the build.
- Give each native app an owner who checks what agents port.
- Freeze new features on the old shared app, or the move never ends.
- Keep web where it is fast enough, as our desktop app did.

## The lesson

One codebase was a fix for the cost of writing everything twice and keeping the copies in sync. Agents now do the writing, and shared fixtures check the sync. So we kept what cross-platform gave us, won back what it took, and picked the best tool for each platform again.

## Next in the series

The general case behind this story: why agents changed the case for cross-platform frameworks (Dev Growth #12).
