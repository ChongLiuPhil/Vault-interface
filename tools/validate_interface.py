#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
import sys
import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]

def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))

def validate(instance, schema_path: Path, label: str):
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    errors = sorted(Draft202012Validator(schema).iter_errors(instance), key=lambda e: list(e.path))
    if errors:
        for e in errors:
            where = ".".join(str(p) for p in e.path) or "<root>"
            print(f"ERROR {label} {where}: {e.message}", file=sys.stderr)
        raise SystemExit(1)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--project", default=str(ROOT / "templates/project.yaml"))
    p.add_argument("--website", default=str(ROOT / "templates/website.yaml"))
    args = p.parse_args()

    project = load_yaml(Path(args.project))
    website = load_yaml(Path(args.website))
    validate(project, ROOT / "schemas/project.schema.json", "project")
    validate(website, ROOT / "schemas/website.schema.json", "website")

    if website.get("project_id") and project.get("id") != website.get("project_id"):
        raise SystemExit("ERROR: project.id and website.project_id must match")
    if project.get("website", {}).get("metadata") != Path(args.website).name:
        print("WARNING: project.website.metadata does not match the supplied website filename")
    print("Vault Interface validation passed.")

if __name__ == "__main__":
    main()
