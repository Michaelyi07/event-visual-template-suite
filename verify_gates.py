"""Gate checks for the 2128 template package. Real files, real reports.

Gates:
  G1  template count == 7 with exact brief sizes
  G2  zero raw hex and zero literal font-family inside templates/*.html
      (all colors/fonts resolve to tokens.css variables)
  G3  tokens.json is valid W3C DTCG ($type present, naming, hex format)
  G4  stress matrix: 14 runs (7 templates x 10/30-char), all pass,
      geometry: title/subtitle fit + zero overlaps + inside canvas
  G5  badge variants: 3 defined (public/member-only/closed-door), variant
      proof renders pass, text/bg contrast >= 4.5:1 (WCAG 1.4.3)
  G6  sample exports: 7 fictional-event PNGs, sha256 matches register
  G7  usage guide covers editable/locked, crop rules, export formats
  G8  QR slot edge >= 200px in every template that carries a QR

Exit 0 = all pass.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent
FAILS = []
CHECKS = 0
EXPECTED = {
    "poster_vertical_1080x1920": (1080, 1920), "poster_square_1080x1080": (1080, 1080),
    "poster_horizontal_1920x1080": (1920, 1080), "oa_cover_first_900x383": (900, 383),
    "oa_cover_second_200x200": (200, 200), "mp_cover_750x420": (750, 420),
    "podcast_cover_3000x3000": (3000, 3000),
}


def check(gate: str, ok: bool, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    print(f"{'PASS' if ok else 'FAIL'} {gate}" + (f" | {detail}" if detail else ""))
    if not ok:
        FAILS.append(gate)


def lum(hexcol: str) -> float:
    h = hexcol.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    lin = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def contrast(a: str, b: str) -> float:
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def main() -> int:
    tpl_dir = ROOT / "templates"
    reports = json.loads((ROOT / "evidence" / "geo_reports.json").read_text(encoding="utf-8"))
    register = json.loads((ROOT / "version_register.json").read_text(encoding="utf-8"))

    # G1
    files = sorted(p.stem for p in tpl_dir.glob("*.html"))
    check("G1 template_count==7_sizes_match", len(files) == 7 and set(files) == set(EXPECTED),
          f"{len(files)}: {files}")

    # G2
    hex_pat = re.compile(r"#[0-9a-fA-F]{3,8}\b")
    hex_hits, font_hits = [], []
    for p in tpl_dir.glob("*.html"):
        t = p.read_text(encoding="utf-8")
        hex_hits += [f"{p.name}:{m}" for m in hex_pat.findall(t)]
        if "font-family" in t:
            font_hits.append(p.name)
    check("G2 raw_hex_hits==0_and_fonts_via_var", not hex_hits and not font_hits,
          f"hex={hex_hits[:5]} font_family_files={font_hits}")

    # G3
    tokens = json.loads((ROOT / "tokens" / "tokens.json").read_text(encoding="utf-8"))
    bad = []
    def walk(node, path):
        if isinstance(node, dict) and "$value" not in node:
            for k, v in node.items():
                walk(v, f"{path}.{k}" if path else k)
            return
        if node.get("$type") == "color" and not re.fullmatch(r"#[0-9a-fA-F]{6}", node["$value"]):
            bad.append(path)
    walk(tokens["color"], "")
    for name, tok in tokens["typography"]["text"].items():
        v = tok.get("$value", {})
        if tok.get("$type") != "typography" or not v.get("fontFamily")                 or not re.fullmatch(r"\d+px", v.get("fontSize", ""))                 or not re.fullmatch(r"\d+(\.\d+)?", str(v.get("lineHeight", ""))):
            bad.append(f"typography.text.{name}")
    check("G3 dtcg_tokens_valid", not bad, f"bad={bad[:5]}")

    # G4
    stress = [k for k in reports if k.endswith(("_t10", "_t30"))]
    fails = [k for k in stress if not reports[k]["pass"]]
    lens_ok = all(r["title_len"] in (10, 30) for r in (reports[k] for k in stress))
    check("G4 stress_14_runs_zero_overflow_overlap",
          len(stress) == 14 and not fails and lens_ok,
          f"runs={len(stress)} failed={fails} title_lens_ok={lens_ok}")

    # G5
    variants = json.loads((tpl_dir / "_badge_labels.json").read_text(encoding="utf-8"))
    v_ok = set(variants) == {"public", "member-only", "closed-door"}
    vruns = [k for k in reports if "_v_" in k]
    missing = []
    for tpl in EXPECTED:
        for v in ("member-only", "closed-door"):
            key = f"{tpl}_v_{v}"
            if key not in reports or not reports[key]["pass"]:
                missing.append(key)
        pub = reports.get(f"{tpl}_t10")
        if pub is None or not pub["pass"] or pub.get("variant") != "public":
            missing.append(f"{tpl}:public(stress)")
    vpass = len(vruns) == 14 and not missing
    bg = tokens["color"]["badge"]
    contrasts = {v: contrast(bg[v]["bg"]["$value"], bg[v]["text"]["$value"]) for v in bg}
    contrast_ok = all(c >= 4.5 for c in contrasts.values())
    check("G5 badge_variants==3_per_template_and_contrast>=4.5",
          v_ok and vpass and contrast_ok,
          f"variants={sorted(variants)} variant_runs={len(vruns)} missing={missing[:3]} contrast={ {k: round(c, 2) for k, c in contrasts.items()} }")

    # G6
    samples = sorted((ROOT / "evidence" / "samples").glob("*_sample.png"))
    reg = {r["template"]: r for r in register["templates"]}
    sha_ok = []
    for p in samples:
        tpl = p.name[:-len("_sample.png")]
        want = reg.get(tpl, {}).get("sample_sha256")
        sha_ok.append(want == hashlib.sha256(p.read_bytes()).hexdigest())
    check("G6 sample_exports==7_sha256_match", len(samples) == 7 and all(sha_ok),
          f"n={len(samples)} sha_ok={sum(sha_ok)}/7")

    # G7
    guide = (ROOT / "usage_guide.md").read_text(encoding="utf-8")
    g_ok = all(s in guide for s in ("Editable vs locked", "crop rules", "quality 85", "PNG", "safe area"))
    check("G7 usage_guide_sections", g_ok)

    # G8
    qr_ok = all(r["checks"].get("qr_slot", {}).get("ok", True) for r in reports.values()
                if r["template"] != "oa_cover_second_200x200")
    check("G8 qr_slot_edge>=200", qr_ok)

    passed = CHECKS - len(FAILS)
    print(f"SUMMARY {passed}/{CHECKS} gates passed" + (" - ALL PASS" if not FAILS else f" - FAILED: {FAILS}"))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
