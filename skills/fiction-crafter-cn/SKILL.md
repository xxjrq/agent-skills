---
name: fiction-crafter-cn
description: 中文长篇小说创作工作台：把灵感整理为作品目录，维护人物卡、世界观、卷纲、章节和连续性检查。适用于需要长期迭代、多人或多 Agent 协作的网文创作，不承诺爆款、收益或审核结果。
---

# 中文小说工匠

用可读、可 diff 的文件管理长篇作品状态，避免人物、时间线和伏笔在长对话中丢失。它负责组织和检查创作资料，章节正文仍由 Agent 根据用户要求撰写。

## 作品目录

新作品建议使用以下结构：

```text
作品名/
├── README.md
├── story-bible.md       # 一句话 premise、主题、基调与禁写项
├── world.md             # 世界观、规则、时间线
├── characters/
│   └── index.md         # 人物卡与关系
├── outline/
│   ├── volume-01.md     # 卷纲、章节目标、伏笔
│   └── timeline.md      # 事件顺序
├── chapters/
│   └── 001-title.md
└── continuity-report.md
```

## 工作流程

1. 收集题材、读者、篇幅、视角和不可写内容，形成 `story-bible.md`。
2. 建人物卡：目标、阻力、关系、变化弧和已确认事实；每次修改记录原因。
3. 先做世界规则与卷纲，再拆章节目标、冲突、转折、伏笔回收点。
4. 生成或修改章节时，只读取相关人物、时间线和上一章结尾，避免把无关资料塞进上下文。
5. 写入章节后运行连续性检查：人物状态、称谓、时间、地点、伏笔和章节编号。
6. 输出报告，列出通过项、冲突位置和需要人工决定的项；不自动覆盖已有正文。

## 输入与输出

输入可为灵感、已有目录、章节文本或修改要求。输出是目录文件和 `continuity-report.md/json`；每次写入前保留原文件，除非用户明确要求覆盖。

## 失败与边界

- 作品名、章节编号或目标不明确时返回 `needs_clarification`。
- 发现两个互相冲突的事实时标为 `conflict`，给出文件和行号，不擅自选一个。
- 不处理现实违法教程、仇恨煽动或未成年人性内容；可改为安全、虚构的成长冲突。
- 不保证平台签约、过审、销量或“爆款”。

## 命令

```bash
python3 scripts/self_test.py self-test
python3 scripts/self_test.py init --output /tmp/my-novel --title "雾中车站"
python3 scripts/self_test.py check --input examples/success-project
```

