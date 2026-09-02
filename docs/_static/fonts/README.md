# Self-hosted web fonts

This directory contains WOFF2 web-font subsets for:

- Noto Sans JP, weights 400–700 (Google Fonts revision `v56`)
- Source Sans 3, normal and italic, weights 400–700 (Google Fonts revision `v19`)

The files and `unicode-range` declarations were obtained from the Google Fonts
CSS2 API using this request:

```text
https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400..700&family=Source+Sans+3:ital,wght@0,400..700;1,400..700&display=swap
```

The font URLs in the resulting stylesheet were rewritten to relative paths so
the site does not contact Google Fonts at runtime. When updating the fonts,
replace both `fonts.css` and all WOFF2 files together so their revisions and
`unicode-range` declarations stay synchronized. The Source Sans 3 faces also
have `size-adjust: 105%` added locally to balance their visual size with Noto
Sans JP; preserve this adjustment when regenerating the stylesheet.

The fonts are distributed under the SIL Open Font License 1.1. See
`OFL-Noto-Sans-JP.txt` and `OFL-Source-Sans-3.txt`.
