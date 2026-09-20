# Vault Interface 在 Inquiry Publishing Stack 中的位置

Vault Interface 是与提供商无关的公共元数据契约，提供 Schema、模板和验证器；它不包含私人注册表、原创作品、出版队列、部署清单或个人工作记忆。

要完成完整配置，请先阅读 [Starter 体系入口](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/ECOSYSTEM.zh-CN.md)，再连接完整的上游层：

- [AHICP 主页](https://chongliuphil.github.io/AI-Assisted-Human-Inquiry-and-Creation-Protocol/) · [仓库](https://github.com/ChongLiuPhil/AI-Assisted-Human-Inquiry-and-Creation-Protocol)
- [PPF 主页](https://chongliuphil.github.io/Personal-Publishing-Framework/) · [仓库](https://github.com/ChongLiuPhil/Personal-Publishing-Framework)
- [Starter 主页](https://chongliuphil.github.io/Inquiry-Publishing-Project-Starter/) · [仓库](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter)

完整栈新项目的默认基线是 **完整 AHICP + 完整 PPF + Vault Interface**，本仓库只提供公共元数据适配层。精简 profile 必须由人类明确选择。私人项目状态必须保留在项目的私人控制平面中。原创或未发布 canonical source 默认 private，同时可以准备 restricted/authenticated 的 Continuous Web。

Continuous Web 与 Cloudflare 属于项目级发布事项。部署前请阅读[操作指南](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/CONTINUOUS_WEB_CLOUDFLARE.zh-CN.md)；本仓库不会授予任何私人内容或提供商账户的访问权。

跨组件工作必须阅读 [canonical Agent 调取契约](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/AGENT_RETRIEVAL_CONTRACT.zh-CN.md)。公共链接只用于恢复生态关系，不授权私人状态访问。如果 Cloudflare 需要人类执行 UI 操作，Agent 必须给出编号的操作者级步骤、完成证据、验证与回滚。
