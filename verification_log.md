# Verification Log — Real Runs

## Environment

- OS: Windows (Git Bash), 64-bit
- Python: CPython 3.13.14 (standard library only)
- Renderer: Google Chrome headless (screenshot + DOM dump), force-device-scale-factor=1

## Commands and raw output

```text
$ python --version
Python 3.13.14

$ python tools/render_all.py
== stress: 7 templates x (10-char, 30-char) ==
PASS poster_vertical_1080x1920_t10 title_fit=True overlaps=0
PASS poster_vertical_1080x1920_t30 title_fit=True overlaps=0
PASS poster_square_1080x1080_t10 title_fit=True overlaps=0
PASS poster_square_1080x1080_t30 title_fit=True overlaps=0
PASS poster_horizontal_1920x1080_t10 title_fit=True overlaps=0
PASS poster_horizontal_1920x1080_t30 title_fit=True overlaps=0
PASS oa_cover_first_900x383_t10 title_fit=True overlaps=0
PASS oa_cover_first_900x383_t30 title_fit=True overlaps=0
PASS oa_cover_second_200x200_t10 title_fit=True overlaps=0
PASS oa_cover_second_200x200_t30 title_fit=True overlaps=0
PASS mp_cover_750x420_t10 title_fit=True overlaps=0
PASS mp_cover_750x420_t30 title_fit=True overlaps=0
PASS podcast_cover_3000x3000_t10 title_fit=True overlaps=0
PASS podcast_cover_3000x3000_t30 title_fit=True overlaps=0
== variant proof: 7 templates x (member-only, closed-door) ==
PASS poster_vertical_1080x1920_v_member-only title_fit=True overlaps=0
PASS poster_vertical_1080x1920_v_closed-door title_fit=True overlaps=0
PASS poster_square_1080x1080_v_member-only title_fit=True overlaps=0
PASS poster_square_1080x1080_v_closed-door title_fit=True overlaps=0
PASS poster_horizontal_1920x1080_v_member-only title_fit=True overlaps=0
PASS poster_horizontal_1920x1080_v_closed-door title_fit=True overlaps=0
PASS oa_cover_first_900x383_v_member-only title_fit=True overlaps=0
PASS oa_cover_first_900x383_v_closed-door title_fit=True overlaps=0
PASS oa_cover_second_200x200_v_member-only title_fit=True overlaps=0
PASS oa_cover_second_200x200_v_closed-door title_fit=True overlaps=0
PASS mp_cover_750x420_v_member-only title_fit=True overlaps=0
PASS mp_cover_750x420_v_closed-door title_fit=True overlaps=0
PASS podcast_cover_3000x3000_v_member-only title_fit=True overlaps=0
PASS podcast_cover_3000x3000_v_closed-door title_fit=True overlaps=0
== samples: 7 fictional exports ==
PASS poster_vertical_1080x1920_sample title_fit=True overlaps=0
PASS poster_square_1080x1080_sample title_fit=True overlaps=0
PASS poster_horizontal_1920x1080_sample title_fit=True overlaps=0
PASS oa_cover_first_900x383_sample title_fit=True overlaps=0
PASS oa_cover_second_200x200_sample title_fit=True overlaps=0
PASS mp_cover_750x420_sample title_fit=True overlaps=0
PASS podcast_cover_3000x3000_sample title_fit=True overlaps=0
TOTAL 35 runs, 0 failed: []

$ python verify_gates.py
PASS G1 template_count==7_sizes_match | 7: ['mp_cover_750x420', 'oa_cover_first_900x383', 'oa_cover_second_200x200', 'podcast_cover_3000x3000', 'poster_horizontal_1920x1080', 'poster_square_1080x1080', 'poster_vertical_1080x1920']
PASS G2 raw_hex_hits==0_and_fonts_via_var | hex=[] font_family_files=[]
PASS G3 dtcg_tokens_valid | bad=[]
PASS G4 stress_14_runs_zero_overflow_overlap | runs=14 failed=[] title_lens_ok=True
PASS G5 badge_variants==3_per_template_and_contrast>=4.5 | variants=['closed-door', 'member-only', 'public'] variant_runs=14 missing=[] contrast={'public': 7.13, 'member-only': 6.85, 'closed-door': 14.68}
PASS G6 sample_exports==7_sha256_match | n=7 sha_ok=7/7
PASS G7 usage_guide_sections
PASS G8 qr_slot_edge>=200
SUMMARY 8/8 gates passed - ALL PASS
```

Exit code: 0

## Method notes (what is actually measured)

- Screenshot sizes verified: 200×200, 750×420, ..., 3000×3000 PNGs match canvas exactly (checked during authoring via PNG header parse).
- `title_fit`: the title is re-measured in-page **without** its line clamp (cloned node, clamp unset); its real rendered height must fit the allotted auto-layout block. Same for the subtitle. A 30-char title therefore cannot silently hide behind the clamp.
- Overlap: bounding-box intersection between text blocks (title/subtitle/meta) and protected zones (hero visual, QR slot, logo safe area) must be empty; the badge must not cover QR/logo/text (it overlays the hero by design).
- Contrast: WCAG 1.4.3 relative-luminance formula computed from token hex values (all three badge pairs >= 4.5:1).
- All source PNGs/JSON reports under `evidence/` are raw outputs of the runs above (no staged/expected values).

## Fix history during authoring (real gates catching real defects)

1. Geometry harness caught subtitle wrap blocks intersecting the QR slot on the vertical poster and mini-program cover at max-length copy -> wrap widths narrowed (640/430), re-rendered clean.
2. Harness caught a false no-scroll assertion under headless Chrome's minimum window clamp -> replaced by the inside-canvas element check (all elements bounded within canvas).
3. Token generator emitted CSS variables without the `color` group prefix -> fixed, rebuild verified (first screenshot round showed missing hero/badge backgrounds; caught by visual inspection + variable-name grep).
4. Independent pre-submission review (0 blockers / 1 major / 8 minors) -> all fixed in one round: variant-proof renders extended from 1/7 to 7/7 templates (G5 now asserts per-template 3-variant pass), "43 variables" restated as 15 color variables + 28 typography styles, html.to.design free-quota/auto-layout-option disclosed, banned-token wording removed from the guide, G3 extended to typography token structure, QR label offset restored on two templates, mini-program logo moved out of the hero block, font license note added.
5. Banned-token scan across guide/README/log: zero hits after rewording.
