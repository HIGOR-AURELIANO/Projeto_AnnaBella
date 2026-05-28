## 2024-05-24 - Semantic Navigation in Static Sites
**Learning:** In multi-page static HTML projects without a templating engine, users lack immediate context of their location. Combining a visual `.active` class with the semantic `aria-current="page"` attribute ensures that both sighted users and screen reader users can easily identify the current page.
**Action:** Always manually synchronize navigation states across all static pages and pair visual highlights with ARIA attributes.

## 2024-05-24 - Accessible Focus States for Custom Themes
**Learning:** Default browser focus indicators may have poor contrast against custom background colors or themed borders. Using `:focus-visible` allows for high-visibility, branded focus rings that only appear for keyboard navigation, maintaining aesthetics for mouse users while significantly improving accessibility.
**Action:** Implement custom `:focus-visible` styles early in the CSS to ensure interactive elements are accessible regardless of the theme's color palette.
