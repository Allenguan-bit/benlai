---
title: 我花了两天，用AI帮我抢到了一台免费的云服务器——然后在上面跑起了自己的AI
section: AI
date: 2026-05-20T09:00:00+08:00
---


> 一个 AI 小白用 Claude in Chrome 全程操控浏览器，从零开始申请 Oracle Cloud 免费层、搭建 AI 智能体平台、部署本地大模型的真实记录。很多技术概念，是东西装好之后才慢慢搞懂的。

---

## 序：那个"永久免费"的诱惑

如果你关注过云计算，你一定听说过 Oracle Cloud 的免费层（Always Free）。

它有一个让所有人都眼红的资源：**4 OCPU + 24GB RAM 的 ARM 服务器**，永久免费，不限时间。

对比一下：AWS、Azure、Google Cloud 的免费层，基本都是 1GB 内存以下的小玩意儿，够你跑个 Hello World。Oracle 给的这台，相当于一台真正可以做事的服务器——跑 Docker、部署 Web 应用、甚至跑本地 AI 大模型，都没问题。

但所有人都知道，这个资源有一个出了名的坑：**抢不到**。

Oracle Toronto 区域的 ARM 实例，几乎全年处于"Out of Capacity"（容量不足）状态。你填好表单点击创建，系统会直接报错，让你明天再来。明天来了继续报错。很多人等了几个月，从来没成功过。

这是我抢到之前对这件事的基本认知。

然后我决定试试。

---

## 第一天：账号、安全、网络——AI 帮我一步一步走

那是 2026 年 5 月 11 日，我打开了 Oracle Cloud 的控制台，准备开始设置。

我的底层需求很清楚：我想要一台自己的服务器，不依赖任何商业 AI API，在上面跑一个属于自己的 AI 智能体——能联网、能记忆、能处理我的私人知识库，同时成本接近零。

但我对 Oracle Cloud 几乎完全陌生——不只是 Oracle，对整个云计算和服务器这套东西，我都是门外汉。控制台界面对新人本来就不友好，各种术语——Compartment、VCN、Subnet、Security List、Route Table——光看名字就已经晕了。我当时的真实状态，是连这些词是什么意思都不知道，只是在 Claude 的带领下一步一步往下走，做完了再问"这个是干什么的"。

这时候我用了一个最近在玩的功能：**Claude in Chrome**。

这是 Anthropic 的一个 Beta 功能，可以让 Claude 直接控制你的浏览器——它能看到你的屏幕，能点击按钮，能填写表单，能截图分析页面状态。你坐在旁边，它帮你操作。

我把 Oracle Cloud 的标签页打开，对 Claude 说："我申请了 Oracle Cloud 账号，想利用它的 free tier，我现在已经 login，不熟悉它的功能和设置，你能帮我恰当地设置吗？"

然后……它就开始干活了。

### 第一步：账号安全

Claude 告诉我，在做任何事之前，先要保护好账号。它导航到 Identity 设置，帮我确认 MFA（多因素认证）已经开启——我的 iPhone 上有 Authenticator App，这个已经配好了。

然后它帮我创建了一个 Budget Alert（预算预警）：命名为 `free-tier-alert`，每月 $1 触发通知。

这一步的意义是：就算因为某个误操作产生了费用，系统会立刻发邮件提醒你，不会等到账单来了才发现。

### 第二步：搭建网络基础设施

云服务器不是孤立存在的，它需要网络环境。Oracle 把这套网络叫做 VCN（Virtual Cloud Network，虚拟云网络）。

Claude 帮我依次创建了：

**VCN：main-vcn**，IP 段是 10.0.0.0/16。这是整个私有网络的"地块"，16 位掩码意味着里面可以容纳 65000 多个 IP 地址，够用了。

**Internet Gateway：main-igw**。这是网络的"大门"，让 VCN 里的机器可以和互联网通信。没有这个，服务器就是个没有网的黑盒子。

**Public Subnet：public-subnet**，IP 段 10.0.0.0/24。这是 VCN 里的一个"子网区域"，放公网可访问的资源。

**Route Table**：配置了一条路由规则，把所有发往外网的流量（0.0.0.0/0）指向 main-igw。这是让内网机器能访问互联网的关键。

这些操作，如果让我自己来，至少要对着文档摸索一两个小时，还可能漏掉某个配置导致后面连不上网。Claude 直接把整个流程走完，我在旁边看着，偶尔确认一下。

### 第三步：生成 SSH 密钥

SSH 密钥是连接服务器的"钥匙"。Claude 指导我在 Windows 11 的终端里运行：

```
ssh-keygen -t ed25519 -C "oracle-cloud"
```

生成了一对密钥：
- **私钥**：存在 `C:\Users\我的用户名\.ssh\id_ed25519`，只放在本地，绝对不能外传
- **公钥**：`ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIEqCOGB6khFoLznlw0s3Efu5pnUTde9pOIm6zYnzV33 oracle-cloud`，这个要填入 Oracle 创建实例时的表单

这就是所谓的"非对称加密"：公钥可以公开，私钥自己保管，两者配合才能建立连接，不需要密码。

