---
title: 我花了大半天，让Claude真正"住进"我的Obsidian知识库
section: AI
date: 2026-05-17
---


*——一个AI新手的真实踩坑记录*

---

## 先说说我是谁

我不是IT背景，过去几年一直在关注AI相关的新闻，知道这东西很厉害，但始终停留在"有概念、没动手"的阶段。每次看到别人分享AI工作流，心里觉得很酷，但不知道从哪里下手。

三周前，我遇到了极客教的王斗校长。他讲的一句话让我真正开了窍：**AI agent 的时代已经到了，而且几乎不需要编程基础就能参与。**

从那一刻起，我开始动手。三周下来，已经搭建跑通了几个AI智能体项目。今天才想着要开始跟大家分享这个过程——之前踩的坑、正在做的事、以及接下来的探索。

这个系列，记录的就是我从零开始的真实路径。不是教程，不是攻略，是一个普通人真实的成长过程——包括卡壳的时刻，还有最终搞定时那种说不清楚的成就感。

今天这篇，讲的是**让Claude真正"住进"我的Obsidian知识库。**

---

## 为什么要做这件事

开始折腾AI agent之后，我才知道了Obsidian这个工具。最初用的是网页版，收录了一部分个人资料。但后来发现桌面版更方便整理电脑里已有的笔记和资料，于是今天决定改用桌面版。

就是这个"改用桌面版"的决定，让我掉进了一个接一个的坑。

我想实现的是：让Claude直接读写我的Obsidian知识库，能搜索内容、发现笔记之间的关联、帮我整理。而不是每次都靠手动复制粘贴。

---

## 先说结论

折腾了大半天，踩了将近十个坑，但最终实现了：

- Claude 可以直接读写我本地的 Obsidian vault
- 支持中文笔记内容搜索
- 电脑、OneDrive、手机三端同步正常

值得吗？值得。

---

## 两种方案，各有用处

连接 Claude 和 Obsidian，有两条路：

**方案A：Filesystem 连接器**
Claude Desktop 内建的工具，直接授权一个本地文件夹路径。三分钟搞定，稳定可靠，适合文件读写操作。

**方案B：obsidian-mcp**
通过 MCP（Model Context Protocol）安装的第三方服务器，支持按内容语义搜索、标签管理、笔记整理。功能更强，但配置更复杂。

最终两个都装，分工合作：Filesystem 负责结构性操作，obsidian-mcp 负责内容搜索和笔记管理。

---

## 第一章：方案A，三分钟搞定

方案A非常简单：

1. 打开 Claude Desktop → Settings → Integrations
2. 找到 Filesystem 连接器
3. 添加路径：我的 vault 所在的本地文件夹
4. 完成

测试一下，让Claude列出知识库的文件夹结构——秒出结果。

```
[DIR] Cooked
[DIR] Inbox  
[DIR] Raw
[DIR] Templates
```

方案A通了。

---

## 第二章：方案B，开始踩坑

方案B需要配置一个 JSON 文件，告诉 Claude Desktop 去哪里找 obsidian-mcp 服务器。

### 坑一：配置文件在哪里？

普通版 Claude Desktop 的配置文件在：
```
C:\Users\[用户名]\AppData\Roaming\Claude\claude_desktop_config.json
```

但我装的是 **Microsoft Store 版**，路径完全不同：
```
C:\Users\[用户名]\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude_desktop_config.json
```

找这个路径花了不少时间。

### 坑二：PowerShell 写入中文路径会乱码

我的知识库叫"Allen的知识库"，用 PowerShell 写入配置文件后，中文变成了 `????`。

```json
"OBSIDIAN_VAULT_PATH": "C:\\Users\\...\\Allen????"
```

解决方法：用记事本手动打开文件粘贴内容，保存时确认编码是 UTF-8。

### 坑三：obsidian-mcp 不接受环境变量传路径

我最初把 vault 路径放在 `env` 里，结果 obsidian-mcp 每次启动就打印使用说明然后退出。原来它需要把路径作为**命令行参数**传入：

```json
"args": ["-y", "obsidian-mcp", "C:\\Users\\...\\Allen的知识库"]
```

