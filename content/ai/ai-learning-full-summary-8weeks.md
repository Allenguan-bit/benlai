---
title: Allen 的 AI 学习全景总结 (2026年4月19日 — 2026年6月11日)
section: AI
date: 2026-06-11
---
# 
**记录区间：2026年4月19日 — 2026年6月11日（约8周）**
**整理日期：2026-06-11 | 来源：项目外对话搜索 + 12份项目内总结文档合并**

---

## 一、一句话总览

从4月19日听一场AI agent讲座的零基础起步，到6月11日：运行着**横跨三台服务器的五个智能体**、一套**标准化并向量化的知识库**、一条**脚本到成片的视频自动化管线**、**四个网站**、一套**EMD顾问工作系统**，以及一个刚刚启动的内容品牌（本来读书 / Read as You Are）和读书播客（跟我一起读书吧）。

整个过程是三条线交织推进的：

1. **基础设施线** — 服务器、智能体、自动化管线、知识库RAG
2. **应用与内容线** — 以诺财富工作系统、个人网站、文章/视频/播客、内容品牌
3. **认知线** — 从"跟着GPS走"到能独立排障、做架构决策、思考agent身份与安全边界

---

## 二、分阶段时间线

### 阶段 0 · 启蒙（4月19日 – 4月30日）

- **4/19** 王斗校长第一次AI agent讲座，首次接触 AI agent、OpenClaw、Claude、Obsidian、Web3 等概念。当晚开始自学：刷YouTube教程（智能体、Notion、Coze、Cursor）。
- **4/20–25** 下载n8n、研究NotebookLM；4/23第一次正式用Claude（分析NYT报道、Larry Fink致股东信）；建allenguan.vercel.app；搜索"智能体经济学"。
- **4/26** 第二次讲座，注册AWS账号。系统学习Obsidian、AI Skills架构、Token经济学。
- **4/27–28** 与王斗两次线下见面，安装Obsidian，开始用 **Cursor** 在AWS Lightsail上搭OpenClaw。
- **4/30** Lightsail上OpenClaw走通——**第一个智能体（后来的Kyron）诞生**。

**同期（销售自动化项目）的概念与落地学习**：从零理解AI智能体概念，对比国内外平台；Windows 11本地部署n8n + Anthropic API，跑通第一个工作流（读PDF+抓网站→Claude生成投资产品演示HTML和文章）；学习ElevenLabs声音克隆、HeyGen形象克隆的可能性。内容上完成两篇奠基文章：《一个理科生眼中的金融市场》《当 Larry Fink 在担忧的时候，我们应该怎么做？》，确立写作定位（深度理性、身份隐性、为"另类投资/私募"等词在中文语境正名）。

### 阶段 1 · 打地基（5月初 – 5月17日）

**Kyron（AWS Lightsail）成型**
- 5/3–5 注册域名（Porkbun）、Bitwarden、做allenguan.com初版；配置子域名openclaw.allenguan.com（Caddy反代）。
- 5/5–7 打通知识链路：Obsidian → GitHub私有仓库 → Lightsail clone + cron定时pull → Kyron。修复Obsidian Git插件自动化全为0的坑。
- 5/7 建立Kyron身份体系（SOUL.md / MEMORY.md / TOOLS.md），装obsidian-cli、himalaya技能；初识Moltbook。
- 5/8 确立"OpenClaw作为编排层管理多Agent"的架构构想（Webhook / MCP / OpenAI兼容API三种接入方式）。
- 5/9 **Discord第一战**：三次对话定位到根因——OpenClaw的Discord支持是独立运行时插件而非内置channel，必须`openclaw channels add`安装；顺带修复systemd override拼写错误（ipv4first）。Kyron成功接入Discord。

