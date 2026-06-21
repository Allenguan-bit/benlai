---
title: AI 学习旅程回顾报告：From Zero to AI Agent Builder
section: ai
date: 2026-05-17T06:00:00+08:00
---

*2026年4月19日 — 5月17日  ·  Allen Guan  ·  Enoch Wealth Management  ·  Toronto*

---

> ⏱ **28天** 从听一场讲座到发布第一篇内容
>
> 🛠 **15+ 工具** 涵盖 AI 对话、智能体框架、自动化、知识管理、云端部署
>
> 🤖 **3个自动化系统** OpenClaw 智能体 + N8N 工作流 + Dify agent
>
> 📤 **4个内容平台** 小红书 · B站专栏 · X 中文 · X 英文

## 一、活动时间线

| 启蒙期 | 搭建期 | 扩展期 | 深化期 | 输出期 |
|:---:|:---:|:---:|:---:|:---:|
| 4/19–4/25 | 4/26–4/30 | 5/2–5/10 | 5/11–5/16 | 5/17 |

| 日期 | 阶段 | 活动内容 |
|---|---|---|
| 4月19日 | 启蒙期 | 王斗第一次讲座；首次接触 AI agent、OpenClaw、Claude、Notion；浏览大量 YouTube 学习视频；下载 N8N |
| 4月20日 | 启蒙期 | 继续浏览 YouTube（CloudGPT、Notion）；晚上下载 N8N |
| 4月21日 | 启蒙期 | 搜索 NotebookLM 功能和使用场景 |
| 4月23日 | 启蒙期 | 首次使用 Claude；分析 Mythos AI 网络安全报道；分析 Larry Fink 2026 主席致股东信 |
| 4月24日 | 启蒙期 | 搜索 Qwen、Manus；建立 allenguan.vercel.app 个人网站 |
| 4月25日 | 启蒙期 | 搜索智能体经济学相关内容 |
| 4月26日 | 搭建期 | 王斗第二次讲座；注册 AWS 账号；学习 Obsidian；深入学习 AI Skills、Token 经济学、AI 商业模式分析框架 |
| 4月27日 | 搭建期 | 与王斗第一次线下见面；安装 Obsidian；用 Cursor 搭建 OpenClaw |
| 4月28日 | 搭建期 | 与王斗第二次线下见面；继续用 Cursor 推进 OpenClaw 配置 |
| 4月30日 | 搭建期 | 完成 AWS Lightsail 上 OpenClaw 搭建，走通整个流程（Cursor 阶段完成） |
| 5月2日 | 搭建期 | Claude 上搭建加拿大自雇记账智能体（bookkeeping HTML 应用） |
| 5月3日 | 搭建期 | 注册域名 |
| 5月4日 | 扩展期 | 注册 Bitwarden；做 allenguan.com 网站；完成灵感生成器 APP 全流程；更新网站头衔 |
| 5月5日 | 扩展期 | 搜索 DDR5 内存/NAS 升级；搜索 Stripe、DeepSeek 4、Knab、Link；研究 OpenClaw 访问 Obsidian 方案 |
| 5月6日 | 扩展期 | 确定 Notion + Obsidian 两层知识管理工作流；迁移内容进 Obsidian |
| 5月7日 | 扩展期 | 修复 Git 自动同步链路；全面升级 Kyron 智能体架构（SOUL/MEMORY/TOOLS）；探索 Moltbook；研究 Claude Projects |
| 5月8日 | 扩展期 | 深入学习 Claude Projects；为太太公司设计税务自动化方案；排查 Telegram/Discord 跨平台连通 |
| 5月9日 | 扩展期 | Discord bot 权限配置 |
| 5月10日 | 扩展期 | NAS 部署 Dify agent（Docker + Ollama + Qwen2.5-7B）；调整 WinSCP 备份频率；讨论 Claude Projects 策略 |
| 5月11日 | 深化期 | NAS 搭建 N8N 自动化（Groq→Telegram）；讨论 Cursor/Claude Code 开发效率；解决 Claude Code 安装问题；深入学习 OpenClaw 核心文件；探索机票监控智能体；分析被动收入策略；开始申请 Oracle Cloud 免费账号 |
| 5月11–12日 | 深化期 | 申请 Oracle Cloud 免费账号；最大卡点：Toronto ARM 区域容量长期不足，需反复抢占；期间误建一台错误规格实例（E2.1.Micro + Oracle Linux），发现后删除重来；经历漫长等待后最终成功抢到 ARM 实例 |
| 5月13日 | 深化期 | Oracle Cloud ARM 服务器（4 OCPU/24GB RAM，免费）上部署 Dify 完整系统；安装 Ollama + llama3.1:8b + nomic-embed-text；配置 12 个 Docker 容器（含向量数据库 Weaviate、Nginx、Redis 等）；建立 Allen's Brain 知识库（上传 Obsidian MD + EMD产品PDF）；完成 Allen's Assistant 智能体（Chatflow + RAG）；全程由 Claude 提供架构方案和部署指引 |
| 5月14日 | 深化期 | OpenClaw Telegram/Discord 跨平台连通深入配置 |
| 5月15日 | 深化期 | N8N 自动化扩展（增加投资领域监控源，早晚推送） |
| 5月16日 | 深化期 | 完善 OpenClaw 核心身份文件；安装 soul-memory 技能；完成 Telegram 和 Discord 接入 |
| 5月17日 | 输出期 | 确定 AI 内容品牌平台矩阵；完成 obsidian-mcp 配置；制作开篇内容文章；整理本份时间线存档 |