### 坑四：中文 vault 名让 obsidian-mcp 罢工

配置终于写对了，但搜索一直卡死。去看日志，发现：

obsidian-mcp 会把 vault 名称转换成英文，中文字符全部丢弃。"Allen的知识库"被转成了 `d-note`——只剩下最后几个可识别的字母，搜索完全失效。

**解决方案：把 vault 名改成英文。**

---

## 第三章：vault 英文化，引发三端同步混乱

把知识库根目录从"Allen的知识库"改成"Allen-Vault"，同时把所有中文文件夹名改成英文：

| 原来 | 改为 |
|------|------|
| 01-AI进化日志 | 01-AI-Log |
| 02-投资知识库 | 02-Investment |
| 03-碎片收藏 | 03-Fragments |
| 随想 | Journal |
| 中医 | TCM |
| ... | ... |

改完之后，obsidian-mcp 终于正常——vault 被识别为 `allen-vault`，搜索秒出结果。

但新的问题出现了。

### 坑五：中英文文件夹并存

改名操作失误，创建了新的英文文件夹，但旧的中文文件夹还在。vault 里同时存在两套结构。用 PowerShell 逐一删除才解决。

### 坑六：Remotely Save 插件把中文文件夹推回来

电脑端删干净了，但手机端 Obsidian 还有中文文件夹。我用的是 **Remotely Save 插件**做手机和电脑之间的同步——它会把手机本地文件 push 到 OneDrive，再同步到电脑。

结果：电脑刚删完，手机的 Remotely Save 又把中文文件夹推回来了。

理清这个三层结构之后才找到正确顺序：

```
电脑 Obsidian（直接读写 OneDrive 文件夹）
        ↕ OneDrive 自动同步
      OneDrive 云端
        ↕ Remotely Save 插件
手机 Obsidian（手机本地存储）
```

**正确操作顺序：**
1. 手机端 Remotely Save 改为 Pull only 模式
2. 电脑端删干净所有中文文件夹
3. 等 OneDrive 同步完成
4. 手机端手动触发 Pull
5. 手机本地残留中文文件夹手动删除
6. 恢复双向同步

---

## 最终效果

配置完成后，我测试了一句话：

> "搜索我笔记里关于意识的内容"

结果秒出：

```
Found 5 matches in 5 files

Cooked\Journal\2018-02-26 精神分裂症与神秘主义——纳什与意识的边界.md
Cooked\Journal\2018-05-26 GEB——怪圈、意识与色即是空.md
Cooked\Journal\2018-12-19 禅修诱导的濒死体验MI-NDE——意识的边界.md
Cooked\Journal\2019-07-10 科学与无意识——原型意象与物理学的汇合.md
Cooked\Journal\2022-08-24 Chico Xavier——巴西著名灵媒与意识的非还原性解释.md
```

从2018年到2022年，横跨四年的思考痕迹，一秒浮现。

这才是我想要的感觉。

---

## 几个值得记住的教训

**1. Store 版和普通版 Claude Desktop 配置路径不同**
用 PowerShell 查进程路径来判断自己装的是哪个版本。

**2. obsidian-mcp 不支持中文 vault 名**
vault 根目录和所有文件夹名用英文，笔记内容是中文完全没问题。

**3. 多端同步要先理清层次结构**
搞清楚"谁同步谁"，再决定操作顺序，否则会陷入反复覆盖的循环。

**4. 先用 Filesystem，再用 obsidian-mcp**
Filesystem 简单稳定是基础，obsidian-mcp 是进阶。两个搭配使用效果最好。

---

## 写在最后

三周前我还完全不知道从哪里下手。今天我让Claude真正读进了我的知识库。

这不是我三周里做的第一件事，但是我决定开始分享的第一篇。接下来我会持续记录——之前做过的、正在做的、以及接下来要探索的。从最初的懵懵懂懂到逐渐找到节奏，都会在这里。

如果你也是非IT背景，也在观望要不要开始，这个系列或许能给你一点参考。

**工具搭好了，重头戏才刚开始。**

---

*极客教王斗校长是让我真正开始动手的引路人。*

*这是我 AI agent 学习旅程系列的开篇。*
