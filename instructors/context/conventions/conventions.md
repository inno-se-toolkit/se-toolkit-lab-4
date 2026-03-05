# Conventions for writing conventions

## Conventions

- [DRY](#dry)
- [Hyperlinks when mentioning sections](#hyperlinks-when-mentioning-sections)
- [Section link text](#section-link-text)

---

## DRY

Don't duplicate content across convention files. If a rule already exists in one file, reference it from others using a hyperlink instead of repeating it.

---

## Hyperlinks when mentioning sections

When mentioning a section by name, always link to it. For sections in another file, include the file path in the link.

Good: `See [Section name](#section-name).`

Good (cross-file): `See [Section name](other-file.md#section-name).`

Bad: `See the Section name section.`

---

## Section link text

Don't include the section number in the link text when linking inline. Use only the section name.

In a table of contents, you may include the section number in the link text.

Good (inline): `[Section name](#323-section-name)`

Good (TOC): `[3.2.3. Section name](#323-section-name)`

Bad (inline): `[3.2.3. Section name](#323-section-name)`
