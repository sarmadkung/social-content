SERIES:    BUILDING #01
TITLE:     We Shipped Four Platforms From One Codebase. Then We Went Native.
PILLAR:    Building — real decisions from a product I work on
LEVEL:     INTERMEDIATE
MODE:      PERSONAL
TYPE:      DECISION
SOURCE:    2026-10-22 — Pivot
FORMAT:    VISUAL
HEADLINE:  One codebase, four apps. Then we went native.
LAYOUT:    COMPARE
VISUALS:   1 = What did cross-platform give us, and take? · 2 = Did cross-platform manage everything for us? · 3 = What did we migrate to? · 4 = Who keeps the apps in sync now? · 5 = What did we achieve in the end? · 6 = Is cross-platform dead? As a default, yes. · 7 = Where else is cross-platform dead now? · rest = text
STATUS:    draft
---

We shipped iOS, Android, web and desktop from one codebase. Shared UI, shared libraries, shared packages. Everything that could be shared, was.

Then we took it apart.

Cross-platform gave us a lot. It also took a lot. Here is how we kept what it gave and won back what it took.

Context
A real-time collaboration product I work on: chat, calls, shared documents. One Expo codebase served all four platforms. On paper, the dream: write once, ship everywhere.
In practice, "write once" became "debug everywhere".

What did cross-platform give us, and take?
It gave us:
→ One codebase: write a feature once, ship it everywhere
→ One team: nobody had to know Swift, Kotlin and web at the same time
→ Every platform at once: a feature reached all four together
→ Apps that matched: same screens, same behaviour everywhere

It took from us:
→ Performance: everything waited on one JavaScript thread
→ Native feel: the UI was close to each platform, never exactly right
→ Independence: a fix for one platform could break another
→ Simple builds: shared plumbing broke one app while another built fine

