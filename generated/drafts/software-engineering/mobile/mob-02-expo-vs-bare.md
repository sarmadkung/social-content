SERIES:    SOFTWARE ENGINEERING · MOBILE #02
TITLE:     Expo vs Bare React Native: Is There Still a Reason to Eject?
PILLAR:    Software Engineering · Mobile — for mid-level and senior React Native engineers
LEVEL:     INTERMEDIATE
MODE:      WHY
FORMAT:    VISUAL
HEADLINE:  Generate your native folders, or own them
LAYOUT:    COMPARE
STATUS:    draft
---
"Start with Expo, eject when you need native code" was solid advice years ago.
Today it is mostly outdated, and teams still eject out of habit.

The plain question
Why did teams eject, and does that reason still exist?

The reason, step by step
1. Old Expo was a sandbox. If a library needed custom native code, you could not use it. Ejecting gave you the ios/ and android/ folders to edit.
2. Development builds changed that. You build your own app binary with any native library inside, and still use Expo tooling.
3. Config plugins changed the rest. A plugin edits Info.plist, AndroidManifest or Gradle files for you, from code.
4. Prebuild generates the ios/ and android/ folders from app.json plus plugins. Expo calls this Continuous Native Generation (CNG).
5. For your own native code, the Expo Modules API lets you write modules in Swift and Kotlin.

[FACT_CHECK: React Native docs recommend starting new apps with a framework such as Expo → reactnative.dev "Get Started"]

Proof
Adding a native storage library:
npx expo install react-native-mmkv
npx expo prebuild   # or let EAS Build run it
No eject. The native folders are output, like a build folder.

[FACT_CHECK: react-native-mmkv works in Expo via development builds / prebuild → react-native-mmkv docs]

What goes wrong if you ignore it
You edit ios/AppDelegate by hand in a CNG project. The next prebuild --clean deletes the change. It works on your laptop and breaks on CI.
Fix: put that change in a config plugin, or decide the team owns the native folders from now on.

When bare React Native still makes sense
→ Brownfield: adding React Native into an existing native app
→ Native engineers who own and hand-edit ios/ and android/ every week
→ Heavy native changes no plugin covers, and nobody wants to write one
Even then, you can still use Expo modules and EAS in a bare project.

[PERSONAL: optional — a native change I moved into a config plugin, or a case where I chose bare]

Takeaway: the question is not "Expo or bare" anymore. It is "do we generate our native folders, or own them?"

Next: FlatList vs FlashList, and why your list janks.

#ReactNative #Expo #MobileDevelopment #SoftwareEngineering