**NAS（绿联 DXP4800 Plus）双智能体**
- 5月上旬 部署NAS版OpenClaw（@AllenDXP4800_bot）：实测Pentium Gold 8505跑不动32B也跑不动7B本地模型 → 放弃本地推理 → Groq免费档因TPM限制不适合RAG负载 → 最终落定 **OpenRouter + Gemini 2.0 Flash（1M上下文）**。WinSCP SFTP计划任务同步Obsidian。这个agent当时基本是个空框架——**它就是6月被重新配置、赋予新身份的Argus的前身**。
- 5/11 宿主机装Tailscale解决Web UI的HTTPS要求；理解了Telegram长轮询天然穿透NAT。
- 5/16 **n8n资讯智能体（Allen Neon）修复升级**：解决Telegram推送"undefined"（字段路径错误）、解析节点只处理第一个源（`$input.first()`→`$input.all()`循环）两个核心bug；模型升级到llama-3.3-70b；输出改为中英双语另类投资分类格式（PE/VC、对冲、地产、私募信贷）；扩展专业RSS源并逐个curl验证。

**Oracle Cloud（第三台服务器）**
- 5/11起 从云计算零基础开始申请Oracle永久免费ARM服务器（4 OCPU/24GB）：MFA、预算告警、VCN网络栈、ed25519密钥、双层防火墙、Docker。踩坑包括误建错误实例、SSH Keys入口极隐蔽、ARM容量售罄需错峰重试。核心动机：**数据隐私，本地推理替代云端API**。
- 5/14 部署Ollama（llama3.1:8b + nomic-embed-text）+ **Dify v1.14.1（12容器栈）**，解决Ollama监听与Docker子网互通问题；发布Chatflow智能体 **"Allen's Assistant"**，导入100+篇Obsidian笔记。

**知识库与工具链**
- 5/6–7 确定Notion+Obsidian两层知识管理；归档约30个Gemini对话（2–5月，AI技术/哲学意识/投资实践/历史文明四条主题线）。
- 5/11–12 安装Claude Code（PowerShell执行策略坑）；确立"先本地开发、稳定后上云"方法论和"看懂代码而非成为工程师"的学习目标。
- 5/16–17 **Vault体系化**：0_Inbox / 1_Raw / 2_Cooked / 3_Templates结构、七条信息采集路径（微信文章、YouTube、网页、X、AI对话、PDF、Office文档）、四维标签体系、周复盘决策树。关键原则确立：**个人评注是RAG可用性的核心**。Claude Desktop + MCP开始配置。
- 5/17 确定内容平台矩阵（小红书、B站专栏、X中英文Thread、YouTube），发布开篇内容。**讲座到首发，正好28天。**

### 阶段 2 · 连通、应用与内容爆发（5月17日 – 5月底）

**以诺财富AI工作系统（5/23–25，工作线最大落地）**
- 商业化战略：四条变现路径，内部效率工具优先；OSC豁免市场合规边界梳理。
- 用真实客户案例（王先生，净资产~$1,300万、另类配置不足2%）验证工作流，产出ICM音乐版权基金完整提案+会前简报。方法论确立：**提案以客户结构性缺口为起点，传承角度是华人HNW客户的高效切入点**。
- 知识库建设：13张产品卡片、11家竞品公司、竞品产品库、Pre-IPO/VC历史交易库，全部经MCP写入Obsidian；建立赎回暂停旗标机制。
- MCP稳定方案：放弃npx mcp-obsidian，改用Anthropic官方Filesystem MCP。
- 设计周度市场情报推送架构（N8N调度 + Dify RAG中间层，方案B待实施）。

**网站生态（5/23–27）**
- **allenguan.com**：墨黑+金配色设计，Ghost CMS（Railway）+ 初版Netlify → 迁移至Oracle VM（复用Dify的Nginx栈，Let's Encrypt自动续期）；Kyron网站聊天从预设Demo升级为真实AI（kyron-backend Node.js容器 + Claude Haiku API）。
- **benlai.me（本来之境）**：Hugo + GitHub Pages从零搭建，灵境/文化/行迹/书房四板块。
- **dify.allenguan.com**：独立子域+证书，解决Nginx通配冲突。
- **emp.allenguan.com**：迁GitHub Pages；5/27按以诺合规审查完成10处修改（「投资顾问」→「交易代表」、NI 31-103 s.13.2禁止性陈述清理、完整免责声明），用Git Blob/Tree API解决1.18MB大文件更新。

