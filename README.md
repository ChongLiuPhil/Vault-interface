# Vault Interface

**Public project homepages:** [AHICP](https://chongliuphil.github.io/AI-Assisted-Human-Inquiry-and-Creation-Protocol/) · [PPF](https://chongliuphil.github.io/Personal-Publishing-Framework/) · [Vault Interface](https://chongliuphil.github.io/Vault-interface/) · [Starter](https://chongliuphil.github.io/Inquiry-Publishing-Project-Starter/)

**Ecosystem and agent entrypoint:** [docs/ECOSYSTEM.md](docs/ECOSYSTEM.md) · [ecosystem.yaml](ecosystem.yaml) · [llms.txt](docs/llms.txt) · [canonical agent retrieval contract](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/AGENT_RETRIEVAL_CONTRACT.md)

Public, provider-neutral metadata interfaces for project repositories that may be indexed by a private portfolio or vault.

This repository contains only reusable schemas, templates, and validators. It does **not** contain any private registry, publication queue, research notes, deployment inventory, or personal working memory.

This public contract participates in a default full-stack baseline of **full AHICP + full PPF + Vault Interface**. Reduced profiles require explicit human selection. Original or unpublished project source remains private by default; Vault Interface exposes only approved public metadata.

The interface is designed to be consumed by repositories such as Academic Vault, AHICP-governed projects, PPF publishing projects, and composite starters.

A private repository's identity is **not required public metadata**. The `project.repository` field is optional and may remain null unless disclosure of the repository locator has been explicitly approved.

See [README.zh-CN.md](README.zh-CN.md) for the canonical Chinese introduction.


## Composite adoption

To combine this interface with AHICP and/or PPF for a new project or an existing-project upgrade, use:

https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter

Vault Interface remains responsible only for the public metadata contract; it does not become the project-governance or publication-lifecycle authority.

## Licensing

This repository uses a **noncommercial split-license model** intended to support personal learning, education, research, public-benefit work, and other noncommercial reuse.

- Software, scripts, schemas, automation, machine-readable configuration, and executable templates: **PolyForm Noncommercial License 1.0.0**.
- Prose documentation, specifications, diagrams, educational content, and methodological materials: **CC BY-NC-SA 4.0**.
- Commercial use requires a separate commercial license.

See [LICENSE.md](LICENSE.md) and [COMMERCIAL-LICENSING.md](COMMERCIAL-LICENSING.md) for the authoritative repository-level licensing boundary.
