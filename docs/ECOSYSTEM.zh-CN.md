# Vault Interface 在 Inquiry Publishing Stack 中的位置

Vault Interface 提供一套与平台无关的公共元数据接口，包括 Schema、模板和验证器。它只负责“项目对外怎样被描述”，不保存私人注册表、原创作品、发布队列、部署清单或 Working Memory。

如果第一次接触整个体系，请先从 [AHICP 主页](https://chongliuphil.github.io/AI-Assisted-Human-Inquiry-and-Creation-Protocol/) 开始；那里提供完整使用指南。需要配置、采用或升级项目时，再由 AI 进入 Starter 的机器入口。

要完成完整配置，请先阅读 [Starter 体系入口](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/ECOSYSTEM.zh-CN.md)，再连接完整的上游层：

- [AHICP 主页](https://chongliuphil.github.io/AI-Assisted-Human-Inquiry-and-Creation-Protocol/) · [仓库](https://github.com/ChongLiuPhil/AI-Assisted-Human-Inquiry-and-Creation-Protocol)
- [PPF 主页](https://chongliuphil.github.io/Personal-Publishing-Framework/) · [仓库](https://github.com/ChongLiuPhil/Personal-Publishing-Framework)
- [Starter 主页](https://chongliuphil.github.io/Inquiry-Publishing-Project-Starter/) · [仓库](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter)

完整栈新项目的默认基线是 **完整 AHICP + 完整 PPF + Vault Interface**，本仓库只提供公共元数据适配层。精简配置（profile）必须由使用者明确选择。私人项目状态继续保留在项目自己的私有空间中。原创或未发布源内容默认 private，同时可以准备 restricted/authenticated 的 Continuous Web。

Continuous Web 与 Cloudflare 属于项目级发布事项。部署前请阅读[操作指南](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/CONTINUOUS_WEB_CLOUDFLARE.zh-CN.md)；本仓库不会授予任何私人内容或提供商账户的访问权。

跨组件工作必须阅读 [权威 Agent 调取契约](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/AGENT_RETRIEVAL_CONTRACT.zh-CN.md)。公共链接只用于恢复生态关系，不授权私人状态访问。如果 Cloudflare 需要使用者执行界面操作，AI Agent 必须给出编号步骤、完成条件、验证方法和回滚方式。
