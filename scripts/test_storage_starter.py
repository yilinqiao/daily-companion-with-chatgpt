"""Release gate rejects configured private storage and absent adapters."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


class StorageStarterTests(unittest.TestCase):
    def check(self, mutate):
        source = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory(dir=source.parent) as folder:
            target = Path(folder) / 'template'
            shutil.copytree(source, target, ignore=shutil.ignore_patterns('.git', '__pycache__'))
            mutate(target)
            return subprocess.run([sys.executable, '-B', str(target / 'scripts/check_public_release.py')],
                                  capture_output=True, text=True)

    def test_missing_notion_adapter_fails_release(self):
        def mutate(root):
            (root / 'System/storage/notion.md').unlink(missing_ok=True)
        self.assertEqual(self.check(mutate).returncode, 1)

    def test_configured_notion_destination_fails_release(self):
        def mutate(root):
            p = root / 'System/profile.md'
            p.write_text(p.read_text().replace('notion_suite_id: null', 'notion_suite_id: example-private-id'))
        self.assertEqual(self.check(mutate).returncode, 1)

    def test_missing_planning_window_fails_release(self):
        def mutate(root):
            p = root / 'System/profile.md'
            p.write_text('\n'.join(line for line in p.read_text().splitlines() if not line.startswith('planning_window_end:')))
        self.assertEqual(self.check(mutate).returncode, 1)
