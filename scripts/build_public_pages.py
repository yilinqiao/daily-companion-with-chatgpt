#!/usr/bin/env python3
"""Generate a read-only, JavaScript-free mirror of the generic public template."""
from html import escape
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]
REPO = "https://github.com/yilinqiao/daily-companion-with-chatgpt"

# Deliberately allowlist public files; never mirror the checkout or personal folders.
SYSTEM_FILES = (
    "System/setup.md", "System/profile.md", "System/instructions.md",
    "System/setup/notion.md", "System/setup/github.md",
    "System/storage/notion.md", "System/storage/github.md",
    "System/workflows/morning.md", "System/workflows/evening.md",
    "System/policies/rules.md", "System/policies/artifacts.md",
    "System/action_ledger.md", "System/daily_companion_extra.md",
    "System/upgrade.md", "System/maintenance.md",
)
PUBLIC_FILES = ("README.md", "CHANGELOG.md", "AGENTS.md", "docs/GETTING_STARTED.md",
                "docs/PRIVACY.md", *SYSTEM_FILES)


def html_page(title, body):
    return ("<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
            f"<title>{escape(title)}</title><style>"
            "body{font:16px/1.6 system-ui,sans-serif;max-width:900px;margin:2rem auto;padding:0 1rem}"
            "pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f4f4f4;padding:1rem;border-radius:6px}"
            "a{color:#1756a9}h1{line-height:1.2}"
            "</style></head><body>" + body + "</body></html>\n")


def build(output, commit=""):
    if output.exists():
        raise ValueError("Output directory must not already exist")
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)", version):
        raise ValueError("Invalid public VERSION")
    if commit and not re.fullmatch(r"[a-f0-9]{40}", commit):
        raise ValueError("Invalid source commit")
    # Read every required file before creating output. Missing files block publishing.
    contents = {name: (ROOT / name).read_bytes() for name in PUBLIC_FILES}
    provenance = (f'<p>Source commit: <a href="{REPO}/commit/{commit}">{commit}</a></p>'
                  if commit else "<p>Local preview; source commit not attested.</p>")
    output.mkdir(parents=True)

    def write(path, data):
        target = output / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data.encode("utf-8") if isinstance(data, str) else data)

    def document(name):
        return html_page(name, f"<h1>{escape(name)}</h1><p>Public template version: {version}</p>"
                         + provenance + f"<pre>{escape(contents[name].decode('utf-8'))}</pre>")

    write("VERSION", (ROOT / "VERSION").read_bytes())
    write("version.html", html_page("Daily Companion version", f"<h1>Latest published version: {version}</h1>" + provenance))
    for name, data in contents.items():
        write(name, data)
        write(str(Path(name).with_suffix(".html")), document(name))
    # Only the explicitly approved public artwork and its legacy variant.
    for cover in ("assets/daily-companion-cover.png", "assets/daily-companion-cover.webp"):
        write(cover, (ROOT / cover).read_bytes())
    for alias, name in (("setup.html", "System/setup.md"), ("changelog.html", "CHANGELOG.md"),
                        ("upgrade.html", "System/upgrade.md")):
        write(alias, document(name))
    write("bundle.html", html_page("Daily Companion public setup bundle",
          f"<h1>Public setup bundle</h1><p>Version: {version}</p>" + provenance +
          "".join(f"<h2>{escape(name)}</h2><pre>{escape(contents[name].decode('utf-8'))}</pre>"
                  for name in SYSTEM_FILES)))
    links = "".join(f'<li><a href="{Path(name).with_suffix(".html").as_posix()}">{escape(name)}</a></li>'
                    for name in PUBLIC_FILES)
    write("index.html", html_page("Daily Companion", "<h1>Daily Companion with ChatGPT</h1>"
          f"<p>Public template version: <strong>{version}</strong></p>" + provenance +
          '<p>Read-only mirror of the public template. No private notes, personal configuration or automatic installation.</p>'
          '<ul><li><a href="version.html">Latest version</a></li><li><a href="setup.html">Setup</a></li>'
          '<li><a href="bundle.html">Complete setup bundle</a></li><li><a href="changelog.html">Changelog</a></li>'
          f'<li><a href="{REPO}">Canonical repository and version history</a></li></ul>'
          f"<h2>Public source files</h2><ul>{links}</ul>"))
    write(".nojekyll", "")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--commit", default="")
    args = parser.parse_args()
    build(args.output, args.commit)
