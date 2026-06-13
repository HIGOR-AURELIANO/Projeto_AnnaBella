## 2026-06-13 - Active Menu State and ARIA Current
**Learning:** In multi-page static sites without a templating engine, users benefit significantly from a visual "you are here" indicator in the navigation menu. Pairing this with `aria-current="page"` ensures that both visual users and screen reader users can easily orient themselves within the site's structure.
**Action:** When working with navigation components, always verify that the current page is visually distinct and semantically identified using `aria-current="page"`.
