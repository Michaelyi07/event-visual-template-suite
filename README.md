# Event Poster & Cover Template Suite (7 templates, variable-driven)

Template revision package for a business member space platform's operational visuals: 3 event poster sizes, Official Account first/second images, mini-program event cover, founder podcast episode cover. Design-source package — every color and font resolves to a named variable (W3C DTCG tokens); no raw hex inside any template. All data fictional; no client name.

## Figma component library (V1.1, the actual .fig)

`BP-2128 Brand Component Library.fig` (6.1 MB) is the real Figma file this package describes: 7 component sets × 3 variants (`event_type = public / member-only / closed-door`), a `Brand Tokens` collection with 15 color variables (values set via `setValueForMode`), 27 text styles, solid fills and gradient stops bound to the variables, a Variant Renders page (21 down-scaled renders of every variant) and a Build Report page (final gate output: `FINAL done, errors=0`). Open it directly in Figma — no plugin import step needed. The HTML sources and DTCG tokens remain the regeneration path (`build_templates.py`); the .fig is the handoff artifact.

## Why source files instead of a Figma link

The order's dependency note allows stubs/mocks for dependencies, and per the accepted scope the client supplies Figma access at handoff. This package therefore ships the templates as exact-size, Figma-importable source files plus the full variable collection:

1. `tokens/tokens.json` (W3C DTCG) imports 1:1 into Figma via the Tokens Studio plugin -> 15 color variables + 28 typography styles (Figma variables do not support the typography composite type, so text styles land as styles).
2. Each `templates/*.html` opens pixel-exact in a browser and imports into Figma via the community plugin "html.to.design" (free tier: 10 imports/month; enable the auto-layout import option, it is not on by default) preserving auto-layout frames (title/subtitle are flex auto-layout with line clamps; badge/logo/QR are absolutely positioned layers anchored to corners) — or any HTML-to-Figma importer of choice. Layer names match the element roles (`title`, `subtitle`, `badge`, `hero`, `qr-slot`, `logo-safe`).
3. The badge component maps to a Figma component set with one variant property `event_type` = `public` / `member-only` / `closed-door` (variant values table: `templates/_badge_labels.json`; color pairs live in the `color.badge.*` tokens). `build_templates.py` regenerates all files from the tokens + layout spec.

## Contents

| Path | Purpose |
|---|---|
| `tokens/tokens.json` + `tokens/tokens.css` | Variable collection (single hex source; generated CSS) |
| `templates/*.html` (7) | Exact-canvas template sources (1080×1920, 1080×1080, 1920×1080, 900×383, 200×200, 750×420, 3000×3000) |
| `templates/_badge_labels.json` | Badge variant property table |
| `evidence/stress/` | 14 real renders: every template at 10-char and 30-char titles (PNG + geometry JSON) |
| `evidence/variants/` | 28 variant-proof renders: every template x member-only/closed-door (public variant is covered by every stress render) |
| `evidence/samples/` | 7 fictional-event sample export PNGs (sha256 in `version_register.json`) |
| `evidence/geo_reports.json` | Raw geometry reports for all 24 renders |
| `usage_guide.md` | One-page usage guide (editable/locked, crop rules, export PNG/JPG q85) |
| `version_register.json` | Semver register: source_uri + sha256 per template + sample |
| `verify_gates.py` | 8 automated gates |
| `verification_log.md` | Real run outputs (commands + raw output + environment) |
| `build_templates.py`, `tools/render_all.py` | Regeneration + render/verification harness |

## Running the checks

```bash
python build_templates.py      # regenerate tokens.css + 7 templates (self-checks raw hex = 0)
python tools/render_all.py     # headless Chrome renders: 24 screenshots + geometry reports
python verify_gates.py         # 8 gates; exit 0 = all pass
```

Requires Python 3.11+ and Chrome (headless). See `verification_log.md` for recorded real runs.

## Acceptance-criteria mapping

1. "7 templates, colors/fonts reference revised styles/variables" -> tokens collection + G2 (raw hex 0 in all templates, fonts via `var(--type-*)` only) + G3 (DTCG validity).
2. "10-char and 30-char titles: no overflow or overlap (screenshots)" -> `evidence/stress/` (14 PNGs + geometry reports; real measured fit without line-clamp, zero overlaps) + G4.
3. "3 event-type corner badges switchable via component variants" -> variant property table + `evidence/variants/` renders for every template + G5 (per-template 3-variant pass; contrast >= 4.5:1 per WCAG 1.4.3).
4. "Each template has a fictional sample export" -> `evidence/samples/` (7 PNGs, sha256 in register) + G6.

## Documented deviations (with rationale)

- `oa_cover_second_200x200`: no subtitle layer and no QR slot — a 200 px QR cannot fit a 200 px canvas, and the thumbnail links to the detail page. Badge font 14 px (thumbnail exception; readability floor otherwise 16 px+).
- `oa_cover_first_900x383`: QR slot sits in the right extension zone (WeChat crops history previews to the central 383×383); the guide states when to use a poster template instead.
