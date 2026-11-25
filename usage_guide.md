# Template Usage Guide — Event Poster & Cover Suite (v1.0.0)

One page. Applies to all 7 templates in `templates/`. All colors and fonts resolve to the variable collection in `tokens/` (W3C DTCG `tokens.json` + generated `tokens.css`); never hard-code a hex value or font name in a template.

## 1. Editable vs locked elements

| Element | Editable? | Notes |
|---|---|---|
| Title (`#title`) | Yes, 10–30 CJK chars | Auto-layout fill width + line clamp; verified no overflow at 10 and 30 chars (see `verification_log.md`) |
| Subtitle (`#subtitle`) | Yes, 0–40 CJK chars | Optional; leave empty to hide. **Exception: `oa_cover_second_200x200` has no subtitle layer** (thumbnail use case; documented deviation) |
| Badge (`#badge`) | Variant only | Switch component property `event_type`: `public` (公开活动) / `member-only` (会员专享) / `closed-door` (闭门会). Text + colors switch together from the variant table; do not free-type badge text |
| Meta line (`.meta`) | Yes | Date / venue / host; fictional sample values |
| Hero visual (`.hero`) | Image slot only | Replace the sample shapes with the event hero image; keep the block geometry. Decorative shapes are locked |
| QR slot (`.qr-slot`) | Image swap only | Replace the sample checkerboard with the real QR code at the same size and position. Slot edge is >= 200 px in all templates that carry a QR. **Exception: `oa_cover_second_200x200` has no QR slot** (a 200 px QR cannot fit a 200 px canvas; the thumbnail links to the detail page instead) |
| Logo safe area (`.logo-safe`) | Logo swap only | Keep the mark inside the marked safe area; never stretch or recolor |

## 2. Image crop rules

- Hero images: fill the hero block (cover fit); keep the subject centered within the middle 80% of the block — edges may be cropped by the block's rounded corners.
- `oa_cover_first_900x383`: WeChat crops history/share previews to the central ~383×383 square. Keep the badge, title and subtitle inside the central zone; the QR slot sits in the right extension zone and may be invisible in the cropped preview (first-image use cases normally carry no QR; use a poster template when a QR is required).
- `mp_cover_750x420`: page banner size. For the WeChat share card (5:4), re-export from the same tokens with the core content inside the central 1:1 zone.
- `podcast_cover_3000x3000`: keep all text inside the central safe area (Apple player UI overlays the bottom edge; QR and logo are placed accordingly).

## 3. Export rules

- Format: **PNG**, or **JPG at quality 85** when file weight matters (podcast covers must be non-transparent: PNG or JPG, no alpha).
- Export at exactly 1x canvas size: 1080×1920 / 1080×1080 / 1920×1080 / 900×383 / 200×200 / 750×420 / 3000×3000.
- Fonts: the stack is Source Han Sans SC / Noto Sans SC (both SIL OFL) / Microsoft YaHei / PingFang SC. Install one of the first two on authoring machines; if only the generic sans-serif fallback resolves, text metrics may drift and the 30-char fit must be re-verified.
- Do not scale text or elements after export; if the title does not fit, shorten the title (10–30 chars) rather than shrinking the font below the template's text style.

## 4. Versioning

Each template carries semantic version in `version_register.json` (PATCH = color/copy via tokens, MINOR = layout change, MAJOR = canvas size change). A published version requires `source_uri` + matching `sha256`; a failed gate rolls back to the last published version.