For a while, the gains were worth it. Then the losses started to win. Two of them, as real bugs:
→ Native feel: a bottom sheet with a fixed height cut off its own buttons when users set a larger text size in their phone settings. Safe areas (the parts of the screen the notch and home bar don't cover), keyboards and gestures behaved differently on each platform, so shared components grew a pile of "if this platform" checks.
→ Independence: a browser-only line in a shared config file crashed every iOS and Android launch before the first screen. The tests passed, because the test environment pretends to be a browser.

Did cross-platform manage everything for us?
No. It was one codebase on paper. Underneath, we still handled each platform by hand:
→ Libraries: many packages work only on native or only on web, so each one needed a fallback
→ Web vs native APIs: web APIs (localStorage, window) and native APIs (camera, file system) need separate code paths behind platform checks
→ Logs and crashes: Xcode for iOS, Logcat for Android, the browser console for web; native crash reports need their own symbol files per platform
→ Permissions: an Info.plist entry on iOS, the manifest on Android, a browser prompt on web
→ Notifications: APNs on iOS, FCM on Android, web push on the web
→ Platform actions: the share sheet, deep links and background tasks work differently on each OS
→ UI details: safe areas, the keyboard, the Android back button versus the iOS back gesture
→ Testing: each platform still needed its own devices and simulators
That per-platform work is the work native apps do anyway. So going native cost less than it looked.

Options
[PERSONAL: the options we considered: stay on Expo and fix it, go native everywhere, a mix — and why each was or was not picked]

Decision
Native where the platform matters. Web where it doesn't.

What did we migrate to?
Before: one Expo codebase → iOS, Android, web, desktop
After:
→ iOS: native Swift and SwiftUI
→ Android: native Kotlin and Jetpack Compose
→ Web: its own web app
→ Desktop: the web app in a native window

Why desktop stayed on web
It is fast enough, and the OS is not part of the product there. Going native on desktop would cost a lot and give users almost nothing. Native is a choice per platform, not a rule.

Who keeps the apps in sync now?
This was the scary part. With one codebase, the framework kept the apps in sync for free: there was only one copy of the code. Split it into separate apps, and someone has to make sure a feature or a fix reaches every one of them.

A few years ago, that someone was more people: a Swift developer, a Kotlin developer, a web developer, and every feature built three times by hand.

Now coding agents do the porting. We wrote the rules once, in the agents' instruction file (the file every agent session reads before it starts):
→ A new feature is built in the web app first, then ported to the native apps
→ A fix lands in every app it affects
→ When a shared behaviour changes (how links open, how search ranks, how a page lays out its blocks), the instruction file names the native code that must change with it

People still own the apps. Agents do the porting; each native app has an owner who keeps it in step with main and checks what lands.

Shared tests check the ports: the same test cases run against every app, so a skipped port fails the build before the apps drift apart.

Why this beats a cross-platform tool
→ The framework kept the apps in sync by forcing the same code on every platform. Every app got the same compromises, and a bug in shared code reached every app too.
→ Agents and shared tests keep the behaviour in sync, not the code. Same feature, same rules, but each app is written the way its platform expects.

What did we achieve in the end?
We kept every win cross-platform gave us, thanks to agents:
→ One codebase → one set of rules and shared tests; agents write each app from them
→ One team → agents write the Swift and the Kotlin; people review and own each app
→ Every platform at once → a feature built on web is ported to the native apps within days, not quarters
→ Apps that match → shared tests fail the build when an app's behaviour drifts

Plus, we gained what only native apps can do:
→ Calls outside the app → a call shows up as a Live Activity on iOS and keeps running in a foreground service on Android
→ Text size and safe areas → SwiftUI and Compose handle them, so no more sheets cutting off their own buttons
→ Performance → the native apps talk to the OS directly, with no JavaScript layer in between
→ Independence → each app has its own code; an Android fix cannot touch iOS, and browser code lives only in the web app
→ Own builds → each app builds on its own, with its own tools and its own CI

The price we pay now
We didn't get this for free. The price moved from our users to us:
→ More code to review: three apps instead of one
→ More pipelines and more store releases; iOS UI tests need a Mac in CI
→ Some bugs now live on one platform only, so we test each app on its own
→ Tests only cover what someone wrote a test for. Anything else can still drift.

Result
→ The move took weeks, not years. With agents writing the native code from the same rules and tests, a native rewrite stopped being a multi-year project.
[PERSONAL: the performance difference you saw after the move, with a number if safe to share]
[PERSONAL: what got better, with a number if safe to share (startup time, frame drops, crash rate, time to ship a feature on all platforms)]

Is cross-platform dead? As a default, yes.
For apps where the operating system is the product, cross-platform as the default is dead. Three beliefs that kept us on it died with it:
→ "Write once, run everywhere": in practice it became write once, debug everywhere
→ "A native rewrite takes years": agents write the native code from shared rules and tests
→ "You are locked into your framework": our sync rules are plain text, so changing how we sync is an edit, not a migration
What we'd tell a team starting today: don't pick cross-platform by default. Pick per platform: native where the OS is the product, web where it is fast enough.

Keep in mind if you build something like this
→ Move one platform at a time; the old app keeps shipping meanwhile
→ Put sync rules in the agents' instruction file, not in people's heads
→ Back every rule with a shared test, so a skipped port fails the build
→ Give each native app an owner who checks what agents port
→ Freeze new features on the old shared app, or the move never ends

Lesson
One codebase was a fix for the cost of writing everything twice and keeping the copies in sync. Agents now do the writing, and shared tests check the sync. So we kept what cross-platform gave us, won back what it took, and picked the best tool for each platform again.

Where else is cross-platform dead now?
Agents can write the same feature for every platform. So which other "write once, run everywhere" tools lose their reason to exist? Some candidates, agree or not:
→ Desktop wrappers: one web app packaged for Windows, macOS and Linux
→ Hybrid WebView apps: a website wrapped to look like a phone app
→ Shared UI kits: one component library forced onto web and mobile
→ Low-code app builders: drag and drop once, export to every platform
Where do you think cross-platform is dead, and where does it still win? Tell me in the comments.

#MobileDevelopment #iOSDev #AndroidDev #CodingAgents #SoftwareEngineering
