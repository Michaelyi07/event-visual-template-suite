"""Build the 7 event-visual templates as exact-size HTML source files + tokens.css.

Architecture (mirrors the Figma variable model 1:1):
  tokens/tokens.json  - W3C DTCG design tokens (single hex source, imports to Tokens Studio)
  tokens/tokens.css   - generated: CSS custom properties (the "variable collection")
  templates/*.html    - component sources; every color/font is var(...) only (raw-hex scan = 0)
- Text areas are flex auto-layout with line clamp; an embedded geometry script
  measures real rendered fit (title without clamp must fit its block) and box
  overlaps, writing a JSON report used by the gates.
- Badge variant switching: ?v=public|member-only|closed-door sets
  html[data-variant] -> badge bg/text + label via the variant property table.
- Query params: t=title text, s=subtitle text (s= hides subtitle), v=variant.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "templates"
OUT.mkdir(exist_ok=True)
TOKENS = json.loads((ROOT / "tokens" / "tokens.json").read_text(encoding="utf-8"))

BADGE_LABELS = {"public": "公开活动", "member-only": "会员专享", "closed-door": "闭门会"}


def hex_to_css_var_name(dotted: str) -> str:
    return "--" + dotted.replace(".", "-")


def collect_vars() -> dict:
    """Flatten DTCG tokens into CSS custom properties."""
    vars_ = {}
    colors = TOKENS["color"]

    def walk(node, path):
        if isinstance(node, dict) and "$value" not in node:
            for k, v in node.items():
                walk(v, f"{path}.{k}" if path else k)
            return
        if node.get("$type") == "color":
            vars_[hex_to_css_var_name(path)] = node["$value"]
    walk(colors, "color")

    typ = TOKENS["typography"]
    fam = ", ".join(f'"{f}"' for f in typ["font"]["sans"]["$value"])
    vars_["--typography-font-sans"] = fam
    for name, tok in typ["text"].items():
        v = tok["$value"]
        vars_[f"--type-{name}"] = (
            f'{v["fontWeight"]} {v["fontSize"]}/{v["lineHeight"]} var(--typography-font-sans)'
        )
    return vars_


def write_tokens_css() -> None:
    vars_ = collect_vars()
    lines = ["/* Generated from tokens/tokens.json (W3C DTCG) - the single hex source.",
             "   In Figma these import as the variable collection via Tokens Studio. */",
             ":root {"]
    for k in sorted(vars_):
        lines.append(f"  {k}: {vars_[k]};")
    lines.append("}")
    (ROOT / "tokens" / "tokens.css").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"tokens.css: {len(vars_)} variables")


GEO_JS = r"""
<script>
(function(){
  const q = new URLSearchParams(location.search);
  const VARIANTS = %VARIANTS%;
  const v = q.get('v') || 'public';
  const t = q.get('t');
  const s = q.get('s');
  document.documentElement.dataset.variant = v;
  const titleEl = document.getElementById('title');
  const subEl = document.getElementById('subtitle');
  const badgeEl = document.getElementById('badge');
  if (t !== null && t !== '') titleEl.textContent = t;
  if (s !== null) {
    if (s === '') { subEl.style.display = 'none'; }
    else { subEl.textContent = s; }
  }
  if (badgeEl) badgeEl.textContent = VARIANTS[v];

  function rectsOverlap(a, b) {
    return !(a.right <= b.left + 0.5 || b.right <= a.left + 0.5 ||
             a.bottom <= b.top + 0.5 || b.bottom <= a.top + 0.5);
  }
  function rect(el) { return el.getBoundingClientRect(); }

  function report() {
    const rep = {
      template: document.body.dataset.template,
      size: [document.body.offsetWidth, document.body.offsetHeight],
      variant: v,
      title_len: titleEl.textContent.length,
      subtitle_len: (subEl.style.display === 'none' ? 0 : subEl.textContent.length),
      checks: {}
    };
    const wrap = titleEl.closest('.title-wrap');
    const clone = titleEl.cloneNode(true);
    clone.style.cssText = '-webkit-line-clamp:unset;position:absolute;visibility:hidden;width:' +
      (titleEl.clientWidth) + 'px;margin:0;';
    document.body.appendChild(clone);
    const neededH = clone.offsetHeight;
    clone.remove();
    rep.checks.title_fit = { needed_h: neededH, avail_h: wrap.clientHeight, ok: neededH <= wrap.clientHeight + 1 };
    if (subEl.style.display !== 'none' && subEl.textContent.length > 0) {
      const swrap = subEl.closest('.subtitle-wrap');
      const sclone = subEl.cloneNode(true);
      sclone.style.cssText = '-webkit-line-clamp:unset;position:absolute;visibility:hidden;width:' +
        (subEl.clientWidth) + 'px;margin:0;';
      document.body.appendChild(sclone);
      const sNeeded = sclone.offsetHeight;
      sclone.remove();
      rep.checks.subtitle_fit = { needed_h: sNeeded, avail_h: swrap.clientHeight, ok: sNeeded <= swrap.clientHeight + 1 };
    }
    const movers = { title: titleEl.closest('.title-wrap') };
    if (subEl.style.display !== 'none' && subEl.textContent.length > 0) movers.subtitle = subEl.closest('.subtitle-wrap');
    const meta = document.querySelector('.meta');
    if (meta) movers.meta = meta;
    const prot = {};
    const hero = document.querySelector('.hero');
    if (hero) prot.hero = hero;
    const qr = document.querySelector('.qr-slot');
    if (qr) prot.qr_slot = qr;
    const logo = document.querySelector('.logo-safe');
    if (logo) prot.logo_safe = logo;
    const overlaps = [];
    for (const mn in movers) for (const pn in prot) {
      if (rectsOverlap(rect(movers[mn]), rect(prot[pn]))) overlaps.push(mn + 'x' + pn);
    }
    if (badgeEl) for (const pn in prot) {
      if (pn === 'hero') continue;
      if (rectsOverlap(rect(badgeEl), rect(prot[pn]))) overlaps.push('badgex' + pn);
    }
    rep.checks.overlaps = { count: overlaps.length, pairs: overlaps };
    if (qr) rep.checks.qr_slot = { edge: qr.offsetWidth, ok: qr.offsetWidth >= 200 };
    let inside = true;
    const W = document.body.offsetWidth, H = document.body.offsetHeight;
    document.querySelectorAll('.title-wrap,.subtitle-wrap,.meta,.qr-slot,.logo-safe,.hero,#badge').forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.left < -1 || r.top < -1 || r.right > W + 1 || r.bottom > H + 1) inside = false;
    });
    rep.checks.inside_canvas = inside;
    // note: document-level scroll probes are unreliable under headless Chrome's
    // minimum window clamp (>=500px); overflow containment is guaranteed by
    // html/body overflow:hidden plus the inside_canvas element check above.
    rep.pass = rep.checks.title_fit.ok &&
               (rep.checks.subtitle_fit ? rep.checks.subtitle_fit.ok : true) &&
               rep.checks.overlaps.count === 0 &&
               (rep.checks.qr_slot ? rep.checks.qr_slot.ok : true) &&
               rep.checks.inside_canvas;
    document.getElementById('geo-report').textContent = JSON.stringify(rep);
    document.title = 'GEOREPORT';
  }
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(() => setTimeout(report, 80));
  } else { setTimeout(report, 400); }
})();
</script>
"""

HTML_HEAD = """<!DOCTYPE html>
<html lang="zh-CN" data-variant="public">
<head>
<meta charset="utf-8">
<title>{name}</title>
<link rel="stylesheet" href="../tokens/tokens.css">
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: {w}px; height: {h}px; overflow: hidden; }}
body {{
  position: relative;
  background: var(--color-neutral-0);
  font: var(--type-meta);
  color: var(--color-neutral-900);
}}
.hero {{ position: absolute; overflow: hidden; border-radius: {hero_radius}px;
  background: linear-gradient(135deg, var(--color-brand-primary-700) 0%, var(--color-brand-primary-600) 62%, var(--color-brand-primary-500) 100%); }}
