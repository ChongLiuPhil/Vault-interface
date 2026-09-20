import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]

class InterfaceValidationTests(unittest.TestCase):
    def test_invalid_uri_is_rejected(self):
        project = yaml.safe_load((ROOT / "templates/project.yaml").read_text(encoding="utf-8"))
        website = yaml.safe_load((ROOT / "templates/website.yaml").read_text(encoding="utf-8"))
        website["links"] = ["not a uri"]
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            project_path = td / "project.yaml"
            website_path = td / "website.yaml"
            project_path.write_text(yaml.safe_dump(project, sort_keys=False, allow_unicode=True), encoding="utf-8")
            website_path.write_text(yaml.safe_dump(website, sort_keys=False, allow_unicode=True), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(ROOT / "tools/validate_interface.py"), "--project", str(project_path), "--website", str(website_path)],
                text=True, capture_output=True
            )
        self.assertNotEqual(result.returncode, 0, "invalid URI unexpectedly passed validation")

if __name__ == "__main__":
    unittest.main()
