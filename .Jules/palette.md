## 2025-05-15 - Synchronizing Navigation in Static Sites
**Learning:** In projects without a templating engine (like Jekyll or React), UI components like navigation menus must be manually synchronized across all pages. Neglecting this leads to inconsistent UX, such as missing "active" states or outdated links on certain pages.
**Action:** When modifying global components in a static site, grep for the component's signature across all `.html` files to ensure 100% parity in implementation.
