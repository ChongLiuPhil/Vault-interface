# Agent 协作契约

先阅读 [`docs/ECOSYSTEM.zh-CN.md`](docs/ECOSYSTEM.zh-CN.md)、[`ecosystem.yaml`](ecosystem.yaml) 与 [canonical 跨仓库 Agent 调取契约](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/AGENT_RETRIEVAL_CONTRACT.zh-CN.md)。本仓库只保存公共元数据接口。

完整栈新项目默认基线是 **完整 AHICP + 完整 PPF + Vault Interface**。Vault Interface 不替代任何上游框架。精简 profile 必须由人类明确选择。

不要在这里加入私人注册表、原创手稿、工作记忆、部署清单、凭据、读者秘密或出版队列。原创或未发布项目源文件默认保留在项目 private 仓库；本公共接口只承载经过批准的公共元数据。

从任意 Vault Interface 公共入口进入时，在跨组件配置前恢复全部四个公共组件。公共链接只授权读取公共信息，绝不授权私人状态访问。

涉及 Continuous Web 或 Cloudflare 时，遵循 [共享操作指南](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/CONTINUOUS_WEB_CLOUDFLARE.zh-CN.md) 以及相关 PPF provider runbook。若必须由人类执行 Cloudflare UI 操作，必须给出编号的操作者级步骤，包括准确目标、当前 Dashboard 路径、非秘密填写值、秘密边界、完成证据、验证与回滚。绝不要求人类在聊天中提供秘密。
