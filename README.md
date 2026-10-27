# Agent Skills

一组面向中文内容生产与浏览器自动化的 Agent Skill，遵循 [Agent Skills](https://code.claude.com/docs/en/skills) 规范：每个技能是一个目录，入口为 `SKILL.md`。

## 技能列表

| 技能 | 用途 | 依赖 |
|---|---|---|
| [geo-article-production](skills/geo-article-production/) | 从选题资料到可发布文章包：证据整理、SEO/GEO 关键词、平台版本、去 AI 味润色、封面与配图、发布证据准备 | 可选：aigeo 后台、Remotion |
| [github-project-intro](skills/github-project-intro/) | 把一个 GitHub 仓库做成完整介绍视频：来源核验、内容策划、证据采集、分镜、渲染、配音、封面 | Remotion、Easy WebBridge（可选） |
| [douyin-download-webbridge](skills/douyin-download-webbridge/) | 下载抖音视频、图文与音轨，复用已授权的浏览器会话，不需要第三方 API Key | Easy WebBridge |
| [fiction-crafter-cn](skills/fiction-crafter-cn/) | 中文长篇小说创作工作台：作品目录、人物卡、世界观、卷纲、章节与连续性检查 | 无 |

## 使用方式

把需要的技能目录复制到你的 Agent 技能目录即可：

```bash
# Claude Code
cp -r skills/geo-article-production ~/.claude/skills/

# Codex
cp -r skills/geo-article-production ~/.codex/skills/
```

Agent 会根据 `SKILL.md` 里的 `name` 和 `description` 自动决定何时加载。

## 约定

- 每个 `SKILL.md` 只写"什么时候用、怎么判断、怎么产出"，细节放 `references/`
- 脚本放 `scripts/`，可执行、可单独测试
- 不在技能里写死本机绝对路径

## License

MIT
