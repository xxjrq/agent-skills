---
name: geo-article-production
description: 从选题资料到可发布文章包的中文自媒体生产 Skill。用于证据整理、SEO/GEO 关键词与引用、平台版本、去 AI 味润色、字数规则、头像/图标资产、Remotion 封面与插图、ImageGen 概念画面、封面上传复核和发布证据准备；默认停在最终发布前，不自动点击发布。
license: MIT
metadata:
  author: xxjrq
  version: "0.1.3"
  related_skills: "aigeo-project, cn-humanizer, geo-cover-design, geo-title-optimizer, skill-seo, easy-upload, easy-webbridge"
---

# GEO 文章生产

## 我的100个开源项目：每日生产与发布交接（2026-10-14）

该用户最新要求每天生产5篇QA合格新主稿，投稿由其他负责人使用既有geo-publication工作流完成。生产执行者只写稿、做官方Logo封面、同步当前用户writing.articles并回读、生成production-handoff-YYYYMMDD.json/Markdown；不打开平台编辑器、不存平台草稿、不提交或预约、不创建自动投稿任务。主稿与独立平台稿由Luna（gpt-6-luna）生成，负责人通读并绑定正文哈希验收；修订和平台稿不重复计数。4:3横图、3:4竖图及176/320缩略图沿用当前系列合同。

交接每项包含项目/版本、正文和平台稿哈希、源稿ID、主稿/平台稿/来源/Logo/封面/QA路径、publication_hold和未核验原生字段，状态ready_for_publisher。后台失败独立记backend_pending；编辑/资产未通过不进入合格计数。发布负责人按同一源稿ID和版本接收并填写publisher_received_at，平台状态和证据独立回写；ready_for_publisher不能算submitted或published。具体可执行流程复用aigeo的docs/content/geo-articles-100/CONTENT-OPERATIONS-CURRENT.md；不另建重复Skill。

把一条用户需求整理成有来源、可检查、适配各平台的文章包。这个 Skill 负责生产与发布前检查，不替平台做最终发布决定，也不把“检测分数”当成文章质量证明。

## 工具路由

- `selfmedia-github-research`：需要核验 GitHub 项目身份、README 事实、版本或动态数据时使用，保留来源 URL 和核验时间。
- `skill-seo`：检查文章主题、标题、关键词、描述和引用结构是否可发现；不承诺搜索排名、GEO 结果或流量。
- `geo-title-optimizer`：生成问题型/结果型/场景型标题候选、评分和独立平台标题；不负责发布，也不虚构平台规则。
- `cn-humanizer` 或 `humanizer-zh`：识别并改写官腔、翻译腔、套话、节奏过度工整和 AI 高频词。润色后人工通读，不能伪造“AI 检测通过率”。
- `geo-cover-design`：项目级封面合同；负责内容类型、平台比例、主标题居中、安全区、真实图标、多款构图、Remotion 渲染和上传回读。它不是抖音专用 Skill。
- `imagegen` / `selfmedia-imagegen`：只有画面确实需要概念插画、场景或背景时使用。生成图不承担准确中文排版，文字必须在生成后用 Remotion/CSS 等确定性方式叠加。
- `easy-upload`：只用于离线文章包、字段和素材准备；平台发布仍按当前授权的 Easy WebBridge 流程执行。
- `aigeo-project/references/content-compliance.md`：平台内容、版权、隐私、广告声明和敏感表述的合规规则；它是项目参考文档，不是独立发布执行器。
- `easy-webbridge`：需要读取已登录平台、上传封面或回读草稿/公开状态时使用明确的在线 `browserId`。遇到登录、验证码或安全验证立即暂停。

### 多风格封面合同

- 默认使用 Remotion，遵守 geo-cover-design 的当前合同：日常运营按主题制作一张16:9主封面，其他比例仅按目标平台实测要求准备。探索新风格或用户要求比较时，才制作适合该主题的不同候选，不固定每篇三款。
- 按主题、官方图标、视觉焦点、缩略图可读性和平台裁切选主款，禁止随机或伪随机抽主款。保存源文件、选择理由、尺寸和哈希。seed只用于可复现纹理或装饰。
- 默认候选风格可包括 `workbuddy-github`、`editorial-coral`、`terminal-lime`、`poster-amber`；内容类型、主钩子、项目名和动态数字必须来自已核验资料，不能套用榜单的 Star、排名或热度事实。
- 每个平台独立上传对应比例封面；上传前记录文件哈希，上传后重新打开编辑器回读封面状态。未回读不能记为已上传，未上传不能发布。
- ImageGen 只用于概念背景或材质探索，不能承担准确中文、项目 Logo、产品界面或动态数据；确定性文字必须由 Remotion 后置排版。

## 输入与输出

输入至少包括：需求原文、目标受众、目标平台/账号、事实来源或待核验问题。缺少平台、账号、来源或版权边界时先列缺项，不凭空补齐。

输出一个版本化内容单元，例如：

```text
article/
  brief.md                 # 需求、受众、主张和禁用项
  sources.md               # 来源 URL、摘录、核验时间和风险
  article.md               # 主稿与 frontmatter
  variants/                # 各平台标题、正文和标签
  assets/
    icon-avatar-manifest.json
    cover-remotion.png
    illustrations/
  qa.json                  # 字数、链接、合规、视觉检查结果
  title-brief.md           # 标题实体、意图、痛点和选题边界
  title-candidates.json    # 标题候选、评分和选中理由
  platform-titles.md       # 平台独立标题、预算、来源和长度
  title-qa.json             # 标题与正文/封面映射及门禁
  publish-evidence/        # 每个平台独立的草稿/公开回读证据
```

