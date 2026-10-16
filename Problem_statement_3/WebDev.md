# Web Code Auto-Fixer & Playground Studio

## Context & Objective

Developers frequently encounter malformed user-submitted code—such as unclosed HTML tags, mismatched elements, unformatted CSS rules, and basic JavaScript syntax errors.

Your task is to build a Web Code Auto-Fixer website. The website / application must take raw HTML, CSS, and JavaScript input (either separately or together as a single code block), automatically detect and repair markup or syntax errors, and format the code cleanly as a mandatory requirement. A real-time side-by-side comparison between the raw input and corrected output is a bonus feature.

## Scope & Functional Requirements

### HTML Engine (Mandatory)

- Tag Auto-Closing & Balance: Detect and close missing end tags (for example, `<div><p>Hello</div>` should become `<div><p>Hello</p></div>`).
- Mismatched Tag Repair: Fix incorrect nesting or tag order (for example, `<b><i>text</b></i>` should become `<b><i>text</i></b>`).
- Void Tag Handling: Correctly handle self-closing tags like `<img>`, `<input>`, `<br>`, and `<hr>` without forcing unnecessary closing tags.
- Attribute Normalization: Quote unquoted or improperly quoted attributes (for example, `<a href=index.html>` should become `<a href="index.html">`).
- Code Formatting & Indentation: Output clean, consistently indented HTML using 2 or 4 spaces.

### CSS Engine (Mandatory)

- Syntax Repair: Auto-insert missing semicolons at the end of declaration lines and repair unclosed brackets such as `{}`.
- Property Beautifier: Format CSS into standard readable blocks, with selectors on their own line and properties indented.
- Basic Validation: Identify and flag invalid or unknown CSS property names (for example, `colr: red;` should be flagged as an error or warning).

### JavaScript Engine (Optional / Bonus)

- Syntax & Formatting Check: Run basic JavaScript beautification and detect fundamental syntax issues such as missing closing parentheses or unclosed quotes.
- Console / Error Log: Catch and display syntax error messages with line numbers instead of letting the application crash.

### Interactive Web UI (Optional / Bonus)

- Split Editor Layout: Left panel for raw input (tabs for HTML, CSS, and JS); right panel for fixed code and live preview.
- Error Log Drawer: Highlight the specific lines where errors were found and explain what auto-fixes were applied.
- One-Click Action Button: Include a “Fix & Format Code” button and a “Copy Corrected Code” button.
- Live Sandbox Preview: Render the auto-fixed HTML, CSS, and JS in an isolated `<iframe>` container.

## Tech Stacks & Constraints

- You may use any language of your choice to implement this problem statement, such as C/C++, Python, or JavaScript. However, Python or JavaScript is preferred.
- You can choose how you want to attempt this problem statement. You may either:
  1. Write a program in your preferred language that does the job.
  2. Build an interactive interface where malformed code is pasted and clean, corrected code is produced along with a preview (optional).
- Basic helper libraries (for example, CodeMirror, Monaco Editor for the UI, or standard DOM parsing APIs) are allowed, but the core tag-repair logic must be clear and understandable (for example, stack-based data structures for matching tags).

## Expected Scenarios

Your submission must be able to handle the following cases:

- Unclosed Nested Tags: `<div><span><p>Text</div>`
- Malformed Attributes: `<img src=pic.jpg alt="photo class=hero>`
- Broken CSS Blocks: `h1 { color: red; font-size: 16px` (missing trailing brace)
- Mixed Case Tags: `<DIV><p>Hello</P></DIV>` (normalize to lowercase standard)
- Script Tag Safety: Ensure inline JavaScript inside HTML `<script>` tags is properly escaped and handled.

## Suggested Deliverables

- A working auto-fix tool or web application for malformed HTML, CSS, and optional JavaScript.
- A clean output that repairs broken structure and formatting while preserving the intent of the original code.
- A user-friendly interface with input/output panels and optional preview support.
- Error reporting or warnings for elements that were corrected automatically.

## Resources

- [freeCodeCamp](https://www.freecodecamp.org/) – A full, free curriculum with certifications.
- [MDN Web Docs](https://developer.mozilla.org/) – The definitive reference for HTML, CSS, and JavaScript.
- [Apna College](https://www.youtube.com/@ApnaCollegeOfficial) – Beginner-friendly tutorials.
- [CodeWithHarry](https://www.codewithharry.com/) – Project-based web development tutorials.
- [Chai aur Code](https://www.youtube.com/@chaiaurcode) – Modern JavaScript and React content.
- [Coding Ninjas](https://www.codingninjas.com/) – Structured learning courses.
