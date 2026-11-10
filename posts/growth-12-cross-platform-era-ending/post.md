For ten years, "we need it on every platform" had one answer: one codebase.
React Native or Flutter for phones. Electron for desktop. Ionic to wrap the web app in a mobile shell.

That was the right call. Writing the same feature twice, or four times, was the most expensive thing in app development.

Coding agents just made it cheap.

The question
If an agent can build a feature in Swift and then port it to Kotlin in an afternoon, why are we still paying the cross-platform tax?

What cross-platform did for us
A cross-platform framework lets you write an app once and run it on several platforms (iOS, Android, web, desktop). Every job it did now has another owner:
→ One codebase → the agent writes each app from one spec
→ One skill set → the agent knows Swift, Kotlin and C#; you need to review them, not master all of them
→ Feature parity → a shared spec + the same test scenarios on every app
→ Shared business logic → it lives in the backend, or in API clients generated from one contract

The reason, step by step
1. Cross-platform was never about better apps. It was about cost: one team instead of one per platform.
2. The biggest cost was writing and keeping several versions of every feature.
3. Agents are very good at exactly this: "here is the iOS version and the spec, build the Android one".
4. When writing it twice is cheap, the tax you paid for one codebase stops making sense.

Not just mobile
The same logic applies to every "write once, run everywhere" framework:
→ Mobile: React Native, Flutter, Ionic, .NET MAUI → native Swift for iOS, Kotlin for Android
→ Desktop: Electron, Flutter desktop → native SwiftUI for macOS, WinUI for Windows, or stay on web
→ Web and mobile in one: React Native Web, Expo for web → a real web app + native mobile apps
Each one hurts in its own way:
→ Electron ships its own copy of Chromium and Node.js inside every app. Big downloads, high memory, even for a simple chat window.
→ Flutter draws its own widgets instead of using the platform's. It looks close, but a new OS design arrives only when Flutter redraws it.
→ Ionic runs your web app inside a WebView (a browser view embedded in the app). Scrolling, gestures and the keyboard feel like a website.
→ .NET MAUI replaced Xamarin, and Xamarin support ended. Teams had to migrate whole apps just to stay supported.
→ React Native Web shares components between the browser and the phone. Browser-only code slips into a shared file and crashes the mobile app.

The middle ground: Kotlin Multiplatform can share just the logic and keep each platform's UI native. That is the same split this post argues for.

The tax of one codebase
Performance
→ An extra layer sits between your code and the OS: a JS runtime, an embedded browser or a custom renderer.
→ In React Native, one JS thread does the work. When it is busy, lists stutter and animations drop frames.
→ Slower startup: the runtime has to load before the first screen.
→ Bigger apps: you ship the framework on top of your code.
One fix breaks another platform
→ A shared component fixed for Android now looks wrong on iOS.
→ A web fix uses a browser-only API and crashes the mobile app.
→ Every change has to be tested on every platform, because every platform shares the code.
UI that never quite fits
→ Keyboard, safe areas, gestures, windows and scrolling behave differently on each platform.
→ `if (Platform.OS === 'web')` checks spread through the code until nobody trusts a component.
→ The look and feel is copied from the platform, not inherited from it.
Dependencies and upgrades
→ A library supports iOS and Android but not web, or the other way round.
→ A framework upgrade can break half your dependencies at once.
→ New OS features arrive weeks or months late, after the framework catches up.
Debugging and native code anyway
→ A crash can live in your code, the framework layer or native code. You debug three layers.
→ You still write native code for widgets, share extensions, the camera and background work.

How the apps stay in sync
This is the part people worry about. Without one codebase, the apps drift apart. Here is the loop that stops it:
1. Write the feature spec once: screens, states, API calls, edge cases. Platform-neutral.
2. The agent builds it on one platform first.
3. The agent ports it to the others, using the spec and the first diff as the reference.
4. One API contract (OpenAPI or protobuf) generates the client code for every app, so the data layer cannot drift.
5. The same test scenarios run on every app (for example, one set of Maestro flows for iOS and Android).
6. Review checks parity: same states, same errors, same edge cases. (How to review agent code: DEV GROWTH #09.)

I've lived this: a product I work on went from one Expo codebase for iOS, Android, web and desktop to native iOS and Android. The full story is its own post (BUILDING #01).

What you get back
→ Day-one access to new OS features: widgets, Live Activities, App Intents, new camera APIs
→ Real native look, feel and gestures, not a copy
→ Platform tools that just work: Xcode Instruments, Android Studio profiler
→ No framework layer between your code and the OS, fewer native-module workarounds, smaller apps
→ No waiting for a framework to support the new iOS, Android, macOS or Windows release

Watch out: what going native costs
→ Review doubles → the agent writes two codebases, someone still checks both → have a reviewer who can read each language
→ More pipelines → two builds, two store reviews, two release dates → automate builds and ship both apps on the same day
→ Platform-only bugs → a fix lands on iOS and Android still has the bug → run the same test scenarios on every app, every time
→ Drift → the apps slowly behave differently → one spec, one API contract, parity checks in review

What goes wrong if you ignore this
→ You start a new app on a cross-platform stack by habit, and pay the tax for years
→ Your app gets new OS features last, after competitors who went native
→ Or the opposite: you go native with no spec and no shared tests, and the apps drift apart in a month

When cross-platform still wins
→ You share real logic and UI with a React web app
→ Nobody on the team can review Swift, Kotlin or the desktop language
→ The app is simple forms and lists, and the OS is not part of the product
→ Desktop, where the web app is fast enough. We kept ours on web.

Keep in mind before you pick a cross-platform framework
→ Decide per platform: phones and desktop need different answers
→ Write the spec before the first app, not after the second
→ Generate API clients from one contract, never by hand
→ Go native only where someone can review that language
→ Keep web where it is fast enough; native has to earn its cost

Takeaway
Cross-platform solved the cost of writing it twice. Agents solve that cost too, so you can pick the best tool for each platform again.

Next: how to break a problem down before you code.

#SoftwareEngineering #MobileDevelopment #CrossPlatform #CodingAgents #DeveloperGrowth
