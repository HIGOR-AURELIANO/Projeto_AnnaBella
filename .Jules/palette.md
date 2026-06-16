## 2026-06-13 - Navigation Orientation & Header Accessibility
**Learning:** Static multi-page sites often lack visual and semantic feedback for the current page location, which disorients users. Additionally, branding-heavy header images are frequently missing alt text, creating a barrier for screen reader users.
**Action:** Always implement a combination of visual `.active` classes and semantic `aria-current="page"` attributes on navigation menus. Ensure main header branding has concise, descriptive alt text (e.g., "Anna Bella Oficial") rather than generic or missing descriptions.