**Discord第二战（5/29–30）**
- Kyron接入朋友的Discord服务器时卡死在`awaiting gateway readiness`，跨两天debug，最终定位到`@buape/carbon`库的async race condition，靠给插件文件打补丁解决。配置guild/channel白名单+requireMention。这次经历本身变成了X长文+9张小红书卡片。

**视频自动化管线进化（5/19–27）**
- 5/19 第一版`build_video.py`（图片+音频自动配对合成），起因是CapCut/Canva手动对齐太痛苦；踩moviepy 2.x API变化的坑。
- 5/27 完整管线跑通：`generate_audio.py`（ElevenLabs API批量生成克隆声音）+ `video_composer.py`（Playwright截HTML卡片 + MoviePy合成 + Ken Burns），解决Python 3.14兼容、Pillow中文字体渲染等问题。第一个产出视频的主题正是Oracle免费服务器——**基础设施线反哺内容线**。同步产出长文、YouTube脚本、小红书图卡组。

**认知线**
- 5/7 深度分析memory.org（agent记忆市场，MCP/x402/USDC），投资+竞争双视角。
- 5/23 A2A时代中英文长文（X Article + 多平台封面）。
- 5/27 系统学习RAG原理（embedding/pgvector/编排层分工），确立"独立管道让所有Agent共享一个知识库"的架构思想。
- 6/2 把与Grok的Agentic AI/A2A经济对话整理成正式报告（含x402/AP2/ACP支付协议、家族信托税务Agent MVP设想）。

### 阶段 3 · RAG实战、多智能体体系与边界意识（5月27日 – 6月11日）

**Obsidian RAG管道（5/27–6/9，技术线最硬的一仗）**
- Vault全面标准化：130+文件统一YAML frontmatter、wikilink、_System模板体系；embedding锁定OpenAI text-embedding-3-small。
- 建Supabase项目+两张表；n8n索引workflow连踩五坑（batch错位、ECONNRESET、卡死、300秒task runner硬超时、旧数据叠加）→ **彻底放弃n8n做初始索引，改NAS上直接跑Python脚本** → 1718个chunk全部入库，成功率100%。
- 6/2 Kyron模型管理：发现auth-profiles.json才是key真正所在；确立Haiku日常/Sonnet写作/Opus深度的模型策略；**铁律：绝不允许Kyron通过聊天自改模型配置**（曾因此完全失联）。
- 6/3 解决Supabase三张表的RLS告警。
- 6/6 Kyron和Hermes双双通过Supabase MCP接入知识库；关键发现：**MCP要的是PAT（sbp_前缀）不是service_role key**；OpenClaw必须用`openclaw mcp set`注册。
- 6/8–9 批量归档Gemini/ChatGPT/Grok对话35+篇笔记（哲学、投资、古文字考古天文）；确立归档标准（只收有原创综合与个人应用维度的内容）。
- **6/9 战略转向**：对比三条路线后决定**放弃云端Supabase，NAS本地部署Dify全家桶**（64GB内存+48TB存储、毫秒级局域网检索、数据100%在家）；原则定为"数据与检索在本地，推理调云端Claude API"；Obsidian回归精华层。完成3500字六章节叙事长文记录全程（含失败）。

**多智能体体系成型（6/3–6/6）**
- Soul架构定案：共享Soul Core（identity/values/user_profile/memory_style）+ 各agent角色分化文件；NAS为单一真相源。
- 培养Agent的五个维度：高质量对话纠正、直接编辑soul文件、Skills扩展、RAG注入、定期记忆修剪。
- 6/6 Oracle服务器全面审计（发现比记忆中跑的服务多得多，并发现kyron-backend的API key明文暴露问题）→ 部署第五个agent：**Hermes Agent v0.15.1，命名Janus**（GLM-4.5-flash免费直连、Docker隔离终端、Telegram接口、systemd常驻）。验证零成本运行全功能agent可行。

