# Vault Interface

**New to the full stack?** Start with the [AHICP homepage](https://inquirystack.philohub.workers.dev/), which explains the system from the user’s point of view and shows how to hand technical setup to an AI.

**Public project homepages:** [AHICP](https://inquirystack.philohub.workers.dev/) · [PPF](https://inquirystack.philohub.workers.dev/ppf/) · [Vault Interface](https://inquirystack.philohub.workers.dev/vault-interface/) · [Starter](https://inquirystack.philohub.workers.dev/starter/)

**Ecosystem and agent entrypoint:** [docs/ECOSYSTEM.md](docs/ECOSYSTEM.md) · [ecosystem.yaml](ecosystem.yaml) · [llms.txt](docs/llms.txt) · [canonical agent retrieval contract](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/AGENT_RETRIEVAL_CONTRACT.md)

A provider-neutral public metadata interface for describing projects without exposing their private working state.

This repository contains only reusable schemas, templates, and validators. It does **not** contain any private registry, publication queue, research notes, deployment inventory, or personal working memory.

This public contract participates in a default full-stack baseline of **full AHICP + full PPF + Vault Interface**. Reduced profiles require explicit human selection. Original or unpublished project source remains private by default; Vault Interface exposes only approved public metadata.

The interface is designed to be consumed by repositories such as Academic Vault, AHICP-governed projects, PPF publishing projects, and composite starters.

A private repository address is **not required public metadata**. The `project.repository` field is optional and may remain null unless that address has been explicitly approved for disclosure.

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
