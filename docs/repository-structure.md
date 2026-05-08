# Repository Structure

## Root

The root should contain only product-level entry points, config, and major
folders. Raw course inputs do not belong at root.

## Folders

| Path | Purpose |
|---|---|
| `raw/course-1/` | Original first course pack files. |
| `raw/course-2/` | Original second course pack files, including Q-eval images. |
| `raw/extracted-text/` | OCR/text extraction outputs from raw PDFs. |
| `raw/private/` | Local private course-adjacent files that should not be used as public docs. |
| `Wiki/wiki/` | Curated curriculum notes. |
| `Wiki/wiki/lessons/` | Student-facing lesson source files. |
| `Wiki/assets/images/` | Images and diagrams used by wiki and HTML lessons. |
| `rendered/` | Generated HTML, safe to regenerate. |
| `scripts/legacy-extraction/` | One-off historical extraction helpers. |
| `docs/` | Maintainer-facing documentation. |

## Cleanup Policy

- Delete OS metadata such as `.DS_Store`.
- Keep generated HTML only if useful for direct local preview.
- Do not delete raw course PDFs unless there is a confirmed duplicate and a
  retained source-of-truth copy.
