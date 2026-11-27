"""Submit solution for #2327 - precheck double-criterion gate then POST.

Usage:
  PHASE=precheck python tools_submit.py   # dry-run (rate-limited 6/h)
  PHASE=submit   python tools_submit.py   # irreversible POST (foreground only)
"""
from __future__ import annotations

import json
import os
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RECEIPT_DIR = Path("D:/WorkBuddyProjects/clawhunt/outbox/delivery")
KEY_FILE = Path("D:/WorkBuddyProjects/clawhunt/agent-service/config/api_key")
PID = 2128
BASE = "https://clawhunt.store"
REPO = "https://github.com/Michaelyi07/event-visual-template-suite"
DELIVERY_COMMIT = "183721ccf6676ce450f2201bfb900c26f553fa40"

TEXT = (ROOT / "evidence" / "solution_text.txt").read_text(encoding="utf-8")


def call(method: str, path: str, body: dict | None = None, timeout: int = 180):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        BASE + path, data=data, method=method,
        headers={
            "Authorization": "Bearer " + KEY_FILE.read_text(encoding="utf-8").strip(),
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read().decode("utf-8", "replace")
        return r.status, (json.loads(raw) if raw else {})


def payload():
    return {
        "solution_text": TEXT,
        "assets": [{
            "kind": "github_repo",
            "url": REPO,
            "label": "event-visual-template-suite (public)",
            "notes": f"delivery commit {DELIVERY_COMMIT[:7]}; 7 variable-driven templates (DTCG tokens), 35 verified renders, usage guide, version register",
        }],
    }


def ts() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def gate(st: int, resp: dict):
    data = resp.get("data") or {}
    wp = data.get("would_pass")
    defects = data.get("defects") or []
    ok = st < 400 and (wp is True or (wp is None and not defects))
    return ok, wp, defects


def main() -> None:
    phase = os.environ.get("PHASE", "precheck")
    print(f"PHASE={phase} chars={len(TEXT)} ts={ts()}")

    if phase == "precheck":
        st, resp = call("POST", f"/api/v1/problems/{PID}/solution/precheck", payload())
        ok, wp, defects = gate(st, resp)
        print("PRECHECK_HTTP", st, "would_pass", wp)
        print("defects", json.dumps(defects, ensure_ascii=False)[:1200])
        print("critic", json.dumps((resp.get("data") or {}).get("critic") or {}, ensure_ascii=False)[:600])
        print("GATE_PASS", ok)
        (ROOT / "evidence" / "precheck_result.json").write_text(
            json.dumps({"ts": ts(), "http": st, "would_pass": wp, "defects": defects,
                        "gate_pass": ok, "raw": resp}, ensure_ascii=False, indent=2),
            encoding="utf-8")
        return

    if phase == "submit":
        st, resp = call("POST", f"/api/v1/problems/{PID}/solution/precheck", payload())
        ok, wp, defects = gate(st, resp)
        print("PRECHECK_GATE", st, "would_pass", wp, "defects", len(defects), "OK", ok)
        if not ok:
            print("ABORT: precheck gate failed; no POST sent")
            return
        post_error = None
        post_resp = None
        try:
            st2, resp2 = call("POST", f"/api/v1/problems/{PID}/solution", payload())
            post_resp = {"http": st2, "body": resp2}
            print("POST_HTTP", st2, json.dumps(resp2, ensure_ascii=False)[:500])
        except Exception as e:
            post_error = f"{type(e).__name__}: {str(e)[:200]}"
            print("POST_EXCEPTION", post_error, "(submission may still have landed)")
        finally:
            st3, detail = call("GET", f"/api/v1/problems/{PID}")
            problem = detail.get("data") or detail
            status = problem.get("status")
            print("GET_STATUS", st3, "status", status)
            receipt = {
                "ts": ts(), "pid": PID, "repo": REPO, "commit": DELIVERY_COMMIT,
                "chars": len(TEXT), "precheck": {"http": st, "would_pass": wp, "gate_pass": ok},
                "post_error": post_error, "post_response": post_resp, "verified_status": status,
            }
            RECEIPT_DIR.mkdir(parents=True, exist_ok=True)
            out = RECEIPT_DIR / f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{PID}_solution.json"
            out.write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
            print("RECEIPT", out)
        return

    print("Unknown PHASE", phase)


if __name__ == "__main__":
    main()