.hero .deco-1 {{ position: absolute; width: {deco1}px; height: {deco1}px; border-radius: 50%;
  border: {deco_border}px solid var(--color-brand-accent-gold-500); opacity: .55; }}
.hero .deco-2 {{ position: absolute; width: {deco2}px; height: {deco2}px; border-radius: 50%;
  background: var(--color-brand-primary-500); opacity: .35; }}
.hero .deco-3 {{ position: absolute; width: {deco3}px; height: {deco3}px; border-radius: {deco_radius}px;
  background: var(--color-neutral-0); opacity: .08; }}
#badge {{
  position: absolute; display: inline-flex; align-items: center;
  padding: {badge_pad_v}px {badge_pad_h}px; border-radius: 999px;
  background: var(--color-badge-public-bg);
  color: var(--color-badge-public-text);
  font: var(--{badge_style}); letter-spacing: 2px; white-space: nowrap;
}}
html[data-variant="member-only"] #badge {{ background: var(--color-badge-member-only-bg); color: var(--color-badge-member-only-text); }}
html[data-variant="closed-door"] #badge {{ background: var(--color-badge-closed-door-bg); color: var(--color-badge-closed-door-text); }}
.title-wrap {{ position: absolute; display: flex; flex-direction: column; justify-content: center; }}
#title {{
  font: var(--{title_style});
  color: var(--color-neutral-900);
  width: 100%;
  display: -webkit-box; -webkit-box-orient: vertical;
  -webkit-line-clamp: {title_clamp}; overflow: hidden;
}}
.subtitle-wrap {{ position: absolute; }}
#subtitle {{
  font: var(--{subtitle_style});
  color: var(--color-neutral-700);
  width: 100%;
  display: -webkit-box; -webkit-box-orient: vertical;
  -webkit-line-clamp: {subtitle_clamp}; overflow: hidden;
}}
.meta {{
  position: absolute; font: var(--{meta_style});
  color: var(--color-neutral-700);
}}
.meta b {{ color: var(--color-brand-primary-700); font-weight: 700; }}
.qr-slot {{
  position: absolute; border-radius: 16px;
  background: var(--color-neutral-100);
  border: 2px dashed var(--color-neutral-500);
  display: flex; align-items: center; justify-content: center;
}}
.qr-slot .qr-inner {{ width: {qr_inner}%; height: {qr_inner}%; border-radius: 8px;
  background:
    repeating-conic-gradient(var(--color-neutral-900) 0% 25%, var(--color-neutral-0) 0% 50%)
    0 0 / {qr_mod}px {qr_mod}px;
  opacity: .85; }}
