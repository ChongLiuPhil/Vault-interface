from pathlib import Path
import re
import subprocess
import sys
import tempfile

import yaml


ROOT = Path(__file__).resolve().parents[1]
CORE_REPOSITORIES = [
    "https://github.com/ChongLiuPhil/AI-Assisted-Human-Inquiry-and-Creation-Protocol",
    "https://github.com/ChongLiuPhil/Personal-Publishing-Framework",
    "https://github.com/ChongLiuPhil/Vault-interface",
    "https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter",
]


def main() -> int:
    manifest = yaml.safe_load((ROOT / "ecosystem.yaml").read_text())
    if not isinstance(manifest, dict) or "ecosystem_entrypoint" not in manifest:
        raise SystemExit("ecosystem.yaml is missing ecosystem_entrypoint")
    manifest_text = (ROOT / "ecosystem.yaml").read_text()
    for repository in CORE_REPOSITORIES:
        if repository not in manifest_text:
            raise SystemExit(f"ecosystem.yaml is missing {repository}")
    for relative in ("README.md", "README.zh-CN.md"):
        text = (ROOT / relative).read_text()
        if "ecosystem.yaml" not in text and "docs/ECOSYSTEM" not in text:
            raise SystemExit(f"{relative} does not point to the ecosystem entrypoint")
    page = (ROOT / "docs/index.html").read_text(encoding="utf-8")
    if '<main id="zh" class="lang active">' not in page:
        raise SystemExit("Vault Interface homepage must keep Chinese visible as a no-JavaScript fallback")
    required_homepage_markers = [
        "私人项目状态",
        "公共项目描述",
        "Schema + Validator",
        "https://chongliuphil.github.io/Inquiry-Publishing-Project-Starter/agent/",
    ]
    for marker in required_homepage_markers:
        if marker not in page:
            raise SystemExit(f"homepage is missing required architecture/discovery marker: {marker}")

    scripts = re.findall(r"<script>(.*?)</script>", page, flags=re.DOTALL)
    if not scripts:
        raise SystemExit("Vault Interface homepage has no inline script to validate")
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".js", delete=False) as handle:
        handle.write("\n".join(scripts))
        script_path = handle.name
    try:
        check = subprocess.run(["node", "--check", script_path], capture_output=True, text=True, check=False)
    except FileNotFoundError as exc:
        raise SystemExit("Node.js is required to validate homepage JavaScript") from exc
    if check.returncode != 0:
        raise SystemExit("Vault Interface homepage JavaScript syntax error:\n" + check.stderr)

    print("ecosystem + homepage validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
