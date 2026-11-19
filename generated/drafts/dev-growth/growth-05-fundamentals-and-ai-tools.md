SERIES:    DEV GROWTH #05
TITLE:     AI Writes the Code. Why Fundamentals Still Matter, and How to Keep Them
PILLAR:    Career & Developer Growth — for students and junior developers, and seniors who review AI-written code
LEVEL:     INTERMEDIATE
MODE:      WHY
FORMAT:    VISUAL
HEADLINE:  Use AI, but stay the author
LAYOUT:    STATEMENT
VISUALS:   1 = Why do fundamentals still matter? · 2 = What went wrong on the slow page? · 3 = How do you use AI tools and keep your skills? · 4 = Where is AI a good fit, and where is it risky? · rest = text
STATUS:    draft
---
An AI tool writes a function. It passes the tests. It runs fine on 100 rows. In production, with 100,000 rows, the page times out.

The code is merged under your name. When it breaks at 2 a.m., the AI is not on call. You are.

The question
If AI can write the code, why learn data structures, databases and how networks work? And if you use AI every day, how do you keep those skills?

What it means
AI coding tools are assistants that suggest or write code from a prompt. Using them well means you stay the author: you decide, you check, you understand.

Think of a calculator. It is faster than you at arithmetic. But if you never learned what multiplication means, you cannot tell when you typed the wrong number.

Why do fundamentals still matter?
1. Your job moves from typing to deciding. You read more code than you write, and you choose what gets merged. You can only own a choice you understand.
2. Code can look right and still fail one level down: in how it scales, in what runs at the same time, in what happens when the network fails. That level is fundamentals.
3. Your prompt is only as good as your ideas. "Make it faster" gets a guess. "Use a Set for lookups" or "add an index on user_id" gets the fix. You need to know the name of the right idea to ask for it.
4. When it breaks, you make the call. The tool can suggest causes. You still decide which one is true, using what you know about how the system works.
5. Tools change every few months. Fundamentals change slowly. What you learn about memory, data and networks keeps paying for your whole career.

Takeaway: AI makes code cheap. Understanding why it works is what lets you own it.

What went wrong on the slow page?
The generated code did this:

for (const order of orders) {
  if (blockedIds.includes(order.userId)) { ... }
}

includes() checks the list one item at a time. 100,000 orders × 100,000 blocked IDs is up to 10 billion checks. A Set makes each lookup about one step:

const blocked = new Set(blockedIds);
if (blocked.has(order.userId)) { ... }

[FACT_CHECK: Array.prototype.includes() checks items one at a time, and Set.has() is about one step per lookup → ECMAScript spec / MDN pages for Array.prototype.includes and Set]

The request never mentioned 100,000 rows, and the tests used 100. Knowing Big-O (how work grows as the input grows) is what makes you ask "what happens at real size?" before you merge, and test with real data.

Takeaway: ask how the work grows as the input grows, before you accept the code.

[PERSONAL: one bug in AI-written code you caught because you knew the underlying concept]

How do you use AI tools and keep your skills?
1. Think first. Write your plan in two or three lines before you prompt.
2. Try the hard part yourself when you are learning something new. Use AI after, to compare.
3. Ask for small pieces, not whole features. Small diffs are easy to review.
4. Read every line before you accept it. If you cannot explain a line, ask the tool why, then check the docs.
5. Run it and test it, with real data sizes. AI can invent functions or options that do not exist, and slow code hides in 100-row tests.
6. When the tool fixes something, learn the idea behind the fix.
7. Sometimes turn it off. Solve one problem a week with no assistant, to keep the muscle.

Takeaway: AI types the code. You still own the thinking.

[PERSONAL: how you use AI tools in your own daily work, and one rule you keep]

Where is AI a good fit, and where is it risky?
→ Good: boilerplate, test cases, renaming, explaining unfamiliar code.
→ Risky: security, payments, concurrency (code running at the same time), anything you cannot verify.

Takeaway: hand AI the work you can check quickly. Slow down where one wrong line costs the most.

What goes wrong if you skip this
→ You accept code because it passed one quick run, not because it is right.
→ You cannot choose between two suggestions, so you try them all.
→ You let the tool pick the design, not only the syntax.
→ You paste secrets or private code into a tool your company has not approved.
→ Your growth stalls. Seniority is judgment, and judgment is built on fundamentals.

For seniors
Review AI-written code as carefully as human code. It reads clean and confident whether it is right or wrong. And ask juniors to explain their diff in review: "why this approach?" The answer shows what they understand, and that is where learning still happens.

Keep in mind
→ Test with real data sizes.
→ Can't explain why it works? Don't merge it yet.

Takeaway: use AI for the typing, keep the fundamentals for the deciding. Code you cannot explain is not yours yet.

Next: how to prepare for coding interviews without grinding 500 problems.

#DeveloperGrowth #SoftwareEngineering #AIEngineering #CareerGrowth #Programming
