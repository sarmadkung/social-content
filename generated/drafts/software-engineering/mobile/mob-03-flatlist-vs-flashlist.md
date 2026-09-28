SERIES:    SOFTWARE ENGINEERING · MOBILE #03
TITLE:     FlatList vs FlashList: Why Your List Janks
PILLAR:    Software Engineering · Mobile — for mid-level and senior React Native engineers
LEVEL:     ADVANCED
MODE:      COMPARE
FORMAT:    VISUAL
HEADLINE:  Create and destroy, or recycle
LAYOUT:    COMPARE
STATUS:    draft
---
A chat screen with 2,000 messages. Scroll fast on a mid-range Android.
White gaps appear and frames drop. The list is doing too much work per scroll.

The shared problem
You cannot render 2,000 rows at once. Both lists render only what is near the screen. They differ in what happens to a row that scrolls away.

FlatList (built in)
Virtualization: rows far off screen are unmounted, and new rows are mounted as they come into view.
Mounting means creating components and native views again and again. On a fast scroll the JS thread falls behind, and you see blank space.

FlashList (by Shopify)
Recycling: a row that leaves the screen is not destroyed. It is re-rendered with the next item's data.
Reusing a view costs much less than creating one, so fast scrolls stay smooth.
Version 2 is built for the New Architecture and no longer needs a size estimate for each item.

[FACT_CHECK: FlashList v2 targets the New Architecture and removes the need for estimatedItemSize → FlashList v2 docs/release notes]

In code, the switch is small:
<FlashList
  data={messages}
  keyExtractor={(m) => m.id}
  getItemType={(m) => m.kind}   // "text" | "image" | "system"
  renderItem={({ item }) => <MessageRow msg={item} />}
/>

getItemType keeps separate pools, so an image row is never recycled into a text row.

The catch with recycling
Local state inside a row survives recycling. Expand message #12, scroll, and message #40 shows up expanded.
Fix: keep that state outside the row, keyed by item id, or reset it when the item changes.

The trade-off
→ Drop-in simplicity, no surprises: FlatList
→ Long or fast-scrolling feeds, mixed row types: FlashList
→ Rows with their own useState: FlatList is safer; FlashList needs care

Tips that help either one
→ Wrap row components in memo and keep props stable
→ No heavy work inside renderItem
→ Give images a fixed size so rows do not jump

Common mistake
Judging list speed in a debug build. Dev mode is much slower. Always test in a release build on a low-end Android phone.

[PERSONAL: optional — a list I fixed, with before and after numbers if I measured them]

Takeaway: FlatList creates and destroys rows. FlashList reuses them. Reuse is faster, but reused rows remember their state.

Next: local storage on mobile, MMKV vs SQLite vs WatermelonDB.

#ReactNative #MobileDevelopment #Performance #Expo
