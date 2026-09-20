# Agent contract

Read [`docs/ECOSYSTEM.md`](docs/ECOSYSTEM.md), [`ecosystem.yaml`](ecosystem.yaml), and the [canonical cross-repository agent retrieval contract](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/AGENT_RETRIEVAL_CONTRACT.md) first. This repository is only a public metadata interface.

The default full-stack project baseline is **full AHICP + full PPF + Vault Interface**. Vault Interface does not replace either upstream framework. Reduced profiles require explicit human selection.

Do not add private registries, original manuscripts, working memory, deployment inventories, credentials, reader secrets, or publication queues here. Original or unpublished project source remains private by default in the project repository; this public interface carries only approved public metadata.

From any Vault Interface public entrypoint, reconstruct all four public components before cross-component configuration. Public links authorize public retrieval only, never private-state access.

For Continuous Web or Cloudflare work, follow the [shared operational guide](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/CONTINUOUS_WEB_CLOUDFLARE.md) and the relevant PPF provider runbooks. If a human must perform a Cloudflare UI action, provide numbered operator-level steps with the exact target, current Dashboard path, non-secret values, secret boundary, completion evidence, verification, and rollback. Never request secrets in chat.
