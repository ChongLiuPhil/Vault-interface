# Agent 协作契约

先阅读 [`docs/ECOSYSTEM.zh-CN.md`](docs/ECOSYSTEM.zh-CN.md)、[`ecosystem.yaml`](ecosystem.yaml) 与 [canonical 跨仓库 Agent 调取契约](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/AGENT_RETRIEVAL_CONTRACT.zh-CN.md)。面对新项目时，还必须读取 [项目自动配置契约](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/PROJECT_PROVISIONING_CONTRACT.zh-CN.md)。本仓库只保存公共元数据接口。

完整栈新项目默认基线是 **完整 AHICP + 完整 PPF + Vault Interface**。Vault Interface 不替代任何上游框架。精简 profile 必须由人类明确选择。

不要在这里加入私人注册表、原创手稿、工作记忆、部署清单、凭据、读者秘密或出版队列。原创或未发布项目源文件默认保留在项目 private 仓库；本公共接口只承载经过批准的公共元数据。

从任意 Vault Interface 公共入口进入时，在跨组件配置前恢复全部四个公共组件。公共链接只授权读取公共信息，绝不授权私人状态访问。

涉及 Continuous Web 或 Cloudflare 时，遵循 Starter 项目自动配置契约、[共享操作指南](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/CONTINUOUS_WEB_CLOUDFLARE.zh-CN.md) 与固定版本 PPF Provider runbook。普通新项目使用 `workers-builds-native`，允许每项目一次短人工 GitHub → Cloudflare bootstrap，并要求第二次 push 验证无需重新授权。Provider credential 明文绝不能进入 Vault 公共元数据或 chat/model context；Trusted Secret Broker 只属于高级可选 External-CI Profile。需要人类执行项目级或保留的 Cloudflare UI 动作时，给出准确目标、当前 Dashboard 路径、非秘密填写值、秘密边界、完成证据、验证与回滚。