到这里，所有准备工作都完成了。可以开始创建服务器了。

---

## 最大的坎：ARM 容量抢占战

Oracle Cloud 的 ARM Ampere A1 实例，规格是这样的：

- **OCPU**：4 核（Oracle 自定义的 CPU 单位，大约等于 2 个物理核心）
- **内存**：24 GB
- **存储**：50 GB
- **价格**：永久免费

我填好了所有参数：
- 形状：VM.Standard.A1.Flex
- OCPU 数量：4
- 内存：24 GB
- 操作系统：Ubuntu 22.04
- SSH 公钥：粘贴进去

然后点击"Create"。

**Out of capacity.**

好，再试。

**Out of capacity.**

再试。

**Out of capacity.**

这是所有人都会遇到的墙。Toronto（ca-toronto-1）的 AD-1 可用区，常年容量不足。没有时间规律，没有通知，就是一遍遍报错。

这期间还发生了一个我自己犯的错误：

有一次终于显示创建成功了，我高兴坏了，结果仔细一看——创建出来的是 **E2.1.Micro + Oracle Linux**。这是 Oracle 默认的 AMD 小实例，不是我要的 ARM，内存只有 1 GB。我当时操作太快，没有检查表单的默认值，Oracle 的 UI 在某些情况下会默认回到 AMD 规格。

发现问题之后，我把那台错误的实例终止了，重新来。

**重试过程中还有一个坑**：连续点击"Create"太快，触发了 Oracle 的 Rate Limit（频率限制），直接返回"Too many requests"错误。解决方法是每次重试间隔 30 秒以上，不能无脑狂点。

就这样反复尝试，一直到 **5 月 12 日凌晨**，Toronto 那边悄悄释放了容量。

终端显示：**Create instance — Succeeded.**

实例状态：**Running.**

---

## 拿到服务器之后：防火墙、SSH、Docker

有了实例，还不能直接用。需要做几件事：

### 防火墙配置

Oracle 的安全模型分两层：
- **Oracle Security List**：云层面的防火墙，控制哪些端口对外开放
- **服务器内的 iptables**：系统层面的防火墙，Ubuntu 默认会把很多端口屏蔽

Claude 帮我在 Oracle 控制台的 Security List 里开放了 Port 22（SSH）、80（HTTP）、443（HTTPS）。

然后 SSH 登录服务器之后，又配置了 iptables 规则，允许这三个端口的入站流量，并用 `netfilter-persistent save` 把规则持久化——重启服务器之后规则还在，不需要重新设置。

### SSH 登录验证

```
ssh ubuntu@155.248.xxx.xxx -i ~/.ssh/id_ed25519
```

第一次连上去的感觉，很难描述。一个真实的 Linux 终端，4 OCPU，24 GB 内存，`free -h` 显示 23.4 GB 可用——这台机器是真实的，而且是免费的。

### 安装 Docker

```bash
sudo apt update
sudo apt install docker.io docker-compose -y
sudo systemctl enable docker
sudo systemctl start docker
```

Docker 29.0.3 安装完成，ARM 架构，运行正常。

至此，服务器环境准备完毕。

---

## 第二阶段：部署 AI 智能体平台

拿到服务器是目的，不是终点。我真正想要的，是在上面跑起来一个 AI 系统。

### 为什么要自己跑模型？

现在 AI API 很多，Claude、GPT-4、Gemini，随用随到，为什么还要自己部署？

几个原因：

**隐私**：我有自己的笔记库（Obsidian），里面有很多私人思考、投资分析、阅读记录。我不想把这些数据发给任何第三方 API。

**成本**：AI API 的 token 费用，用量大了会很贵。一台免费服务器加上本地模型，边际成本接近零。

**自主性**：我想要一个完全由自己控制的 AI，不受任何服务商的政策限制，不会因为 API 涨价或停服而中断。

### 选择 Dify

AI 智能体框架有很多：LangChain、AutoGPT、n8n、Flowise……我选了 **Dify**。

原因：
- 有完整的 Web UI，不用写代码也能配置 AI 工作流
- 支持 Docker 一键部署
- ARM 架构官方支持
- 内置知识库（RAG）功能，可以连接本地文档
- 活跃维护，中文社区好

### 选择 Ollama + Llama 3.1 8B

本地大模型的运行时，选了 **Ollama**。

Ollama 的优势是对 ARM 架构的原生支持非常好，在 Apple Silicon 和 ARM Linux 上都有大量优化。

模型选的是 **Llama 3.1 8B Q4 量化版**：
- 模型文件大小约 5 GB
- 24 GB 内存跑起来绰绰有余（加上 Dify 的各种服务，总内存占用大约 18-20 GB）
- Q4 量化：把模型权重从 32 位浮点压缩到 4 位整数，精度略有损失，但大幅减少内存占用和推理时间
- 在纯 CPU 上，推理速度大约 5-10 token/秒——慢，但对于个人工具来说够用

这台服务器没有 GPU，所有推理都是 CPU 计算。如果你对速度有要求，这不适合作为高并发服务，但作为个人工具，等几秒钟出结果完全可以接受。

### 部署过程

