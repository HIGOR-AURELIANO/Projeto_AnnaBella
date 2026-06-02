## 2026-06-02 - Semantic Navigation and Focus Visibility
**Learning:** In static HTML projects without a templating system, structural accessibility (semantic tags) and state indicators (active page, focus rings) must be manually synchronized across all files to maintain a consistent and accessible user experience.
**Action:** Use `aria-current="page"` combined with an `.active` CSS class for navigation, and implement a global `:focus-visible` style to ensure keyboard navigability without affecting mouse users.