## 生产流程

每篇交付前执行 [文章包验收合同](references/article-package-contract.md)，先校验来源、主稿/变体哈希、两图、真实缩略图和执行证据，再同步原稿ID并回读。离线通过与原生发布通过分别记录；不得让 `budget_unknown`、未选择的话题或未上传素材冒充平台门禁通过。用户要求“先写两篇看看”时，以样稿复核覆盖常规日产/投稿流程，保留已有稿件并暂停新增投稿，不自动恢复；不自动点击最终发布。

1. **需求与选题**：把需求拆成目标、受众、一个核心问题和明确不做事项，形成 `brief.md`。
2. **资料与 GEO/SEO**：核验事实和引用；关键词只保留与正文真正相关的词。每条高风险事实都带来源和时间，未知内容标记为待确认。
3. **标题与主稿**：先调用 `geo-title-optimizer`，生成候选、评分和平台独立标题；主稿标题与平台标题分开保存，再写一份事实一致的主稿。标题、摘要、正文、标签和图片说明分别检查。
4. **去 AI 味复核**：运行 `cn-humanizer` 或 `humanizer-zh` 的规则进行人工改写；保留作者判断和事实，不为了“像人”添加未经来源支持的故事。
5. **字数与平台规则**：每个平台使用独立配置 `platform-budgets.md` 或任务输入中的预算。已知值必须注明来源和采集日期；未知或页面动态变化时标记 `budget_unknown` 并停止提交，不套用其他平台的字数。
6. **图标与头像资产**：从官方站点、应用商店、项目仓库或已登记素材库获取，记录来源、许可和哈希；头像/图标用于身份或品牌识别，不自动当作文章封面。
7. **封面与插图**：默认 Remotion，先锁定尺寸、安全区和准确文字，再渲染并视觉检查。需要概念背景时可用 ImageGen，随后用 Remotion 叠加标题、项目名和数字。按实际平台裁切检查同一主封面，确有不同尺寸要求时独立排版，不能硬裁或拉伸。
8. **上传准备**：为每个平台准备独立封面和正文图；在平台编辑器实际上传，检查裁切预览，保存后重开确认封面仍存在。只看到本地文件不算上传完成。
9. **平台字段与排版**：提交前逐平台填写并回读标题、摘要、分类、标签、正文排版、来源/原创声明、可见范围、账号和定时字段；没有该字段时记为 `not_applicable`。小红书的标题、正文、标签和图片说明必须通过外部 URL 门禁；来源 URL 只留在 sources/frontmatter，发现 `http(s)://`、`www.` 或常见域名 URL 时记录 `platform-policy`/`needs_user_action`，不得提交。移除 frontmatter，确认段落、列表、代码块、链接、图片顺序、图片说明和移动端宽度都符合当前编辑器表现。
10. **发布证据**：每个平台、每个账号单独记录草稿、审核中、已公开、未知和失败。公开 URL、管理页状态、标题/账号匹配和关键截图组成证据；提交返回 URL 或 `submitted_unknown` 不等于已公开。
11. **最终边界**：合规检查默认自动通过，不默认等待人工确认；用户明确要求复核或命中高风险条件时才进入人工复核。真实发布仍需用户明确授权的 Easy WebBridge 任务，并在安全验证处交还给用户。

合规检查的“自动”指按来源和当前限制自主执行检查，不表示未检查就通过。发布前读取源稿及运营台账的 `publication_hold`；命中违规/限制内容时停该内容及其跨平台变体，恢复条件由geo-publication维护，不能因日产目标或日期切换解除。

## 持续自主运营

用户明确授权系列持续发布时，生产完成后衔接geo-publication与easy-webbridge，不因本Skill负责离线生产而重复要求日常审批。数量、每日额度与候选队列读取项目运营合同；写作、图片、平台排版、真实话题和公开核验按篇留证。当前项目流程见 `<aigeo-project>/docs/content/geo-articles-100/DAILY-WORKFLOW.md`。

## 文章校验基线

`<aigeo-project>/docs/content/geo-articles-10/batch_02/validate.py` 的 1200–2500 汉字、至少 3 个三级标题、合规说明和待人工确认段，是 batch_02 的示例合同，不是通用平台上限。运行时必须声明采用哪份平台配置，并将动态页面提示视为更高优先级。

## 已知限制

- 不保证 SEO/GEO 排名、平台审核、曝光、转化或“去 AI 检测”结果。
- 不绕过登录、验证码、风控、版权限制或账号安全验证。
- 不把 ImageGen 生成的错字当作可发布文字；准确文字必须后置确定性排版并人工检查。
- 平台规则、字数、封面尺寸和编辑器字段会变化；读不到当前页面要求时输出 `budget_unknown`/`needs_user_action`，不猜测。
- 文章包可由 `easy-upload` 做离线准备，但最终发布与公开状态必须由平台页面回读证明。

## 自检

```bash
python3 - <<'PY'
from pathlib import Path
p = Path('SKILL.md')
s = p.read_text(encoding='utf-8')
required = ['geo-article-production', 'Remotion', 'ImageGen', 'budget_unknown', 'submitted_unknown', '不自动点击最终发布']
missing = [x for x in required if x not in s]
raise SystemExit(f'missing: {missing}' if missing else 'PASS')
PY
```
