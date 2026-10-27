# 中文小说工匠

一个轻量的长篇小说文件工作台：人物、世界观、卷纲、时间线和章节各自落盘，方便你和不同 Agent 接力创作。离线可用，不需要 API Key。

## 能做什么

- 建立人物、世界观、卷纲、时间线和章节目录。
- 检查人物关系、事件顺序和伏笔的连续性。
- 用可读文件支持多人或多 Agent 接力创作。

## 使用

```bash
python3 scripts/self_test.py init --output ./我的作品 --title "雾中车站"
python3 scripts/self_test.py check --input examples/success-project
```

先整理事实，再写章节；发现冲突会指出位置，不会静默改掉原文。
