## 2025-05-15 - Navigation and Form Accessibility in Static Sites
**Learning:** In projects without a templating system, structural UI enhancements like "active" navigation states must be manually synchronized across all HTML files. Using `aria-current="page"` alongside a visual `.active` class provides the best experience for both sighted users and screen reader users.
**Action:** Always check all entry-point HTML files when updating shared components like navigation or headers.

**Learning:** Accessible form validation requires a multi-layered approach: visual indicators (asterisks), programmatic constraints (`required`), and semantic descriptions (`aria-required`).
**Action:** Use the `<span class="required">*</span>` pattern for labels and ensure `aria-required="true"` matches the `required` attribute.

**Learning:** Descriptive `alt` text for branding (logos) provides necessary context for screen reader users that empty `alt=""` or generic text lacks.
**Action:** Audit header logos for descriptive but concise `alt` text like "Brand Name - Logotipo".
