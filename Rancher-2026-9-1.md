# Rancher 社区双周报 | Rancher v2.15.1 正式发布！包含多项关键安全补丁及 RKE2/K3s 全线更新

各位 Rancher 社区的小伙伴们，大家好！

欢迎阅读新一期的 Rancher 社区双周报！在过去的半个月里，Rancher 核心产品家族迎来了一系列重要的安全加固与版本更新。

本期重点推荐 Rancher v2.15.1 的发布，作为紧随 v2.15.0 大版本之后的首个补丁版，它集中修复了包括 SAML 认证断言重放、项目级密钥泄露在内的多项关键安全漏洞。同时，RKE2 与 K3s 同步升级至 **Kubernetes v1.36.4**，进一步稳固了底层引擎的可靠性。此外，**Longhorn v1.12.1** 带来的 V2 数据引擎性能进阶同样值得每一位存储用户关注。

接下来，让我们深入了解各产品的详细更新细节。

## Rancher

Rancher v2.15.1 正式发布！作为一个关键的维护版本，此版本主要聚焦于安全漏洞修复和系统稳定性增强。

### 安全漏洞修复

本版本修复了多项高危安全漏洞，建议所有用户尽快安排升级：

- **SAML 认证重放攻击防护 (CVE-2026-75034)**：修复了 SAML 验证器在 HA 高可用部署下由于各副本内存缓存不一致导致的断言重放漏洞。现在实现了跨副本的断言 ID 追踪。
- **项目密钥泄露风险规避 (CVE-2026-75033)**：修复了 secretsController 在传播项目密钥时未严格校验集群归属的问题，防止跨集群的恶意标签伪造导致密钥泄露。
- **Token API 元数据泄露修复 (CVE-2026-75035)**：加强了对 ext.cattle.io/v1 令牌接口的访问控制，强制执行用户作用域校验，防止未授权用户获取他人令牌哈希。
- **GlobalRole 越权配置补丁 (CVE-2026-71404)**：修复了通过修改注解篡改内置 ClusterRole 规则的逻辑缺陷，规避了潜在的全局权限锁定风险。
- **Norman API 身份信息防篡改 (CVE-2026-71403)**：在 /v3/users 接口中对用户名、外部身份 ID 等关键字段增加了不可变约束，防止账户被非法接管。

### 持续交付与 Fleet 增强

- **Fleet 安全加固 (CVE-2026-75036)**：限制了 Helm 模板预处理阶段的网络访问能力，防止恶意 Bundle 探测集群内部网络或泄露主机元数据。

如需详细了解完整更新内容，请查阅：

- [Rancher v2.15.1 Release Notes](https://github.com/rancher/rancher/releases/tag/v2.15.1 "Rancher v2.15.1 Release Notes")

## RKE2

RKE2 发布了最新的维护版本，涵盖了 v1.34 至 v1.36 的多个 Kubernetes 主版本。本次更新重点对齐了上游 K8s 安全补丁，并持续推进 Ingress 控制器向 Traefik 的平滑过渡。

### 核心引擎与组件升级

- **Kubernetes 版本对齐**：同步升级至最新的上游补丁版 **v1.36.4**、**v1.35.8** 及 **v1.34.11**。
- **容器运行时更新**：升级 containerd 至 **v2.3.4-k3s1.36**（针对 v1.36 分支）或 v2.2.7-k3s1（针对 v1.35 分支），进一步提升了并发处理稳定性。
- **内置 Ingress 演进**：持续优化从 ingress-nginx 向 Traefik (v3.7.11) 的默认切换逻辑。针对 Windows 离线环境，重构了运行时镜像的构建与打包流水线，修复了镜像丢失问题。

### Chart 与插件优化

- **网络插件更新**：更新了 rke2-canal 与 rke2-flannel 的 Chart 版本，优化了底层配置参数。
- **存储驱动增强**：升级 Harvester CSI 驱动至 0.1.31，提升了超融合场景下的卷操作响应速度。

如需详细了解完整更新内容，请查阅：

- [RKE2 v1.34.11+rke2r1 Release Notes](https://github.com/rancher/rke2/releases/tag/v1.34.11%2Brke2r1 "RKE2 v1.34.11+rke2r1 Release Notes")
- [RKE2 v1.35.8+rke2r1 Release Notes](https://github.com/rancher/rke2/releases/tag/v1.35.8%2Brke2r1 "RKE2 v1.35.8+rke2r1 Release Notes")
- [RKE2 v1.36.4+rke2r1 Release Notes](https://github.com/rancher/rke2/releases/tag/v1.36.4%2Brke2r1 "RKE2 v1.36.4+rke2r1 Release Notes")

## K3s

轻量级 Kubernetes 发行版 K3s 发布了 v1.36.4+k3s1 等一系列新版本，主要专注于上游同步与构建流程的优化。

### 系统改进与 Bug 修复

- **Kubernetes 补丁同步**：全面对齐 Kubernetes **v1.36.4**、**v1.35.8** 及 **v1.34.11**，引入了多项上游关于调度器与 API Server 的稳定性修复。
- **构建管道优化**：反向移植了多项测试框架与构建脚本的改进，确保在不同架构（ARM/AMD64）下的编译一致性。
- **基础镜像更新**：更新了内置的 mirrored-coredns 与 Local Path Provisioner，确保组件版本的安全性与现代性。

如需详细了解完整更新内容，请查阅：

- [K3s v1.34.11+k3s1 Release Notes](https://github.com/k3s-io/k3s/releases/tag/v1.34.11%2Bk3s1 "K3s v1.34.11+k3s1 Release Notes")
- [K3s v1.35.8+k3s1 Release Notes](https://github.com/k3s-io/k3s/releases/tag/v1.35.8%2Bk3s1 "K3s v1.35.8+k3s1 Release Notes")
- [K3s v1.36.4+k3s1 Release Notes](https://github.com/k3s-io/k3s/releases/tag/v1.36.4%2Bk3s1 "K3s v1.36.4+k3s1 Release Notes")

## Longhorn

Longhorn v1.12.1 作为最新的维护版本正式发布，不仅修复了关键的存储稳定性问题，还为 V2 数据引擎带来了多项极具工程价值的性能改进。

### 核心特性进阶

- **V2 数据引擎快速克隆 (Fast Cloning)**：增强了基于链接克隆 (Linked-Clone) 的架构，支持多个副本并行克隆，显著缩短了海量卷快照的恢复时长。
- **存储分片 (Experimental)**：引入了基于纠删码 (Erasure Coding) 的实验性存储分片功能，允许卷容量突破单一磁盘限制，并提供更高的容错空间效率。

### 安全与治理

- **默认启用内部网络策略**：为 Longhorn 内部组件（如 instance-manager）默认开启 Ingress NetworkPolicy，强制执行最小特权原则。
- **全量 mTLS 覆盖**：将双向 TLS (mTLS) 保护范围扩展至 instance-manager 所有的 gRPC 服务接口。
- **加密卷空间修正**：修复了 V2 数据引擎加密卷在保留 LUKS2 元数据时可能导致的可用容量偏差问题。

如需详细了解完整更新内容，请查阅：

- [Longhorn v1.12.1 Release Notes](https://github.com/longhorn/longhorn/releases/tag/v1.12.1 "Longhorn v1.12.1 Release Notes")

## 写在最后

感谢大家对 Rancher 社区的热情支持！希望这些更新能为您的云原生基础设施带来更高的安全性与生产力。如果您在升级过程中有任何心得或疑问，欢迎在社区论坛中与我们分享！

我们下期双周报再见！
