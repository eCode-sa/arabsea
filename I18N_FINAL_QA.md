# eGov Full i18n QA — 11 Oct 2026

- HTML pages checked: 114
- Unique Arabic UI strings checked: 3,893
- English-mode strings retaining Arabic characters: 0
- Unchanged Arabic UI strings in English mode: 0
- Shared language control: enabled through assets/js/core/app.js
- Local duplicate languageToggle controls: 0
- Local broken href targets: 0
- Buttons scanned: 1130
- Links scanned: 1774
- Forms scanned: 5
- i18n.js syntax: passed node --check

## Implementation
The central i18n engine now uses exact translations first, then pattern-aware translation for dynamic values such as SAR amounts, days, hours, percentages, dates/status composites, and a controlled glossary fallback. Unknown proper-name fragments are transliterated so English mode does not fall back to Arabic script.
