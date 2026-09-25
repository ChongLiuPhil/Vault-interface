# Vault Interface 在 Inquiry Publishing Stack 中的位置

Vault Interface 提供一套与平台无关的公共元数据接口，包括 Schema、模板和验证器。它只负责“项目对外怎样被描述”，不保存私人注册表、原创作品、发布队列、部署清单或 Working Memory。

如果第一次接触整个体系，请先从 [AHICP 主页](https://inquirystack.philohub.workers.dev/) 开始；那里提供完整使用指南。需要配置、采用或升级项目时，再由 AI 进入 Starter 的机器入口。

要完成完整配置，请先阅读 [Starter 体系入口](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/ECOSYSTEM.zh-CN.md)，再连接完整的上游层：

- [AHICP 主页](https://inquirystack.philohub.workers.dev/) · [仓库](https://github.com/ChongLiuPhil/AI-Assisted-Human-Inquiry-and-Creation-Protocol)
- [PPF 主页](https://inquirystack.philohub.workers.dev/ppf/) · [仓库](https://github.com/ChongLiuPhil/Personal-Publishing-Framework)
- [Starter 主页](https://inquirystack.philohub.workers.dev/starter/) · [仓库](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter)

完整栈新项目的默认基线是 **完整 AHICP + 完整 PPF + Vault Interface**，本仓库只提供公共元数据适配层。精简配置（profile）必须由使用者明确选择。普通私人 downstream 项目首选 `workers-builds-native` + `private-project-quota-saver`：使用个人 `ChongLiuPhil` 账号、repository 默认 private，允许每项目一次短人工 GitHub → Cloudflare bootstrap，给 Worker 配置 Access，并验证第二次 content-only push 无需重新授权、且没有重复 GitHub Actions production Web build。Content-only 改动不启动 GitHub Actions，配置 PR 只运行一个轻量 contract gate，heavy GitHub workflow 手动运行，Cloudflare Workers Builds 负责 main 的自动 Web build；公共框架仓库继续保留完整 CI。`agent-provisioned-external-ci` 继续作为高级可选基础设施。Public release、source repository 公开、reader 扩大、domain/DNS、Provider scope 扩大、paid-plan change 与开启付费 Actions 仍由人保留。私人项目状态继续保留在项目自己的私有空间中。原创或未发布源内容默认 private，同时可以准备 restricted/authenticated 的 Continuous Web。

四个公共框架栏目现以 https://inquirystack.philohub.workers.dev/ 的 Cloudflare Worker 为正式入口，GitHub 继续作为权威源文件、版本历史和 CI 平台。原框架 GitHub Pages 站点已停用。Vault Interface 的公共元数据接口仍然保持 provider-neutral；当前选择 Cloudflare 承载网页，并不意味着 Cloudflare 成为元数据契约的一部分。

四个框架站点的迁移遵循 [Cloudflare 公共站点迁移说明](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/CLOUDFLARE_PUBLIC_DELIVERY_MIGRATION.zh-CN.md)。

Continuous Web 与 Cloudflare 属于项目级发布事项。新项目先阅读[项目自动配置契约](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/PROJECT_PROVISIONING_CONTRACT.zh-CN.md)，再阅读[操作指南](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/CONTINUOUS_WEB_CLOUDFLARE.zh-CN.md)。本仓库不会授予任何私人内容或 Provider account 的访问权；Provider credential 明文绝不能进入 Vault 公共元数据或 model context。默认 Workers Builds 路线让 deployment credential 保持 Provider-managed。

跨组件工作必须阅读 [权威 Agent 调取契约](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/AGENT_RETRIEVAL_CONTRACT.zh-CN.md)。公共链接只用于恢复生态关系，不授权私人状态访问。如果 Cloudflare 需要使用者执行界面操作，AI Agent 必须给出编号步骤、完成条件、验证方法和回滚方式。
