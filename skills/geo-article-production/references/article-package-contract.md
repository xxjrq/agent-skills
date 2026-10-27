# 文章包验收与中断恢复

适用于aimeGeo“我的100个开源项目”系列；每篇沿用同一目录、源稿ID和分发记录。分类取原计划，文章列表分类按用户要求显示“我的100个开源项目”，同时保留原 `series_category` 和具体 `series_theme`，不能丢掉分类主题。

## 交付顺序

1. 从原分类选题，核验公开第一方仓库、固定提交、版本和许可证；读实际脚本，区分工作说明、固定样例自测与真实程序能力。记录 `brief.md`、`sources.md`、`claim-source-map.json`。
2. 标题、正文和样例一起定稿；命令说明运行目录、输入文件如何准备，样例标明来自测试数据。确认脚本是否真会核验资料，不能把输入字段非空检查写成来源真实性核验。至少五个读者问题在 `question-map.json` 对应正文答案，不为凑结构堆空泛FAQ。
3. 执行仓库固定成功/资料不足样例与自测，保存 `sample-execution.json`。记录命令、输出、退出码、提交和核验范围，不把固定样例写成真实用户或设备实测。
4. 完成独立平台标题/变体；每份变体第一行与 `title-qa.json` 对应。原生预算未读取就 `budget_unknown`，话题未选就 `not_selected`，不提前写平台SHIP。
5. 使用Remotion + React + CSS，按现行系列要求保存1440×1080（4:3）横封面、官方Logo、176×132/320×240缩略图与TSX/CSS/输入数据/哈希；竖图为1080×1440（3:4）。实际尺寸看两档缩略图，主字默认在176宽对应至少约24px。离线渲染浏览器独立profile、关闭并清理，不能触发用户钥匙串。历史已验收16:9不批量重制。
6. `qa.json`分别记录内容/来源/视觉复核和未执行的平台检查。`delivery-manifest.json`指向证据文件，不重复复制来源说明。后台读取合并原payload，写入封面＋官方Logo共两图，按原ID重读正文哈希和图片数；修订不新增稿件计数。
7. 执行下面的文章包检查；缺文件、哈希过期、样例失败或视觉pending都停止样稿交付。结构通过仍不能替代人工通读和视觉判断。

```bash
node tools/geo-operations/check-article-package.mjs docs/content/geo-articles-100/<project>
```

脚本位于 `<aigeo-project>`。输出 `offlinePackageReady` 表示保存的离线文稿/资产证据通过，`backendReady`独立表示后台两图和正文已回读，`sampleReady`要求两者同时成立。`--offline`可独立检查文稿包，`--legacy-cover`仅用于历史16:9原包检查。新稿editorial_review须绑定当前正文SHA-256并实际通读，needs_revision或过期复核必须失败。后台未登记不抹去已经独立通过编辑/资产QA的写稿成果。`publicationAllowed`始终false；发布资格仍由geo-publication的实时原生门禁判断。

## 平台与暂停

平台仍须核对正确账号、违规hold、原生标题/全文/媒体/排版/真实话题/声明、额度与全平台小时间隔。只通过Easy WebBridge操作。提交意图和草稿ID先登记，最终按钮只点一次；未知结果只回读。

当前用户要求两篇样稿供其检查时，保存 `execution_mode=two_article_sample_review` 并停止新增生产及最终投稿，待其明确恢复。已有平台草稿保留，不把编辑器自动保存当成全文/封面/标签已重开核验。已有稿件数量如实保留，选出或修订两篇不另计新稿。

后台API发布任务的 `publish_mode` 是 `create` 或 `update`，不是 Skill 动作 `publish`；400拒绝发生在平台最终按钮前时，记“后台写入失败、最终提交0”，修正字段后先去重再决定恢复。写入或点击结果未知时不能自动重试。

2026-10-11样稿示例为商品尺码指南1630、设备适配核对1631；交付状态与文件见 `<aigeo-project>/docs/content/geo-articles-100/two-article-review-20261011.json`。
