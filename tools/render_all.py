"""Render all templates via headless Chrome: screenshots + geometry reports.

Outputs (all real runs):
  evidence/stress/*.png + *.json      7 templates x {10-char title, 30-char title} = 14
  evidence/variants/*.png             vertical poster x 3 badge variants = 3
  evidence/samples/*.png              7 fictional-event sample exports
  evidence/geo_reports.json           every report, one file
"""
import hashlib
import json
import subprocess
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
TPL = ROOT / "templates"
EV = ROOT / "evidence"

T10 = "产业资源对接主题沙龙"                      # exactly 10 CJK chars
T30 = "新一代产业资源对接平台会员企业春季合作洽谈系列主题沙龙活动月"  # exactly 30
_base = "汇聚行业专家与会员企业代表现场交流对接合作机会共建长期合作关系的四季系列实践活动"
S40 = _base[:40]  # exactly 40 (stress string, programmatically bounded)
assert len(T10) == 10 and len(T30) == 30 and len(S40) == 40, (len(T10), len(T30), len(S40))

TEMPLATES = [
    "poster_vertical_1080x1920", "poster_square_1080x1080", "poster_horizontal_1920x1080",
    "oa_cover_first_900x383", "oa_cover_second_200x200", "mp_cover_750x420",
    "podcast_cover_3000x3000",
]
SIZES = {
    "poster_vertical_1080x1920": (1080, 1920), "poster_square_1080x1080": (1080, 1080),
    "poster_horizontal_1920x1080": (1920, 1080), "oa_cover_first_900x383": (900, 383),
    "oa_cover_second_200x200": (200, 200), "mp_cover_750x420": (750, 420),
    "podcast_cover_3000x3000": (3000, 3000),
}
SAMPLES = {  # fictional events; subtitle '' = hidden
    "poster_vertical_1080x1920": ("示例产业资源对接主题沙龙", "对话四位产业合伙人现场对接合作机会", "public"),
    "poster_square_1080x1080": ("示例会员资源对接会", "仅限会员企业报名的一对一合作洽谈专场", "member-only"),
    "poster_horizontal_1920x1080": ("示例创始人闭门研讨", "十二家会员企业创始人的季度策略夜谈", "closed-door"),
    "oa_cover_first_900x383": ("示例产业沙龙：从场地到生态", "会员空间平台升级后的第一场资源对接会", "public"),
    "oa_cover_second_200x200": ("示例会员资源对接会", None, "member-only"),
    "mp_cover_750x420": ("示例产业沙龙报名开启", "03-18 示例园区国际会议中心", "public"),
    "podcast_cover_3000x3000": ("资源对接实战手记", "示例主理人与会员企业创始人的十一期对谈", "closed-door"),
}


def chrome_run(url: str, size: tuple[int, int], screenshot: Path | None, dump: bool) -> str:
    w, h = size
    cmd = [CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
           "--force-device-scale-factor=1", "--force-color-profile=srgb",
           f"--window-size={w},{h}", "--virtual-time-budget=5000"]
    if screenshot:
        cmd += [f"--screenshot={screenshot}"]
    if dump:
        cmd += ["--dump-dom"]
    cmd += [url]
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    return out.stdout


def parse_report(dom: str) -> dict:
    marker = '<pre id="geo-report" style="display:none;">'
    i = dom.find(marker)
    if i < 0:
        raise RuntimeError("geo-report not found in DOM (script may not have run)")
    j = dom.find("</pre>", i)
    return json.loads(dom[i + len(marker):j])


def url_for(tpl: str, t: str | None, s: str | None, v: str | None) -> str:
    params = {}
    if t is not None:
        params["t"] = t
    if s is not None:
        params["s"] = s
    if v:
        params["v"] = v
    qs = ("?" + urllib.parse.urlencode(params)) if params else ""
    return f"file:///{TPL.as_posix()}/{tpl}.html{qs}"


def run_case(tpl: str, label: str, t: str, s: str | None, v: str,
             shot_dir: Path, reports: dict) -> dict:
    w, h = SIZES[tpl]
    url = url_for(tpl, t, s, v)
    shot = shot_dir / f"{tpl}_{label}.png"
    chrome_run(url, (w, h), shot, dump=False)
    dom = chrome_run(url, (w, h), None, dump=True)
    rep = parse_report(dom)
    rep["screenshot"] = shot.relative_to(ROOT).as_posix()
    rep["png_sha256"] = hashlib.sha256(shot.read_bytes()).hexdigest() if shot.exists() else None
    reports[f"{tpl}_{label}"] = rep
    status = "PASS" if rep["pass"] else "FAIL"
    print(f"{status} {tpl}_{label} title_fit={rep['checks']['title_fit']['ok']} "
          f"overlaps={rep['checks']['overlaps']['count']}")
    return rep


def main() -> None:
    for d in ("stress", "variants", "samples"):
        (EV / d).mkdir(parents=True, exist_ok=True)
    reports: dict = {}

    print("== stress: 7 templates x (10-char, 30-char) ==")
    for tpl in TEMPLATES:
        has_sub = tpl != "oa_cover_second_200x200"  # thumbnail has no subtitle layer by design
        run_case(tpl, "t10", T10, "" if has_sub else None, "public", EV / "stress", reports)
        run_case(tpl, "t30", T30, S40 if has_sub else None, "public", EV / "stress", reports)

    print("== variant proof: 7 templates x (member-only, closed-door) ==")
    for tpl in TEMPLATES:
        for v in ("member-only", "closed-door"):
            run_case(tpl, f"v_{v}", "示例产业沙龙", "" if tpl != "oa_cover_second_200x200" else None, v,
                     EV / "variants", reports)

    print("== samples: 7 fictional exports ==")
    for tpl, (t, s, v) in SAMPLES.items():
        run_case(tpl, "sample", t, s if s is not None else "", v, EV / "samples", reports)

    (EV / "geo_reports.json").write_text(
        json.dumps(reports, ensure_ascii=False, indent=1), encoding="utf-8")
    fails = [k for k, r in reports.items() if not r["pass"]]
    print(f"TOTAL {len(reports)} runs, {len(fails)} failed: {fails}")


if __name__ == "__main__":
    main()
