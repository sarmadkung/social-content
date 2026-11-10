> ⚠ NOT READY — resolve these, then delete this block:
> - [PERSONAL: the options we considered: stay on Expo and fix it, go native everywhere, a mix — and why each was or was not picked]
> - [PERSONAL: the performance difference you saw after the move, with a number if safe to share]
> - [PERSONAL: what got better, with a number if safe to share (startup time, frame drops, crash rate, time to ship a feature on all platforms)]

---

I work with a team of engineers on a great app with a lot of users.
It started cross-platform: one Expo codebase for iOS, Android, web and desktop. There were no coding agents back then, so one codebase was the only sane way to ship everywhere.

It worked, until it didn't.
"Write once" turned into "debug everywhere". A fix for one platform broke another. And under the shared code, we still handled every platform by hand.

We knew native was the answer. But a rewrite meant three apps and years of work, with too much else up in the air.

Then agents arrived.
They now write the Swift and the Kotlin from one set of rules, and shared tests fail the build if an app drifts. So we finally took the app native, and the move took weeks, not years.

The app kept everything cross-platform gave it, and gained everything native gives.

For us, cross-platform as the default is dead.

Where else do you think it's dead now, and where does it still win?

#MobileDevelopment #iOSDevelopment #AndroidDevelopment #AIAgents #SoftwareEngineering
