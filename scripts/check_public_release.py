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
    "VERSION", "CHANGELOG.md", "AGENTS.md", "System/upgrade.md",
    "System/maintenance.md", "scripts/check_release_version.py",
    "System/storage/notion.md", "System/storage/github.md",
    "System/setup/notion.md", "System/setup/github.md", "docs/BEHAVIORAL_CONTRACTS.md",
    "assets/daily-companion-cover.webp",
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
    "Notion page id": r"(?:notion\\.so/|notion\\.com/(?:p/)?)[^\\s)]*[a-f0-9]{32}\\b",
    "Drive document id": r"(?:drive\.google\.com/(?:file/d/|drive/folders/)|docs\.google\.com/[^\s]+/d/)[A-Za-z0-9_\-]{20,}",
}
for p in root.rglob("*"):
    # A checkout always contains .git objects, which are binary and not release files.
    if ".git" in p.relative_to(root).parts:
        continue
    if not p.is_file():
        continue
    path = p.relative_to(root).as_posix()
    if any(part in {".git", ".obsidian", "__pycache__", ".trash"} for part in p.parts):
        problems.append("Forbidden directory: " + path)
    if p.name.endswith((".env", ".bak", ".pem", ".key", ".p12", ".pfx")):
        problems.append("Forbidden secret/backup filename: " + path)
    # Exact public artwork allowlist; other binaries remain forbidden.
    if path == "assets/daily-companion-cover.webp":
        data = p.read_bytes()
        if not (12 <= len(data) <= 1024 * 1024 and data[:4] == b"RIFF" and data[8:12] == b"WEBP"):
            problems.append("Invalid public cover: " + path)
        continue
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
profile = (root / "System/profile.md").read_text(encoding="utf-8")
ledger = (root / "System/action_ledger.md").read_text(encoding="utf-8")
extra = (root / "System/daily_companion_extra.md").read_text(encoding="utf-8")
if "setup_complete: false" not in profile or "SETUP_REQUIRED" not in profile:
    problems.append("Profile is not unconfigured")
profile_state = profile.split("---", 2)[1] if profile.startswith("---\n") else ""
profile_keys = re.findall(r"(?m)^([A-Za-z_][A-Za-z0-9_]*):", profile_state)
for key in set(profile_keys):
    if profile_keys.count(key) > 1:
        problems.append("Duplicate profile field: " + key)
for field in ("installed_template_version", "installed_template_commit"):
    if not re.search(r"(?m)^" + field + r": null\s*$", profile):
        problems.append("Public profile has initialized " + field)
for field in ("notion_suite_id", "notion_system_index_id", "notion_daily_source_id", "notion_ledger_source_id", "capture_source"):
    if not re.search(r"(?m)^" + field + r": null\s*$", profile):
        problems.append("Public profile has initialized " + field)
for field in ("gmail_account_ids", "calendar_account_ids"):
    if not re.search(r"(?m)^" + field + r": \[\]\s*$", profile_state):
        problems.append("Public profile has initialized or missing " + field)
if not re.search(r"(?m)^notion_daily_autosave_authorized: false\s*$", profile):
    problems.append("Public profile has initialized Notion write consent")
for field in ("planning_window_start", "planning_window_end", "storage_backend"):
    if not re.search(r"(?m)^" + field + r': "<SETUP_REQUIRED[^"\n]*>"\s*$', profile):
        problems.append("Public profile missing required unconfigured " + field)
version_path = root / "VERSION"
changelog_path = root / "CHANGELOG.md"
if version_path.is_file() and changelog_path.is_file():
    version = version_path.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)", version):
        problems.append("Invalid template VERSION")
    if not re.search(r"(?m)^## " + re.escape(version) + r" [—-] \d{4}-\d{2}-\d{2}\s*$", changelog_path.read_text(encoding="utf-8")):
        problems.append("Missing matching template changelog entry")
if re.search(r"^- \[[xX ]\]", ledger, re.M) or "<!-- dc:" in ledger:
    problems.append("Ledger contains real cards")
for status in ("Action", "Waiting", "Upcoming", "Closed"):
    if "## " + status not in ledger:
        problems.append("Missing Ledger section: " + status)
# The public starter contains no chosen date, claim or delivery history.
extra_state = extra.split("---", 2)[1] if extra.startswith("---\n") else ""
state_keys = re.findall(r"(?m)^([A-Za-z_][A-Za-z0-9_]*):", extra_state)
for key in set(state_keys):
    if state_keys.count(key) > 1:
        problems.append("Duplicate Surprise state field: " + key)
if not re.search(r"(?m)^schema_version: 7\s*$", extra_state):
    problems.append("Surprise schema must be v7")
for field in ("anchor_monday", "weekday_pattern"):
    if not re.search(r"(?m)^" + field + r": null\s*$", extra_state):
        problems.append("Surprise has an initialized or missing " + field)
for field in ("last_approved_auto_delivery", "last_mode", "last_type"):
    if not re.search(r"(?m)^" + field + r": null\s*$", extra):
        problems.append("Surprise has an initialized " + field)
for field in ("recent_types", "recent_themes"):
    if not re.search(r"(?m)^" + field + r": \[\]\s*$", extra):
        problems.append("Surprise has initialized " + field)
if re.search(r"(?m)^(?:weekly_due_dates|next_due|next_due_date|min_gap_days|max_gap_days|schedule_seed|start_week|scheduled_writes_authorized|delivery_status|delivery_due_date|delivery_claimed_at|last_attempt_date):", extra_state):
    problems.append("Surprise still uses legacy cadence fields")
if "Use this template" not in (root / "README.md").read_text(encoding="utf-8"):
    problems.append("README must recommend private template copy")
print("Public template static check")
if problems:
    print("\n".join("FAIL: " + p for p in problems))
    sys.exit(1)
print("PASS: no recognized secrets, configured state or structural violations")
print("Note: static checks cannot guarantee complete PII removal.")
