# Rancher 社区双周报| Rancher 2.5 EOL

## Rancher

一月份，Rancher 同时发布了三个版本，分别是：v2.5.17、v2.6.10、v2.7.1。其中，**v2.5.17 是 2.5 系列的最后一个版本，此版本结束了对 Rancher 2.5 的支持，请升级到更新版本的 Rancher 来获得持续支持**。Rancher 生命周期可通过 https://www.suse.com/lifecycle/ 查阅。

这三个版本均为安全版本，用于修复旧版本中存在的安全漏洞，并没有增加新功能或者 Bug 修复。

- 修复了 Rancher 的 Git 包中可能导致命令注入的问题。有关详细信息，请参阅 CVE-2022-43758。
- 修复了敏感字段和凭证（如 secret token、加密密钥和 SSH 密钥）以明文形式存储在 Kubernetes 对象上的问题。这是一个后续安全修复程序，用于解决 CVE-2021-36782 中遗漏的字段。有关详细信息，请参阅 CVE-2022-43757。
- 改进 Rancher 的 `cattle-token` 的生成过程，使 token 随机化。之前，`cattle-token` 在其组合中没有使用任何随机值，这会导致 token 始终是可预测的。有关详细信息，请参阅 CVE-2022-43755。
- 修复了一个授权逻辑漏洞，该漏洞允许任何下游集群上的经过身份验证的用户可以在 local 集群中获得未经授权的 shell pod 和 kubectl 访问权限。有关详细信息，请参阅 CVE-2022-21953。

此外，这三个版本中还修复了一些其他安全相关的问题，更多发布说明请参考：

- https://github.com/rancher/rancher/releases/tag/v2.5.17
- https://github.com/rancher/rancher/releases/tag/v2.6.10
- https://github.com/rancher/rancher/releases/tag/v2.7.1

## K3S

K3s 发布了 v1.23.16+k3s1、v1.24.10+k3s1、v1.25.6+k3s1 和 v1.26.1+k3s1。

这些新版本除了提升了支持的 Kubernetes 的版本之外，还将 `stable` 版本提升到了 `v1.25.5+k3s2`，同时这些版本也修复了许多关键的问题。

值得大家注意的是以上 4 个版本都更新了内置的 containerd 版本，这是为了修复 pod 在 containerd 重新启动时会丢失 CNI 信息，有可能会导致 kubelet 重新创建 pod 的问题。受影响的 containerd 版本为 `v1.5.15`、`v1.6.9 至 v1.6.14`，所以如果你的 K3s 使用的是这些 containerd 版本，可通过升级 K3s 版本解决该问题。

另外，你可以通过在 K3s 集群中使用 `k3s ctr version` 或在各 K3s 版本的 release note 中查看 K3s 内置的 containerd 版本号。

更多发布说明请参考：

- https://github.com/k3s-io/k3s/releases/tag/v1.23.16+k3s1
- https://github.com/k3s-io/k3s/releases/tag/v1.24.10+k3s1
- https://github.com/k3s-io/k3s/releases/tag/v1.25.6+k3s1
- https://github.com/k3s-io/k3s/releases/tag/v1.26.1+k3s1

## RKE2

REK2 发布了 v1.23.16+rke2r1、v1.24.10+rke2r1、v1.25.6+rke2r1 和 v1.26.1+rke2r1。

这些新版本除了提升了支持的 Kubernetes 的版本之外，还修复了一些关键的问题，同时也将 `stable` 版本提升到了 `v1.24.9+rke2r2`。

更多发布说明请参考：

- https://github.com/rancher/rke2/releases/tag/v1.23.16%2Brke2r1
- https://github.com/rancher/rke2/releases/tag/v1.24.10%2Brke2r1
- https://github.com/rancher/rke2/releases/tag/v1.25.6%2Brke2r1
- https://github.com/rancher/rke2/releases/tag/v1.26.1%2Brke2r1

## RKE

RKE 发布了 v1.3.18 和 v1.4.2，这两个 rke 新版本提升了支持的 kubernetes 版本：

**RKE v1.3.18 支持的 Kubernetes 版本：**

| Kubernetes 版本           |
| ------------------------- |
| v1.24.9-rancher1-1 (默认) |
| v1.23.15-rancher1-1       |
| v1.22.17-rancher1-1       |
| v1.21.14-rancher1-1       |
| v1.20.15-rancher2-2       |
| v1.19.16-rancher2-1       |
| v1.18.20-rancher1-3       |

**RKE v1.4.2 支持的 Kubernetes 版本：**

| Kubernetes 版本           |
| ------------------------- |
| v1.24.9-rancher1-1 (默认) |
| v1.23.15-rancher1-1       |

更多发布说明请参考：

- https://github.com/rancher/rke/releases/tag/v1.3.18
- https://github.com/rancher/rke/releases/tag/v1.4.2

## Elemental

Elemental 是一个软件堆栈，可通过 Kubernetes 实现集中式、完整的云原生操作系统管理解决方案。集群节点操作系统通过 Elemental Toolkit 的容器镜像构建和维护，并使用 Elemental CLI 安装在新主机上。

Elemental Teal 于 2022 年 12 月正式发布，最新的 Elemental 可以帮助用户从 Rancher Manager 2.7.0+ 部署和运行 Kubernetes 集群（K3s 或 RKE2）。 我们也在 2023 年 1 月份发布了 v1.1.0 版本，该版本主要以修复 Bug 为主，同时也增加了一些新功能。

发布说明和文档请参考：
- https://github.com/rancher/elemental/releases/tag/v1.1.0
- https://elemental.docs.rancher.com/