整个部署用 docker-compose 完成，Claude 帮我编写了配置文件，把 Dify 和 Ollama 放在同一个 Docker 网络里，Dify 可以直接访问 Ollama 的 API。

最终跑起来的容器包括：
- Dify API 服务
- Dify Web 前端
- Dify Worker（处理异步任务）
- Dify Sandbox（代码执行环境）
- PostgreSQL（数据库）
- Redis（缓存和队列）
- Nginx（反向代理）
- Ollama（模型推理服务）

12 个容器全部 Up，服务正常运行。

---

## 整个过程里，AI 帮我做了什么

回顾整个过程，Claude 参与了哪些环节？

**浏览器操控**：通过 Claude in Chrome，Claude 直接在 Oracle 控制台里帮我点击、填写、导航，不需要我逐步截图发给它再解释。这省去了大量"描述 UI 状态"的沟通成本。

**问题诊断**：当我说"好像出错了"，Claude 能直接看到页面，判断是 Rate Limit 报错还是容量问题，给出具体的处理方案。

**配置生成**：docker-compose.yml、iptables 规则、Nginx 配置，这些我自己写要花时间查文档和调试，Claude 直接生成可用的版本。

**架构规划**：我描述了我的需求——隐私、低成本、AI 工作流、本地模型——Claude 帮我选了 Dify + Ollama 这个组合，并解释了为什么这个组合适合我的情况。

**知识补全**：说实话，整个过程里我是先做、后懂。VCN 是什么、SSH 非对称加密怎么工作、Q4 量化是怎么回事、ARM 架构为什么特殊——这些概念，我都是在东西装好之后，回头问 Claude"这个我们刚才配的东西到底是干嘛的"，才慢慢搞清楚的。不是在理解之后再操作，而是操作完了再理解。这种方式也挺好的，至少不会被概念卡住，先跑起来再说。

---

## 踩坑总结：如果你也想申请

如果你打算去抢 Oracle Cloud 的 ARM 免费实例，这些是我的真实经验：

**一、ARM 容量没有规律，但凌晨相对容易**。Toronto AD-1 白天几乎全是 Out of Capacity，凌晨偶尔会有容量释放。不过这也不是绝对的，纯粹是碰运气加耐心。

**二、每次重试都要核对规格**。Oracle 的新版 UI 有时候会把 Shape 和 OS 默认回去，不要以为上次填的还在，每次提交前扫一眼：Shape 是 VM.Standard.A1.Flex，OCPU 是 4，内存是 24 GB，OS 是 Ubuntu 22.04。

**三、SSH Key 在新版 UI 里的位置变了**。不是在独立的步骤里，而是在 Step 3 Networking 下面。很容易漏填。漏填之后没法补救，只能终止重建——SSH Key 在实例创建之后无法添加。

**四、重试间隔保持 30 秒以上**，避免触发 Rate Limit。

**五、创建成功之后立刻记录公网 IP**。Oracle 不会发邮件通知你 IP 是什么，要自己进控制台查。

**六、注意区分 Oracle 防火墙和服务器 iptables**。两层都需要配置，只开了 Oracle 这层，服务器本身的 iptables 还会拦截流量。

---

## 结果：我现在有什么

一台运行在 Oracle Cloud Toronto 区域的 ARM 服务器：
- IP：155.248.xxx.xxx
- 规格：4 OCPU / 24 GB RAM / 50 GB 存储
- 系统：Ubuntu 22.04
- 费用：$0/月，永久

在这台服务器上运行的服务：
- **Dify**：AI 智能体平台，可以通过 Web 界面配置各种 AI 工作流
- **Ollama + Llama 3.1 8B**：本地大模型，数据不出服务器
- **Nginx**：反向代理，负责 HTTPS 和域名解析

我下一步计划把 Obsidian 笔记库接进来，让 AI 能基于我的知识库回答问题——真正属于我的私人 AI 助理，不是任何云服务的订阅用户。

---

## 最后说一句

很多人觉得"部署自己的 AI"是一件很复杂的事，需要很强的技术背景。

这次经历让我重新想了想这件事。

我不是运维工程师，也不是云计算专家，说实话连 AI 小白都算不上夸张——开始这个项目之前，我不知道 VCN 是什么，不知道 SSH 密钥和密码的区别，不知道 Docker 容器是怎么工作的。整个过程里，技术细节几乎都是 Claude 在处理，我主要做的是：**描述我想要什么，判断方向是否正确，在出错的时候保持耐心**。

这不是说技术不重要，而是说技术的门槛在变化。以前需要你自己查文档、自己踩坑、自己调试的部分，现在有了可以直接操控浏览器的 AI，门槛低了很多。

真正的坎是你到底想做什么——需求清不清楚，方向对不对，有没有耐心把事情做完。

ARM 实例抢到了，两天，无数次 Out of Capacity 之后。值得。

---

*如果这篇文章对你有用，欢迎转发。如果你有问题，评论区见。*

*服务器已在运行中，AI 智能体部署系列会持续更新——下一篇：如何把 Obsidian 笔记库接进 Dify，做一个真正懂你的私人 AI。*
