# Agent contract

Read [`docs/ECOSYSTEM.md`](docs/ECOSYSTEM.md), [`ecosystem.yaml`](ecosystem.yaml), and the [canonical cross-repository agent retrieval contract](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/AGENT_RETRIEVAL_CONTRACT.md) first. For a new project, also read the [Project Provisioning Contract](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/PROJECT_PROVISIONING_CONTRACT.md). This repository is only a public metadata interface.

The default full-stack project baseline is **full AHICP + full PPF + Vault Interface**. Vault Interface does not replace either upstream framework. Reduced profiles require explicit human selection.

Do not add private registries, original manuscripts, working memory, deployment inventories, credentials, reader secrets, or publication queues here. Original or unpublished project source remains private by default in the project repository; this public interface carries only approved public metadata.

From any Vault Interface public entrypoint, reconstruct all four public components before cross-component configuration. Public links authorize public retrieval only, never private-state access.

For Continuous Web or Cloudflare work, follow the Starter Project Provisioning Contract, the [shared operational guide](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/CONTINUOUS_WEB_CLOUDFLARE.md), and the pinned PPF provider runbooks. After verified platform bootstrap, reuse bounded standing authorization for ordinary private/restricted setup inside the approved scope instead of repeatedly escalating routine provider work. Deployment-token plaintext must remain inside the trusted Secret Broker and must never enter Vault public metadata or chat/model context. If a human must perform a genuinely reserved Cloudflare UI action, provide numbered operator-level steps with the exact target, current Dashboard path, non-secret values, secret boundary, completion evidence, verification, and rollback.
