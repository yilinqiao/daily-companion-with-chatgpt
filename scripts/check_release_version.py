"""Public-source CI gate: changed releases require a version and dated notes."""
import argparse
from datetime import date
from pathlib import Path
import re
import subprocess
import sys


def _version(value):
    if not re.fullmatch(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)", value):
        raise ValueError("VERSION must be MAJOR.MINOR.PATCH without leading zeroes")
    return tuple(map(int, value.split(".")))


def release_problems(base_version, version, changed_paths, changelog):
    problems = []
    try:
        current = _version(version)
        previous = _version(base_version) if base_version is not None else None
    except ValueError as error:
        return [str(error)]
    if not changed_paths:
        return []
    if previous is not None and current <= previous:
        problems.append("Template version must increase for public changes")
    for path in ("VERSION", "CHANGELOG.md"):
        if path not in changed_paths:
            problems.append(path + " must change with a public release")
    entries = re.findall(r"(?m)^## " + re.escape(version) + r" [—-] (\d{4}-\d{2}-\d{2})\s*$", changelog)
    if len(entries) != 1:
        problems.append("CHANGELOG.md must have exactly one matching dated entry")
    else:
        try:
            date.fromisoformat(entries[0])
        except ValueError:
            problems.append("CHANGELOG.md dated entry must use a real date")
    return problems


def comparison_base(requested_base, git):
    if re.fullmatch(r"0{40}", requested_base):
        parents = git("rev-list", "--parents", "-n", "1", "HEAD").stdout.split()
        if len(parents) != 1:
            raise ValueError("New branch has no reliable previous head; use an explicit --base or a pull-request comparison")
        return None  # A root commit is the initial repository release.
    return git("rev-parse", "--verify", "--end-of-options", requested_base + "^{commit}").stdout.strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, help="Previous public commit or PR base SHA")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]

    def git(*arguments, check=True):
        result = subprocess.run(["git", *arguments], cwd=root, capture_output=True, text=True, encoding="utf-8")
        if check and result.returncode:
            raise ValueError("Git release comparison failed: " + result.stderr.strip())
        return result

    try:
        # A new-branch event has no trustworthy prior branch head. Never
        # look only at the last commit and miss earlier instruction edits.
        base = comparison_base(args.base, git)
        if base:
            paths = set(git("diff", "--name-only", base, "HEAD", "--").stdout.splitlines())
            listing = git("ls-tree", "--name-only", base, "--", "VERSION").stdout.splitlines()
            old = git("show", base + ":VERSION").stdout.strip() if "VERSION" in listing else None
        else:
            paths = set(git("ls-tree", "-r", "--name-only", "HEAD").stdout.splitlines())
            old = None
        version = (root / "VERSION").read_text(encoding="utf-8").strip()
        notes = (root / "CHANGELOG.md").read_text(encoding="utf-8")
        problems = release_problems(old, version, paths, notes)
    except (OSError, ValueError) as error:
        problems = [str(error)]
    if problems:
        print("\n".join("FAIL: " + problem for problem in problems))
        return 1
    print("PASS: public release version and changelog are consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
