# Palette's Journal

## 2025-05-14 - Responsive Foundations
**Learning:** Legacy-style layouts often use fixed pixel widths which break on mobile. Implementing a fluid `max-width` with a percentage `width` and global `box-sizing: border-box` is a critical first step for accessibility and UX in these environments.
**Action:** Always inspect the main container's width and set a global `box-sizing` rule to ensure padding doesn't cause overflow.

## 2025-05-14 - Required Field Clarity
**Learning:** Adding the `required` attribute is great for functional accessibility, but users need a visual cue (like an asterisk) to know which fields are mandatory before they attempt submission. Also, ensure no accidental log files are included in the PR.
**Action:** Use a `.required` class for asterisks and double-check for temporary files like `server.log` before submitting.
