# Vault Interface in the Inquiry Publishing Stack

Vault Interface defines a provider-neutral public description of a project. It supplies schemas, templates, and validators, but does not contain private registries, original work, publication queues, deployment inventories, or Working Memory.

If the full stack is new to you, start with the [AHICP homepage](https://inquirystack.philohub.workers.dev/). For project setup, adoption, or upgrades, an AI should enter through Starter’s machine entrypoint.

For a complete configuration, follow the [Starter ecosystem entrypoint](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/ECOSYSTEM.md), then connect the full upstream layers:

- [AHICP homepage](https://inquirystack.philohub.workers.dev/) · [repository](https://github.com/ChongLiuPhil/AI-Assisted-Human-Inquiry-and-Creation-Protocol)
- [PPF homepage](https://inquirystack.philohub.workers.dev/ppf/) · [repository](https://github.com/ChongLiuPhil/Personal-Publishing-Framework)
- [Starter homepage](https://inquirystack.philohub.workers.dev/starter/) · [repository](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter)

The default full-stack baseline for a new project is **full AHICP + full PPF + Vault Interface**, with this repository providing only the public metadata adapter. Reduced profiles require explicit human selection. Private project state must remain in the project's private control plane. Original or unpublished canonical source is private by default, while Continuous Web may be prepared in a restricted/authenticated state.

The four public framework sections now use the verified canonical Cloudflare Worker at https://inquirystack.philohub.workers.dev/, while GitHub remains the canonical source/version-control provider. Former GitHub Pages URLs remain available as legacy entrypoints. Vault Interface's public metadata contract remains provider-neutral; choosing Cloudflare for current site delivery does not make Cloudflare part of the metadata contract.

Use the [coordinated public-delivery migration guide](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/CLOUDFLARE_PUBLIC_DELIVERY_MIGRATION.md) for the framework sites.

Continuous Web and Cloudflare are project-level publication concerns. Before deployment, read the [operational guide](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/CONTINUOUS_WEB_CLOUDFLARE.md); this repository does not grant access to any private content or provider account.

For cross-component work, read the [canonical agent retrieval contract](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/AGENT_RETRIEVAL_CONTRACT.md). Public links support ecosystem reconstruction; they do not authorize private-state access. If Cloudflare requires human UI action, the agent must provide numbered operator-level steps, completion evidence, verification, and rollback.
