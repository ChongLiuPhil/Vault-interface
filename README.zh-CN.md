# Vault Interface

本仓库提供一组**公开、中性、可复用**的项目元数据接口，供私人 Academic Vault、AHICP 项目、PPF 项目以及综合 Starter 使用。

## 边界

本仓库只保存：

- `project.yaml` 的公共接口 schema 与模板；
- `website.yaml` 的公共发布边界 schema 与模板；
- 最小的跨文件一致性校验器；
- 接口版本与兼容性说明。

本仓库**不保存**任何私人：

- repository registry；
- project registry；
- publication queue；
- deployment inventory；
- research notes；
- Working Memory；
- 私人项目关系或未公开材料。

因此，私人 Vault 可以消费本接口，但外部项目不需要访问私人 Vault 才能采用这套体系。

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

Vault Interface 继续只负责公开 metadata contract，不承担项目治理或出版生命周期。
