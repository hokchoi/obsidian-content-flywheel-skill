# Obsidian Content Flywheel Skill

Use AI to end bookmark hoarding and turn saved material into a sustainable content output system.

把收藏夹、转录稿、网页长文、推特/X、小红书图文，变成一个由 Obsidian 驱动的内容生产飞轮。

很多内容创作者的问题不是信息不够，而是信息无法被再次调用：收藏夹越来越大，选题越来越空，真正写的时候大脑一片空白。这个 skill 的目标是让 AI 承担最枯燥的清洗、拆解、链接和多平台重组工作，把创作者真正需要负责的部分留给人：连接、洞察、判断和审美。

## Why This Exists

传统的「XX选题」文件夹很容易变成资料坟场：

- 链接越存越多，但没有被拆成可复用的知识原子
- 看过的爆款内容没有和自己的历史案例库发生连接
- 每次创作都从空白页开始，而不是从已有知识网络中生长
- AI 只被用来写初稿，没有被用来处理更关键的「输入到选题」环节

这个 skill 把内容生产拆成一条更稳定的链路：

```text
原始材料 -> 清洗 -> 四维知识矩阵 -> Obsidian 双链 -> 选题种子 -> COPE 多平台分发
```

## Core Workflow

### 1. Clean Raw Material

输入可以是长视频转录稿、播客文本、网页长文、newsletter、推特/X thread、小红书图文或零散收藏链接。

AI 会先移除：

- 口水话
- 赞助商广告
- 重复铺垫
- 空洞修辞
- 无信息量的转场

保留：

- 关键观点
- 具体案例
- 数据、人物、日期、因果关系
- 可以变成钩子的句子
- 可以沉淀为流程的方法论

### 2. Extract A Four-Dimensional Knowledge Matrix

每条材料会被强制拆成四类知识原子：

| Dimension | Question |
|---|---|
| Counterintuitive insight | 有没有打破常规认知的观点？ |
| Emotional anchor | 哪些案例、冲突或金句最容易引发共鸣？ |
| Method framework | 能否沉淀为读者立刻能用的模型或步骤？ |
| Underlying logic | 现象背后的经济学、心理学、技术或运营本质是什么？ |

### 3. Connect New Notes To The Existing Obsidian Graph

这个 skill 不把 Obsidian 当作文件夹，而是当作可生长的思考图谱。它会搜索已有笔记，并按照这些关系提出双链建议：

- 同一个用户痛点
- 同一个底层机制
- 同一种案例类型
- 同一个工具或工作流
- 相反观点
- 可以继续追问的问题

每条链接都需要说明为什么连接，避免只因为关键词相同就制造噪音。

### 4. Generate Topic Seeds

选题种子不是标题，而是一个待发布的论点。每个选题种子会包含：

- 一句话论点
- 为什么现在值得讲
- 目标读者痛点
- 来源知识原子
- 关联的历史笔记
- 平台适配度
- 还缺什么证据
- 风险：什么会让这个选题变浅、变错、变无聊

### 5. Recompose With COPE

COPE = Create Once, Publish Everywhere.

一个观点会被重新组织成不同平台需要的形态，而不是简单复制粘贴：

- 即时媒体：X/Twitter、小红书
  - 使用「反直觉洞察 + 情绪锚点」
  - 输出短图文、thread、钩子和排版结构
- 深度媒体：Newsletter、公众号、博客
  - 使用「方法论框架 + 底层逻辑」
  - 关联 Obsidian 里的过往案例，扩写成长逻辑文章
- 动态媒体：短视频、长视频、播客
  - 使用「黄金 3 秒开头 - 痛点展开 - 核心干预 - 证据案例 - 行动呼吁」

## What It Does

- 清洗音视频转录稿、网页长文、社媒图文里的噪音
- 用四维矩阵提取内容原子
- 在 Obsidian 中为新知识寻找历史笔记连接
- 从新旧笔记碰撞里生成选题种子
- 用 COPE 策略把一个观点重组为多平台内容草稿
- 提供可复制到 Obsidian 的 Markdown 模板
- 提供一个可选脚手架脚本，用于初始化内容飞轮目录

## Who It Is For

- 高频更新内容账号的创作者
- 使用 Obsidian 管理知识库的人
- 想把收藏夹、转录稿、长文和社媒内容转成选题库的人
- 想让 AI 参与「输入处理」而不只是「代写初稿」的人
- 希望一个观点可以稳定分发到 X/Twitter、小红书、公众号、Newsletter、短视频或播客的人

## Repository Structure

```text
obsidian-content-flywheel-skill/
├── SKILL.md
├── README.md
├── templates/
├── references/
├── scripts/
├── examples/
└── evals/
```

## Skill Trigger

The skill is designed to trigger when the user asks to:

- end bookmark hoarding
- process saved links or transcripts
- create an Obsidian content workflow
- connect new notes to an Obsidian vault
- extract content ideas from long materials
- repurpose one insight across multiple platforms
- generate X/Twitter, Xiaohongshu, newsletter, WeChat, short-video, or podcast drafts from the same source

## Install

Copy this folder into your Codex or Claude skills directory.

For Codex local skills, a common target is:

```bash
cp -R obsidian-content-flywheel-skill ~/.codex/skills/
```

For a project-local skill repository, upload this folder directly to GitHub and point your agent to `SKILL.md`.

## Example Prompts

```text
用 obsidian-content-flywheel 处理这段播客转录稿，输出知识矩阵和小红书草稿。
```

```text
把这个文件夹里的收藏链接做成选题种子库，并和我的 Obsidian 笔记建立双链建议。
```

```text
基于这篇长文生成 COPE 输出：推特 thread、小红书图文、公众号长文结构、短视频脚本。
```

```text
帮我把 Obsidian 里的 AI 内容管理系统升级成“收藏夹不吃灰”的内容飞轮。
```

## Templates

The `templates/` directory includes:

- `source-note.md`: cleaned source note
- `knowledge-matrix.md`: four-dimensional knowledge extraction
- `topic-seed.md`: publishable topic seed
- `cope-draft.md`: multi-platform draft structure

## Optional Vault Scaffolding

To create a starter Obsidian folder structure:

```bash
python scripts/scaffold_vault.py /path/to/vault
```

The script only creates missing folders and missing template files. It does not delete or rewrite existing notes.

Default folders:

```text
00_Workflow/
01_Inbox/
02_Knowledge_Atoms/
03_Topic_Seeds/
04_COPE_Drafts/
99_Templates/
```

## Design Philosophy

In a world where everyone has access to large language models, pure information arbitrage is getting weaker. A creator's stronger moat is curation: the ability to connect fragments, extract mechanisms, judge what matters, and present the right idea in the right format.

This skill is built around that belief. It does not try to replace the creator. It tries to remove the low-value labor between consumption and creation.

## License

MIT.