### 阶段说明

| 阶段 | 时间 | 核心特征 | 关键转折 |
|---|---|---|---|
| 启蒙期 | 4/19–4/25 | 被动接受信息为主，快速浏览大量工具和概念，尚未动手 | 4/23 首次开启 Claude 对话，从消费者变成参与者 |
| 搭建期 | 4/26–4/30 | 从学习到动手，AWS 注册、Obsidian 安装、Cursor 搭建 OpenClaw | 4/30 走通 OpenClaw 全流程，第一个真实可运行的智能体诞生 |
| 扩展期 | 5/2–5/10 | 工具快速扩展：知识管理系统、自动化工作流、个人品牌基础设施 | 5/7 Kyron 智能体架构全面升级，从单一工具到系统化思考 |
| 深化期 | 5/11–5/16 | 从会用到会调试，Claude Code 取代 Cursor，开始理解底层逻辑 | 5/16 Telegram + Discord 双平台接入，智能体全面上线 |
| 输出期 | 5/17 | 从建设者到内容创作者，开始向外输出学习成果 | Obsidian 知识库连接 Claude，形成知识输入→处理→输出完整闭环 |

## 二、学习旅程分析

### 2.1 学习曲线与阶段特征

这28天的学习旅程可以清晰地划分为五个阶段，每个阶段都有鲜明的特征（见上表阶段说明）。

### 2.2 工具使用演变

工具积累的速度和广度，反映出这段时期学习的密度：

| 类别 | 工具 |
|---|---|
| AI 对话与编程 | Claude、Cursor、Claude Code、Gemini |
| 智能体框架 | OpenClaw（AWS）、Kyron、Dify（NAS + Oracle Cloud）、Allen's Assistant（RAG Chatflow） |
| 自动化工作流 | N8N、Telegram Bot、Discord Bot |
| 知识管理 | Obsidian、Notion、NotebookLM |
| 云端与服务器 | AWS Lightsail、Oracle Cloud ARM（4 OCPU/24GB 免费层）、GitHub、Git |
| 本地基础设施 | NAS（绿联）、Docker、Ollama、Qwen2.5-7B |
| 个人网站 | Vercel（vercel.app）、allenguan.com、Netlify |
| 安全与域名 | Bitwarden、域名注册 |
| 其他探索 | Stripe、DeepSeek 4、Knab、Moltbook |

### 2.3 核心认知转变

28天里发生了几次值得记录的思维跃迁：

- **从"工具用户"到"架构师"**：4月19日还在问各种工具是什么，5月中旬已经在设计多层自动化系统的数据流
- **从"复制粘贴代码"到"理解底层逻辑"**：5月11日那次关于 Cursor vs Claude Code 的对话是重要节点，你开始问"怎么读懂代码"而不只是"怎么跑通代码"
- **从"单点工具"到"系统化基础设施"**：Obsidian + Notion + Git + AWS + N8N 不是孤立的工具，而是一套有机的个人 AI 工作系统
- **从"学习者"到"内容创作者"**：5月17日的平台矩阵规划，标志着从积累期正式进入输出期

### 2.4 学习行为模式

回顾这段历程，几个行为模式比较突出：

- **高密度入门**：前7天（4/19–4/25）以广度为主，通过讲座、YouTube、搜索快速建立概念地图，没有过早深挖单一工具
- **以人为师**：王斗校长的两次讲座和两次线下见面是关键加速器，提供了方向感，避免了大量试错成本
- **做中学为主**：几乎所有工具都是在实际搭建中学会的，很少有纯学习不动手的阶段
- **问题驱动迭代**：每次遇到卡点（Git 同步故障、PowerShell 安装问题、跨平台连通等）都变成了下一步学习的入口
- **横向扩展快**：不满足于走通一条路，总在同时探索多个方向（Dify vs N8N、Cursor vs Claude Code 等对比实验）

### 2.5 下一阶段展望

基于前28天建立的基础，以下方向值得重点推进：

**优先级高：内容品牌运营**

小红书/B站/X 的内容矩阵已规划好，开篇文章已完成。持续输出是把学习旅程转化为影响力的关键。

**潜力方向：AI 工作系统与投资顾问业务整合**

现有的 N8N 信息推送、记账智能体等，可以逐步演化为服务高净值客户的专属工具。将 AI 能力与另类投资销售场景结合，是你独特的差异化路径。

**技术积累：Claude Code 深化使用**

已从 Cursor 过渡到 Claude Code，下一步是提升从"能跑通"到"能定制"的能力，尤其是在 OpenClaw/Kyron 智能体的个性化配置上。

**基础建设：知识库系统完善**

Obsidian + obsidian-mcp 已连通，下一步是把过去几年的投资研究、客户洞察、市场分析沉淀进去，让知识库真正发挥"第二大脑"的作用。

---

*报告生成日期：2026年5月17日  ·  Allen Guan  ·  Enoch Wealth Management*