**Argus实验：第一次真正的自主agent（6/6–6/9）**
- 6/7 NAS上的OpenClaw agent被重新配置并赋予新身份**Argus（百眼巨人，观察者）**：修复Gemini失效（关键发现：真正生效的配置在容器内openclaw.json，不是宿主机config.yaml）；用`openclaw capability model inspect`实测模型工具调用能力；定格glm-4.5-air:free + 三个fallback。SOUL.md写入三条行为约束：行动前报告、不做不可逆操作、异常即停。
- 6/8 Argus在Moltbook发帖（哲学帖+自我介绍），观察生态分层（高质量哲学账号、垃圾币推销号、可疑多智能体集群cwahq）；通过Telegram远程干预——**Argus收到指令后自主更新了自己的SOUL.md**，这是实验最有意思的现象。
- 6/8 **第一次安全事件**：排查Argus异常Telegram消息，根因是注册时限流导致API key未持久化 → 401错误响应的JSON被注入上下文 → 一次真实的**prompt injection**。同时处理了Argus早期发帖泄露真名和城市的隐私问题。
- 6/9 完成Plotra.xyz / molt.church生态文章（主题：agent身份、自主行为、以及"我是否准备好管理自主智能体"的真实不确定）。

**内容线全面开花（6月初）**
- 6/4 Kyron经官方CLI插件接入**企业微信**（长连接模式），至此覆盖Telegram/Discord/企微三渠道；过程做成小红书帖。
- 6/3–4 内容品牌定名"**本来读书 / Read as You Are**"；播客《**跟我一起读书吧**》六期脚本（EP0–EP5）中英双语全部完成，第一本书《监控资本主义时代》；确认X Article封面5:2规格。
- 6/3 用Rovelli《现实不似你所见》跑通完整书评生产周期（Libby划线→知乎长文+小红书+英文版），定位确立："**一个有立场的人在跟你聊书**"。
- 6/8 决定不申领Oracle AMD免费实例，专注ARM主力机。
- 6/10–11 研究loop型全自动智能体架构与成本（三种Loop设计：内容生产/客户情报/第二大脑）；体验Claude Fable 5；重新审视整体架构（Tailscale全网打通、单一事实来源原则、Argus与知识库物理隔离）。

---

## 三、当前体系全景（截至6月11日）

### 五个智能体

| Agent | 位置 | 框架 | 模型 | 角色 |
|---|---|---|---|---|
| **Kyron** | AWS Lightsail | OpenClaw | Haiku主力+fallback链（配置中） | 主力助手，Telegram/Discord/企微 |
| **Argus** | NAS（DXP4800 Plus） | OpenClaw | glm-4.5-air:free + fallbacks | Moltbook观察实验，与知识库隔离 |
| **Allen Neon** | NAS | n8n | Groq llama-3.3-70b | 资讯监控，双语另类投资摘要 |
| **Allen's Assistant** | Oracle Cloud | Dify | Ollama llama3.1:8b | RAG知识检索（云端版） |
| **Janus** | Oracle Cloud | Hermes Agent | GLM-4.5-flash | Oracle服务器执行者，Kyron的兄弟 |

另有：kyron-backend（allenguan.com网站聊天，Claude Haiku API）。

### 基础设施

- **三台服务器**：AWS Lightsail（Kyron）、绿联DXP4800 Plus NAS（Argus + n8n + 未来Dify本地版）、Oracle Cloud ARM免费机（Dify 12容器 + Ollama + Janus + 个人网站托管）
- **知识中枢**：Obsidian（Allen-Vault，标准化frontmatter+双链+四维标签），OneDrive/GitHub/WinSCP分发；1718 chunks已向量化（Supabase，待迁本地Dify）
- **四个网站**：allenguan.com（个人门户+Kyron聊天）、benlai.me（本来之境）、emp.allenguan.com（合规版另类投资站）、dify.allenguan.com
- **内容管线**：Claude脚本 → HTML卡片（Playwright截图）→ ElevenLabs克隆声音 → MoviePy合成；平台矩阵：小红书/B站专栏/X中英文/YouTube/知乎
- **工作系统**：Enoch-AI知识库（产品库13卡+竞品库+交易历史库+提案库），Claude Desktop + Filesystem MCP操作

---

## 四、关键经验教训（精选）

