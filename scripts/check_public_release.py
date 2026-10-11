#!/usr/bin/env python3
"""Best-effort public-source privacy and structure check; manual review is still required."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
required = [
    "README.md", "System/setup.md", "System/profile.md",
    "System/instructions.md", "System/action_ledger.md",
    "System/daily_companion_extra.md", "System/workflows/morning.md",
    "System/workflows/evening.md", "System/policies/rules.md",
    "System/policies/artifacts.md", "docs/PRIVACY.md",
]
problems = []
for name in required:
    if not (root / name).is_file():
        problems.append("Missing " + name)
patterns = {
    "email": r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b",
    "private key": r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----",
    "credential": r"\b(?:ghp_|gho_|ghu_|ghs_|github_pat_|sk-|AIza)[A-Za-z0-9_\-]{12,}",
    "personal path": r"(?:[A-Za-z]:\\(?:Users|Documents and Settings)\\|/Users/[^\s/]+/|/home/[^\s/]+/)",
    "Drive document id": r"(?:drive\.google\.com/(?:file/d/|drive/folders/)|docs\.google\.com/[^\s]+/d/)[A-Za-z0-9_\-]{20,}",
}
for p in root.rglob("*"):
    if not p.is_file():
        continue
    path = p.relative_to(root).as_posix()
    if any(part in {".git", ".obsidian", "__pycache__", ".trash"} for part in p.parts):
        problems.append("Forbidden directory: " + path)
    if p.name.endswith((".env", ".bak", ".pem", ".key", ".p12", ".pfx")):
        problems.append("Forbidden secret/backup filename: " + path)
    if p.suffix not in {".md", ".txt", ".yml", ".yaml", ".py", ".html", "", ".gitkeep"} and p.name != ".gitignore":
        problems.append("Unexpected file type: " + path)
    text = p.read_text(encoding="utf-8")
    if "\x00" in text:
        problems.append("Binary NUL: " + path)
    if path == "scripts/check_public_release.py":
        continue
    for label, regex in patterns.items():
        for match in re.finditer(regex, text):
            problems.append(f"{path}: potential {label}")
profile = (root / "System/profile.md").read_text()
ledger = (root / "System/action_ledger.md").read_text()
extra = (root / "System/daily_companion_extra.md").read_text()
if "setup_complete: false" not in profile or "SETUP_REQUIRED" not in profile:
    problems.append("Profile is not unconfigured")
if re.search(r"^- \[[xX ]\]", ledger, re.M) or "<!-- dc:" in ledger:
    problems.append("Ledger contains real cards")
for status in ("Action", "Waiting", "Upcoming", "Closed"):
    if "## " + status not in ledger:
        problems.append("Missing Ledger section: " + status)
if "next_due: null" not in extra or "recent_themes: []" not in extra:
    problems.append("Surprise has an initialized history")
if "Use this template" not in (root / "README.md").read_text():
    problems.append("README must recommend private template copy")
print("Public template static check")
if problems:
    print("\n".join("FAIL: " + p for p in problems))
    sys.exit(1)
print("PASS: no recognized secrets, configured state or structural violations")
print("Note: static checks cannot guarantee complete PII removal.")
