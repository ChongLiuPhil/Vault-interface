# Vault Interface

**第一次了解整个体系：** 从 [AHICP 主页](https://chongliuphil.github.io/AI-Assisted-Human-Inquiry-and-Creation-Protocol/) 开始；那里提供完整使用指南，并说明怎样把后续技术配置交给 AI。

**公共项目主页：** [AHICP](https://chongliuphil.github.io/AI-Assisted-Human-Inquiry-and-Creation-Protocol/) · [PPF](https://chongliuphil.github.io/Personal-Publishing-Framework/) · [Vault Interface](https://chongliuphil.github.io/Vault-interface/) · [Starter](https://chongliuphil.github.io/Inquiry-Publishing-Project-Starter/)

**体系与 AI 配置入口：** [docs/ECOSYSTEM.zh-CN.md](docs/ECOSYSTEM.zh-CN.md) · [ecosystem.yaml](ecosystem.yaml) · [llms.txt](docs/llms.txt) · [权威 Agent 调取契约](https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter/blob/main/docs/AGENT_RETRIEVAL_CONTRACT.zh-CN.md)

本仓库提供一套**公开、平台无关、可复用**的项目元数据接口，让项目能够对外提供必要描述，而不必公开私人工作状态。

## 边界

本仓库只保存：

- `project.yaml` 的公共接口 schema 与模板；
- `website.yaml` 的公共发布边界 schema 与模板；
- 最小的跨文件一致性校验器；
- 接口版本与兼容性说明。

本仓库**不保存**任何私人：

- 仓库注册表；
- 项目注册表；
- 发布队列；
- 部署清单；
- 研究笔记；
- Working Memory；
- 私人项目关系或未公开材料。

本公共契约参与的完整栈新项目默认基线是 **完整 AHICP + 完整 PPF + Vault Interface**；精简配置（profile）必须由使用者明确选择。原创或未发布项目源文件默认保持 private（私有），Vault Interface 只公开已经确认可以公开的元数据。

因此，私人 Vault 可以消费本接口，但外部项目不需要访问私人 Vault 才能采用这套体系。

私有仓库的地址**不是必需公共元数据**。`project.repository` 是可选字段；除非已经明确允许公开，否则应保持 null 或省略。

## 使用

复制 `templates/project.yaml` 与 `templates/website.yaml` 到项目根目录，然后运行：

```bash
python -m pip install -r requirements-validation.txt
python tools/validate_interface.py --project project.yaml --website website.yaml
```

模板默认 `publish: false`。发布状态只能由项目自身的明确授权决定，不能由 repository visibility 自动推导。

## 兼容性

接口版本记录在 `interface-manifest.yaml`。不兼容字段语义变更必须提升 interface version，并提供迁移说明。


## 综合采用

需要把本接口与 AHICP / PPF 组合为新项目或升级既有项目时，使用：

https://github.com/ChongLiuPhil/Inquiry-Publishing-Project-Starter

Vault Interface 继续只负责公共元数据接口，不承担项目治理或出版生命周期。

## 许可

本仓库采用**非商业双重许可模式**，目的是支持个人学习、教育、研究、公益以及其他非商业复用，同时保留商业授权权利。

- 软件、脚本、Schema、自动化、机器可读配置和可执行模板：**PolyForm Noncommercial License 1.0.0**；
- 说明文档、规范、图示、教育材料与方法论内容：**CC BY-NC-SA 4.0**；
- 商业使用需要另行取得商业许可。

仓库级权威许可边界见 [LICENSE.md](LICENSE.md) 与 [COMMERCIAL-LICENSING.md](COMMERCIAL-LICENSING.md)。