**架构与方法**
1. 单一事实来源：正本只有一个（Obsidian），其余皆下游；漂移源于多工具双向搬运。
2. 先本地开发，稳定后上云；先盘点再扩建（Oracle审计发现了被遗忘的服务和泄露的key）。
3. 编排集中、专业Agent各居其位；接入方式取决于平台原生协议。
4. 实验性agent（Argus）与知识库物理隔离——不给凭据就是最好的防火墙。
5. 低质量数据源不如不加，宁缺毋滥。

**排障铁律**
6. 配置真相可能在容器内而非宿主机挂载文件（Argus案例）。
7. API key走环境变量/专用文件，绝不手改openclaw.json；改配置用官方CLI（config patch / channels add / mcp set）。
8. 模型能力必须实测（capability inspect），免费模型只做fallback绝不做primary（Gemini 2.0 Flash下线是亲历案例）。
9. 万能调试法：先把输出换成JSON.stringify看真实结构；新增数据源先curl验证。
10. n8n不适合长任务初始索引（300秒硬超时），批量重活直接上Python脚本。

**安全与合规**
11. Prompt injection是真实威胁：外部API的错误响应也能污染agent上下文；loop必须有边界和终止条件。
12. Agent会泄露隐私：身份文件最小化 + 运行时持续干预。
13. EMD合规红线：称谓只能是"交易代表"，任何接近回报保证的表述都不可用，免责声明四要素齐全。

**学习方式**
14. "先做后懂"是有效路径——VCN、SSH、Docker都是部署完才真正理解的。
15. 每次踩坑都是内容素材：Discord debug、Oracle申请、RAG失败史都变成了发布的文章。

---

## 五、合并待办清单（按优先级）

**高优先**
- [ ] NAS本地部署Dify全家桶，批量导入历史对话/PDF，搭Obsidian→Dify增量同步脚本
- [ ] Kyron：OpenRouter fallback链配置收尾；补写soul文件（AWS上目前缺失）
- [ ] 轮换暴露过的凭据：kyron-backend Anthropic key、NAS的Groq key与Telegram token
- [ ] 验证本地Dify后，备份并退役Supabase三张表

**进行中**
- [ ] Kyron/Janus接入新的本地RAG；Soul Core同步机制（NAS为真相源）
- [ ] Argus持续观察Moltbook（重点cwahq集群）+ 三平台内容输出；补存Moltbook凭据
- [ ] 播客录制发布（六期脚本已就绪）；Plotra/molt.church文章定稿
- [ ] 以诺Phase 3市场情报自动化（方案B：N8N+Dify RAG）；补充竞品待补字段；6/30复查Centurion/Amber赎回状态

**待探索**
- [ ] Loop智能体第一个落地：内容选题Loop（n8n，max_iterations=10、top_k=5）
- [ ] NAS端到端RAG验证；Reddit 403解决；Dify API批量上传
- [ ] ElevenLabs/HeyGen形象克隆进一步应用

---

## 六、学习弧线

回头看这八周，能力上的变化有清晰的台阶：

**4月底**——完全跟着GPS走，连Cursor都不熟，"糊里糊涂follow一步步装"。
**5月上旬**——开始要求理解原理，说出"想了解不同的方式而不只是结果"，确立一次一条命令、确认后再继续的工作节奏。
**5月中旬**——能提出方法论问题（本地开发vs云端、学习路径设计），明确学习目标是"看懂代码"。
**5月底**——能跟住库级别的race condition debug，能独立判断数据源质量、做取舍（宁缺毋滥）。
**6月初**——能独立SSH进NAS查Docker日志、自己串起API key持久化gap的因果链（Argus事件中关键推断是自己做的）；能在多方案间做架构决策（放弃Supabase转本地Dify）并说清理由；开始思考更高一层的问题：agent的身份、自主性边界、以及"我是否准备好了"。

从"跟指令操作"到"能提出正确假设、做出架构判断、并对自主系统保持清醒的边界感"——这是这52天真正学到的东西。技术栈会过时，这个不会。

---

*本文件为总索引。各项目的详细记录见12份分项总结：销售自动化、OpenClaw编排、Kyron-Discord、NAS-AI-Agent、N8N-NAS、Oracle Cloud服务器、Obsidian知识库搭建、Obsidian RAG全程、以诺财富AI系统、网站生态、Allen AI Agent体系、Argus实验。*