.qr-slot .qr-label {{ position: absolute; bottom: -{qr_label_off}px; left: 0; right: 0; text-align: center;
  font: var(--{qr_label_style}); color: var(--color-neutral-500); }}
.logo-safe {{
  position: absolute; display: flex; align-items: center; gap: 12px;
  color: var(--color-neutral-500); font: var(--{logo_style});
  letter-spacing: 3px;
}}
.logo-safe .logo-mark {{ width: {logo_mark}px; height: {logo_mark}px; border-radius: {logo_mark_radius}px;
  background: var(--color-brand-primary-600); position: relative; }}
.logo-safe .logo-mark::after {{ content: ""; position: absolute; inset: 30%;
  border-radius: 50%; background: var(--color-brand-accent-gold-500); }}
</style>
</head>
<body data-template="{name}">
"""


def emit(name: str, spec: dict) -> None:
    w, h = spec["w"], spec["h"]
    html = HTML_HEAD.format(
        name=name, w=w, h=h,
        hero_radius=spec.get("hero_radius", 24),
        deco1=spec["deco1"], deco2=spec["deco2"], deco3=spec["deco3"],
        deco_border=spec.get("deco_border", 6), deco_radius=spec.get("deco_radius", 48),
        badge_pad_v=spec["badge_pad_v"], badge_pad_h=spec["badge_pad_h"],
        badge_style=spec["badge_style"],
        title_style=spec["title_style"], title_clamp=spec["title_clamp"],
        subtitle_style=spec.get("subtitle_style", "subtitle-md"),
        subtitle_clamp=spec.get("subtitle_clamp", 2),
        meta_style=spec.get("meta_style", "meta"),
        qr_inner=spec.get("qr_inner", 78), qr_mod=spec.get("qr_mod", 12),
        qr_label_off=spec.get("qr_label_off", 26),
        qr_label_style=spec.get("qr_label_style", "type-caption"),
        logo_style=spec.get("logo_style", "logo-md"),
        logo_mark=spec.get("logo_mark", 44), logo_mark_radius=spec.get("logo_mark_radius", 12),
    )
    hx, hy, hw, hh = spec["hero"]
    html += (f'<div class="hero" style="left:{hx}px;top:{hy}px;width:{hw}px;height:{hh}px;">\n'
             f'  <div class="deco-1" style="left:{spec["deco_pos"][0]}px;top:{spec["deco_pos"][1]}px;"></div>\n'
             f'  <div class="deco-2" style="left:{spec["deco_pos"][2]}px;top:{spec["deco_pos"][3]}px;"></div>\n'
             f'  <div class="deco-3" style="left:{spec["deco_pos"][4]}px;top:{spec["deco_pos"][5]}px;"></div>\n'
             f'</div>\n')
    html += f'<div id="badge" style="left:{spec["badge"][0]}px;top:{spec["badge"][1]}px;">公开活动</div>\n'
    tx, ty, tw, th = spec["title_wrap"]
    html += (f'<div class="title-wrap" style="left:{tx}px;top:{ty}px;width:{tw}px;height:{th}px;">\n'
             f'  <div id="title">示例产业沙龙</div>\n</div>\n')
    if spec.get("subtitle_wrap"):
        sx, sy, sw, sh = spec["subtitle_wrap"]
        html += (f'<div class="subtitle-wrap" style="left:{sx}px;top:{sy}px;width:{sw}px;height:{sh}px;">\n'
                 f'  <div id="subtitle">面向会员企业代表的产业资源对接与商务合作交流活动</div>\n</div>\n')
    else:
        html += '<div class="subtitle-wrap" style="display:none;"><div id="subtitle"></div></div>\n'
    if spec.get("meta"):
        mx, my, mw, mh = spec["meta"]
        html += (f'<div class="meta" style="left:{mx}px;top:{my}px;width:{mw}px;height:{mh}px;">'
                 f'{spec["meta_html"]}</div>\n')
    if spec.get("qr"):
        qx, qy, qw, qh = spec["qr"]
        html += (f'<div class="qr-slot" style="left:{qx}px;top:{qy}px;width:{qw}px;height:{qh}px;">'
                 f'<div class="qr-inner"></div>'
                 f'<div class="qr-label">扫码报名</div></div>\n')
    if spec.get("logo"):
        lx, ly, lw, lh = spec["logo"]
        html += (f'<div class="logo-safe" style="left:{lx}px;top:{ly}px;width:{lw}px;height:{lh}px;">'
                 f'<div class="logo-mark"></div><span>示例空间</span></div>\n')
    html += '<pre id="geo-report" style="display:none;"></pre>\n'
    html += GEO_JS.replace("%VARIANTS%", json.dumps(BADGE_LABELS, ensure_ascii=False))
    html += "\n</body>\n</html>\n"
    (OUT / f"{name}.html").write_text(html, encoding="utf-8")
    # self-check: no raw hex and no font-family literal inside the template
    hex_hits = re.findall(r"#[0-9a-fA-F]{3,8}\b", html)
    assert not hex_hits, f"{name}: raw hex found {hex_hits}"
    assert "font-family" not in html, f"{name}: literal font-family found"
    print(f"built {name}.html ({len(html)} chars, gates clean)")


TEMPLATES = {
    "poster_vertical_1080x1920": dict(
        w=1080, h=1920,
        hero=(80, 80, 920, 980), deco1=320, deco2=180, deco3=420, deco_border=8, deco_radius=64,
        deco_pos=(560, 120, 700, 620, 180, 660),
        badge=(104, 104), badge_pad_v=12, badge_pad_h=24, badge_style="type-badge-lg",
        title_wrap=(80, 1100, 920, 330), title_style="type-display-poster", title_clamp=3,
        subtitle_wrap=(80, 1450, 640, 96), subtitle_style="type-subtitle-lg", subtitle_clamp=2,
        meta=(80, 1560, 620, 90), meta_style="type-meta",
        meta_html='<b>2027-03-18 14:00</b><br>示例城市 · 示例园区国际会议中心',
        qr=(760, 1480, 240, 240),
        logo=(80, 1780, 400, 100), logo_style="type-logo-lg", logo_mark=56, logo_mark_radius=14,
    ),
    "poster_square_1080x1080": dict(
        w=1080, h=1080,
        hero=(72, 72, 936, 420), deco1=180, deco2=110, deco3=220, deco_border=6, deco_radius=40,
        deco_pos=(600, 60, 740, 240, 140, 220),
        badge=(92, 92), badge_pad_v=10, badge_pad_h=20, badge_style="type-badge-md",
        title_wrap=(72, 532, 936, 300), title_style="type-display-square", title_clamp=3,
        subtitle_wrap=(72, 852, 640, 84), subtitle_style="type-subtitle-md", subtitle_clamp=2,
        meta=(72, 956, 640, 44), meta_style="type-meta-square",
        meta_html='<b>2027-03-18 14:00</b> · 示例园区国际会议中心',
        qr=(788, 838, 220, 220), qr_inner=78, qr_mod=11,
        logo=(72, 1000, 300, 60), logo_style="type-logo-sm", logo_mark=40, logo_mark_radius=10,
    ),
    "poster_horizontal_1920x1080": dict(
        w=1920, h=1080,
        hero=(0, 0, 1120, 1080), deco1=340, deco2=200, deco3=460, deco_border=8, deco_radius=64,
        hero_radius=0,
        deco_pos=(640, 100, 820, 620, 200, 160),
        badge=(1184, 64), badge_pad_v=10, badge_pad_h=20, badge_style="type-badge-md",
        title_wrap=(1184, 150, 672, 200), title_style="type-display-wide", title_clamp=3,
        subtitle_wrap=(1184, 370, 672, 96), subtitle_style="type-subtitle-md", subtitle_clamp=2,
        meta=(1184, 486, 672, 120), meta_style="type-meta-sm",
        meta_html='<b>2027-03-18 14:00</b><br>示例城市 · 示例园区国际会议中心<br>主办方：示例空间',
        qr=(1184, 660, 240, 240),
        logo=(1184, 940, 400, 80), logo_style="type-logo-md", logo_mark=44, logo_mark_radius=12,
    ),
    "oa_cover_first_900x383": dict(
        w=900, h=383,
        hero=(258, 40, 383, 120), deco1=64, deco2=40, deco3=80, deco_border=4, deco_radius=20,
        deco_pos=(210, -14, 40, 40, 120, 10),
        badge=(258, 170), badge_pad_v=6, badge_pad_h=14, badge_style="type-badge-sm",
        title_wrap=(258, 214, 383, 116), title_style="type-display-oa", title_clamp=3,
        subtitle_wrap=(258, 334, 383, 46), subtitle_style="type-subtitle-sm", subtitle_clamp=2,
        qr=(660, 151, 200, 200), qr_inner=78, qr_mod=10, qr_label_off=26,
        logo=(20, 320, 220, 44), logo_style="type-logo-sm", logo_mark=32, logo_mark_radius=8,
    ),
    "oa_cover_second_200x200": dict(
        w=200, h=200,
        hero=(0, 0, 200, 48), deco1=26, deco2=16, deco3=34, deco_border=3, deco_radius=10,
        hero_radius=0,
        deco_pos=(130, -10, 30, 6, 60, 4),
        badge=(10, 10), badge_pad_v=4, badge_pad_h=8, badge_style="type-badge-xs",
        title_wrap=(16, 56, 168, 134), title_style="type-display-thumb", title_clamp=5,
        subtitle_wrap=None, qr=None, logo=None,
    ),
    "mp_cover_750x420": dict(
        w=750, h=420,
        hero=(0, 0, 750, 160), deco1=80, deco2=48, deco3=100, deco_border=4, deco_radius=24,
        hero_radius=0,
        deco_pos=(500, -18, 600, 60, 300, 20),
        badge=(40, 36), badge_pad_v=6, badge_pad_h=14, badge_style="type-badge-sm",
        title_wrap=(40, 184, 430, 140), title_style="type-display-mp", title_clamp=3,
        subtitle_wrap=(40, 332, 430, 48), subtitle_style="type-subtitle-mp", subtitle_clamp=2,
        qr=(500, 176, 200, 200), qr_inner=78, qr_mod=10, qr_label_off=26,
        logo=(40, 388, 200, 28), logo_style="type-logo-xs", logo_mark=20, logo_mark_radius=6,
    ),
    "podcast_cover_3000x3000": dict(
        w=3000, h=3000,
        hero=(300, 300, 2400, 780), deco1=520, deco2=300, deco3=640, deco_border=14, deco_radius=96,
        deco_pos=(1560, 60, 1900, 420, 400, 120),
        badge=(300, 1140), badge_pad_v=20, badge_pad_h=44, badge_style="type-badge-xl",
        title_wrap=(300, 1320, 2400, 840), title_style="type-display-podcast", title_clamp=3,
        subtitle_wrap=(300, 2220, 2400, 220), subtitle_style="type-subtitle-podcast", subtitle_clamp=2,
        meta=(300, 2500, 1900, 90), meta_style="type-meta-podcast",
        meta_html='示例主理人 · 对话示例产业合伙人',
        qr=(2460, 2500, 400, 400), qr_inner=80, qr_mod=20, qr_label_off=40, qr_label_style="type-meta-podcast",
        logo=(300, 2860, 600, 100), logo_style="type-logo-xl", logo_mark=80, logo_mark_radius=20,
    ),
}

if __name__ == "__main__":
    write_tokens_css()
    (OUT / "_badge_labels.json").write_text(
        json.dumps(BADGE_LABELS, ensure_ascii=False, indent=2), encoding="utf-8")
    for name, spec in TEMPLATES.items():
        emit(name, spec)
    print("done:", len(TEMPLATES), "templates")
