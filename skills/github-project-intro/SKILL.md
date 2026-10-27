---
name: github-project-intro
description: 将一个 GitHub 仓库从工作台入库、官方来源与高风险声明核验、抖音内容策划、真实网页证据采集、脚本与 Timeline、Remotion 渲染、配音、两尺寸封面到五文件发布包完成闭环。用户要求介绍 GitHub 单仓库、复制现有 GitHub 视频任务、录屏或批量生产 GitHub 项目视频时使用。
---

# GitHub 单仓库视频编排

本 Skill 是 GitHub 单仓库视频的唯一编排入口。每个仓库独立拥有事实、策划、脚本、录屏、Timeline、音频、封面数据和发布包；只复用公共组件。旧作品和示例只能参考，不能作为事实、Schema 或视觉硬标准。

## 1. 读取顺序与职责

先读取仓库 `AGENTS.md` 规定的文档，再按阶段完整读取并执行：

1. `work-library-api-registration`：工作台入库或复制任务字段。
2. `~/.codex/skills/selfmedia-github-research/SKILL.md`：官方来源与高风险声明。
3. `~/.codex/skills/douyin-tech-content-planner/SKILL.md`：受众、唯一收益、钩子和证据顺序。
4. `~/.codex/skills/record-web-demo/SKILL.md`：证据清单、Action Plan和真实录屏。
5. `~/.codex/skills/selfmedia-script-storyboard/SKILL.md`：先确定最终口播和可读分镜，不预估最终音频时长。
6. 本 Skill 的音频规则：串行生成并实测音频，先得到真实时长和字幕时间。
7. `~/.codex/skills/selfmedia-script-storyboard/SKILL.md`：使用录屏动作时间与实测音频完成 Timeline v1.2。
8. `~/.codex/skills/selfmedia-cover-design/SKILL.md`：3:4 与 4:3 两尺寸封面。
9. `~/.codex/skills/selfmedia-remotion-render/SKILL.md`：公共模板渲染。
10. 本 Skill 的流程门禁：核对阶段顺序、必需产物和工作台状态；五文件机器合同通过后直接原子生成正式发布包。

内容 Agent 只能修改自己的内容单元。`apps/studio/src/root.tsx`、公共模板、公共封面、Schema、Preflight 和发布校验器只能由主集成 Agent 修改。多个 Agent 不得同时修改共享文件。

## 2. 入库与正式内容单元

1. 用户提交正式选题后，必须先完成工作台入库：新内容调用 `POST /api/production-requests`，已有目录调用 `POST /api/works` 后再调用 `POST /api/production-requests/adopt`。两种方式都必须返回有效 `work_id` 和生产请求 ID；没有这两个 ID 不得研究、录屏或渲染。
2. 入库成功后，才在 `projects/github/videos/<content-id>/` 建立或接管独立内容单元，并同步 `projects/index.yaml` 与 `projects/task-index.yaml`。`content.yaml`、`task.yaml` 和 `制作单.md` 必须落盘同一个 `work_id`；工作台流程界面第一阶段固定显示“工作台入库”。
3. 工作台只保存任务需求；复制模板时清空旧仓库 URL、Star、版本、许可证、脚本、Timeline、录屏、来源、封面数据和发布包。
4. `renderer.composition_id` 固定为 `GitHubProjectDemoTemplate`。模板 ID 由工作台/API 返回，不手写依赖某条历史作品的模板 ID。
5. 用户提交正式任务即允许工作台按八阶段连续执行到 `release_ready`。只有用户明确要求测试并指定停点时才设置 `stopAfterStageId`；`planning` 只交制作单，`render` 只留渲染暂存，不生成正式目录。
   工作台连续执行时复用同一个 Codex session，保留阶段门禁但不为每个阶段重新建立上下文。
5. 正式内容单元必须存在：
   - `project.json`
   - `content.yaml`
   - `task.yaml`
   - `research/facts.json`
   - `制作单.md`
6. Pipeline research 输出在临时工作区时，必须将官方来源、当前使用的动态字段和高风险声明结论写回正式内容单元；不得拿临时目录代替正式项目。

GitHub 单项目视频只维护一个人工主文档 `制作单.md`，使用 `decision`、`voiceover`、`storyboard`、`assets`、`release` 五个固定标记区块。新任务不创建 `research/decision.md`、`research/content-plan.md`、`script/voiceover.md`、`script/script.json`、`创作提示词.md` 或 `qa/`；事实、Timeline、Action Plan、录屏清单、音频、SRT 和渲染 Props 继续使用独立机器文件。

## 3. 来源、风险与策划门禁

1. 使用 GitHub 仓库页确认项目身份并保存官方 URL。只为本片实际出现的高风险声明访问 README、官方文档或发布页，不做全功能百科式核验。
2. 高风险声明包括：动态数字和排名；价格、成本、节省比例和性能对比；安全、隐私、法律结论；许可证、版本、维护状态和官方身份；绝对承诺；以及没有真实画面或官方来源支撑的具体结果。
3. Star、版本、许可证等字段只有在画面或文案使用时才核验；使用时在正式渲染前刷新。`facts.json` 保存精确值、来源和风险结论；没有额外高风险声明时记录空清单即可。
4. 普通痛点、疑问句、情绪、类比、轻度幽默和真实演示的口语化总结不做逐句核验。用户给出或认可的钩子默认锁定，只有明确事实错误、法律合规风险或严重误导时才能否决；其他风险只做最小词级修改。
5. 一条视频只承诺一个核心收益。先确定受众、人话钩子、前12秒兑现和唯一CTA，再写脚本。事实文件不得向口播注入 README 技术措辞；只有真正影响能否使用的硬门槛才随对应功能自然说明，禁止单独制作风险提示页、待核验页、免责声明墙或适用边界页。
6. 公开成品不展示完整网址、二维码、下载按钮、站外动作指令或普通工具的具体货币金额。
7. 项目身份无法确认，或公开文案仍包含未解决的高风险声明时停止；没有高风险声明不得阻塞录屏和渲染。

## 4. 真实证据与素材时间

必须先执行 `record-web-demo`：

1. 使用800×600逻辑视口采集README、图片/GIF、候选截图和选择器。
2. 先制定 GitHub 仓库身份镜头：真实仓库名使用细圆角框，Star或版本使用细椭圆圈；该镜头必须排在所有README或外部Demo之前。
3. 再选择1～3个能证明核心收益的README或官方Demo证据；文件列表、安装日志、Logo和许可证不能默认充当结果证据。
4. GitHub身份与外部Demo使用独立Action Plan和录屏文件；各自验证通过后再录屏。需要1600×1200编码源时使用 `--pixel-scale 2` 后处理，不扩大网页布局。
5. 录屏清单必须记录每个实际动作的 `startMs`、`endMs`、页面、操作、证据对象和执行结果。
6. 录屏脚本必须成功完成，清单中的动作必须有实际 `startMs`、`endMs` 和完成状态；失败动作不得进入 Timeline。
7. Timeline的 `trimStartMs` 和 `trimEndMs` 只能来自录屏清单，禁止把成片场景时间当成素材入点。

## 5. 脚本与 Timeline

时长按信息、实测口播和画面阅读时间决定，不固定为25秒。默认叙事参考：

```text
0～3秒    GitHub仓库页、项目名、Star和核心价值
3～6秒    README结果或官方Demo的第一个真实证据
前12秒    出现最强真实证据
中段      继续演示1～2个证据
后段      适用场景、门槛或限制
结尾      一句总结和一个自然CTA
```

先把最终口播和可读分镜写入 `制作单.md` 的 `voiceover` 与 `storyboard` 区块。音频阶段完成后，使用实测音频时长、字幕时间和录屏清单生成唯一机器导演文件 `timeline.json`。Timeline：

- 使用 `packages/timeline-schema/timeline.schema.json`，版本为 `1.2`；
- Scene `role` 只允许 `hook`、`proof`、`process`、`result`、`identity`、`cta`；
- `direction.proofByMs <= 12000`；
- `direction.demoLayoutPreset` 固定为 `fixed-demo-v1`；演示外框固定 `x=86, y=420, width=908, height=681`；
- 最多一个 `visualPeak: true`；
- `focus` 使用从已验证源帧得出的归一化坐标；
- 演示场景不得设置 `identityTop`、`evidenceTop`、`captionTop`；强调只允许发生在演示框内部；
- 录屏已有标注时不得在Remotion重复标注；
- 场景、字幕和音频覆盖完整时间，无重叠、越界和无效留白。

标题、封面、首屏、口播、字幕和发布文案必须出现 `GitHub` 与项目名，并保持项目身份、数字和其他高风险事实一致。三个平台标题分别不超过30个Unicode字符。三个平台的 `话题/标签` 行必须各含 `#github优质项目 #github开源`，总数 5～7 个且不重复，并补充项目标签和至少两个匹配本条内容的价值/场景标签；实时热门标签最多补 2 个且只能在有当次平台证据时添加。

## 6. 公共 Remotion 架构

新仓库只使用公共Composition：

- `GitHubProjectDemoTemplate`
- `GitHubProjectCoverPortrait`
- `GitHubProjectCoverLandscape`

`GitHubProjectCoverFeed` 仅作历史兼容，不进入新项目的Composition清单、渲染任务或发布包。

项目通过结构化输入传入 Timeline、项目名、Star、钩子、结果、预设和素材。禁止：

- 新建仓库专用TSX视觉系统；
- 在Root注册仓库专用视频或封面Composition；
- 把OpenMontage或任何历史项目硬编码成公共模板默认事实；
- 在渲染阶段改事实、猜素材时间或重排场景。

`GitHubProjectDemoTemplate` 是模板ID，不是项目ID。Studio固定使用 `http://localhost:3000/`，通过输入属性选择项目数据。普通TSX、CSS、JSON和素材改动依靠热更新；只有依赖、配置、入口变化、服务无响应或不可恢复编译错误才允许重启并记录原因。CLI正式渲染不依赖Studio端口。

正式渲染前执行一次统一Preflight：正式文件完整、公开内容使用的动态字段和高风险声明有效、Action Plan与录屏通过、素材时间合法、Timeline Schema通过、标题长度通过、音频模式一致、封面数据完整。任一失败立即停止。

## 7. 音频模式

只服从工作台、`content.yaml` 和 `task.yaml` 一致的 `voice.mode`：

- `generate-and-mix`：串行生成Edge-TTS并合入发布视频；最终必须为AAC 48kHz立体声，平均音量约-20～-28dB。
- `generate-reference`：生成参考音频但不合入；发布视频必须真正无音轨。
- `self-recorded`：不生成TTS；发布视频必须真正无音轨，SRT保留待用户配音后微调。

模式缺失或三处不一致时Preflight失败。音频阶段必须位于 Timeline 阶段之前；文案变化后重新生成并实测音频，不得复用旧时长。Timeline 与 SRT 必须使用本次实测时长，音频或 SRT 超过 Timeline 时长时不得进入渲染。

## 8. 封面与正式渲染

封面必须执行 `selfmedia-cover-design`，不能在视频完成后临时拼一张。视频固定生成两张独立排版封面：3:4、4:3；不得硬裁视频帧，不生成9:16视频流封面。

GitHub系列固定信息顺序：GitHub栏目身份、项目名、项目名下方的金色Star、一个6～12字具体结果。封面数据必须来自本项目，并分别生成3:4与4:3两个文件。

全部项目通过Preflight后，只Bundle一次，再按已批准策划批量渲染视频和封面。不得为同一版本反复预览、逐场景抽帧和重渲染，也不得创建 QA 图片目录。

## 9. 媒体资产、封面与多平台发布

### 9.1 先区分四类图片产物

一个项目不能只登记一个“图片”字段。必须分别管理：

| 产物 | 用途 | 首选生成方式 | 是否使用 AI 生图 |
|---|---|---|---|
| 文章内配图 | 解释架构、流程、安装步骤、真实功能 | 官方截图、录屏抽帧、Remotion 静帧或 SVG；必要时再用 AI 做不承载事实的背景 | 默认不使用；事实画面不能用 AI 编造 |
| 文章封面 | CSDN、知乎、公众号等文章列表缩略图 | Remotion/HTML/CSS 叠加排版 | 可用 AI 生成无文字背景，但标题、项目名、Star、数字必须后叠 |
| 视频封面 | 抖音/B站视频或图文入口封面 | `selfmedia-cover-design` + 公共 Remotion Composition，独立生成 3:4 与 4:3 | 可用 AI 生成视觉主体，但不能硬裁视频帧代替封面 |
| Skill 图标 | SkillHub 探索页、Skill 包元数据 | 复用项目图标或 selfmedia-imagegen 生成无文字图标，再裁切/导出 512px | 可用；图标内不要放小字和不可读英文 |

结论：**文章封面和视频封面不是把视频第一帧截出来；文章内配图也不是每张都调用生图。** 真实截图负责证据，Remotion 负责稳定排版，AI 生图只负责没有事实风险的视觉背景或图标。

### 9.2 图片资产的生成顺序

每个项目按下面顺序准备资产，禁止先做封面再补事实：

```text
官方来源与事实核验
  → 真实截图/录屏/README证据
  → 文章结构与视频 storyboard
  → 确定需要哪些配图
  → 生成或整理图片资产
  → Remotion 统一叠加项目名、标题、数字和品牌排版
  → 生成文章封面、3:4视频封面、4:3视频封面
  → 尺寸/安全区/事实一致性检查
```

图片来源选择：

1. **真实产品画面**：GitHub、官方 Demo、官方文档、实际运行页面，直接截图或从录屏抽帧。
2. **解释型图示**：优先用 Remotion、SVG、HTML/CSS 生成，适合架构图、流程图、对比表和安装步骤。
3. **氛围背景**：使用 `selfmedia-imagegen` 生成，不放未经核验的 Logo、Star、版本号、价格和功能承诺。
4. **文章封面标题**：必须在 Remotion/HTML/CSS 中叠加，不依赖 AI 在像素内生成中文文字。

### 9.3 封面字段与排版规则

每个项目的封面数据必须单独保存，至少包括：

```yaml
cover:
  eyebrow: "GitHub 开源项目"
  project_name: "<项目名>"
  hook: "<6～12字具体结果>"
  star_text: "<真实 Star，带核验日期>"
  focal_asset: "<真实截图或无事实风险的背景图路径>"
  palette: "<本项目选定色板>"
  source_checked_at: "<YYYY-MM-DD>"
  outputs:
    portrait: "02-竖封面-3比4.png"
    landscape: "03-横封面-4比3.png"
```

GitHub 系列固定信息顺序：栏目身份 → 项目名 → 金色 Star → 一个具体结果。封面主标题只表达一个收益，不把“100 个项目”、完整功能列表或安装命令塞进封面。

- 3:4：`1080×1440`，上边界约 `115px`，下边界约 `216px`，左右各 `86px`。
- 4:3：独立重排，不拉伸、不硬裁 3:4 封面。
- 9:16 视频画面：`1080×1920`，核心内容遵守顶部 `170px`、底部 `288px`、左右 `86px` 的项目安全区；这不是视频封面尺寸。
- 标题、项目名、Star、版本和其他精确数字均使用确定性排版；AI 图像中不生成精确文字。

### 9.4 文章图片与 Remotion 的分工

文章发布前按文章类型选择：

| 文章内容 | 推荐资产 | 说明 |
|---|---|---|
| 项目介绍 | 1 张项目封面 + 1 张真实 GitHub 截图 + 1 张核心能力图 | 核心能力图用 SVG/Remotion，不用 AI 假装产品截图 |
| 安装教程 | 命令截图、终端截图、流程图 | 命令和路径必须来自真实项目 |
| 架构拆解 | SVG/Remotion 架构图 + 官方 README 截图 | 结构可视化，事实来源仍指向官方仓库 |
| 对比评测 | Remotion/HTML 表格 + 各项目官方链接 | 只比较已核验字段 |
| 纯观点文章 | 封面 + 少量氛围图 | 氛围图可 AI 生成，但不能用来证明产品功能 |

### 9.5 发布平台分层

发布不是所有平台都发同一份原文，按“代码源、技能分发、文章搜索、视频分发”分层：

| 层级 | 平台 | 主要任务 | 发布内容 |
|---|---|---|---|
| 代码主源 | GitHub | 权威事实、版本、Issue、Star | 源码、README、CHANGELOG、License、Release |
| 国内代码镜像 | Gitee | 国内访问、镜像入口、备用下载 | 与 GitHub 同步的源码和 README，明确 GitHub 为主源 |
| Skill 分发 | SkillHub | Skill 搜索、安装、版本管理 | 合法 Skill 包、manifest、中文描述、图标、版本变更 |
| 文章搜索 | CSDN、知乎、掘金、今日头条、公众号 | 长文搜索、解释和导流 | 平台适配后的文章、封面、真实截图、官方链接 |
| 视频/图文分发 | Bilibili、抖音 | 发现、演示、关注和导流 | 视频、专栏/图文、3:4 或平台要求的入口图 |
| 可选扩散 | 少数派、SegmentFault、开源中国、博客园 | 技术读者和开发者社区 | 只在内容确实适配时发布，不为凑数量重复灌水 |

100 个项目的最低发布组合建议是：

```text
GitHub 主源 + Gitee 镜像
  → 有 Skill 的项目再上 SkillHub
  → CSDN / 知乎 / 公众号选择适合平台的文章版本
  → Bilibili / 抖音发布演示视频或图文
```

SkillHub 不是所有 GitHub 项目都能发布。只有真正具备可执行 Skill 包结构、`SKILL.md`/`manifest.yaml`、触发词和自测说明的项目才上架；普通工具仓库只发布 GitHub、Gitee 和文章/视频内容。

### 9.6 发布前的平台适配

每个平台都生成独立的 `release` 字段，不允许把一篇 Markdown 原样复制到所有平台：

```yaml
release:
  github:
    repo_url: ""
    release_url: ""
    status: "pending"
  gitee:
    mirror_url: ""
    sync_checked_at: ""
    status: "pending"
  skillhub:
    skill_slug: ""
    package_path: ""
    icon_path: ""
    status: "not_applicable"
  articles:
    csdn: { title: "", url: "", status: "pending" }
    zhihu: { title: "", url: "", status: "not_applicable" }
    wechat: { title: "", url: "", status: "not_applicable" }
  media:
    bilibili: { url: "", status: "pending" }
    douyin: { url: "", status: "pending" }
```

每个平台完成后必须回读标题、正文/README 关键段、项目链接、图片和公开状态；发布日志记录实际 URL、时间、版本、浏览器环境和验收结论。发布、发送、删除和覆盖旧稿仍然是人工确认动作。

## 10. Release Check

Agent 完成以下机器流程门禁后，把五文件写入 `renders/release-package/`。工作台校验通过后原子改名为 `发布成品/` 并直接进入 `release_ready`：

- 工作台生产请求已关联有效 `work_id`，且库记录目录与 `source_dir` 完全一致；否则停止，不进入来源与风险核验、录屏或渲染阶段；
- Pipeline `validate --require-assets`通过；
- Timeline Schema、素材时长、前12秒证据门禁通过；
- 渲染命令成功，视频输出为1080×1920、30fps、H.264；
- 音轨符合 `voice.mode`，TTS 和 SRT 末尾不超过视频时长；`generate-and-mix` 的最终平均音量必须在 -28～-20dB；
- 两张封面尺寸和命名正确；
- 三个平台各有实质不同的标题和描述，标题均不超过30个Unicode字符，描述保留真实段落；
- 三个平台标签均含 `#github优质项目 #github开源`，每行 5～7 个不重复标签，项目标签和价值/场景标签匹配当前内容；
- `projects/index.yaml`、`projects/task-index.yaml`、`task.yaml`、`content.yaml`状态一致。

不完整播放、不抽帧、不逐图查看、不做 OCR、联系表或 20:9 压力图，不生成 QA 图片和主观报告。最终画面由用户查看。

不再设置 `rendered → visual_reviewed` 人工确认阶段，也不复制重复候选包。任一机器合同失败时不得生成 `发布成品/` 或报告 `release_ready`。正式发布包必须且只能有五个文件：发布文案、视频、3:4封面、4:3封面、SRT。SRT固定命名为 `04-字幕.srt`；最终画面由用户在正式目录查看。

不自动上传，不操作平台账号，不采集发布后数据。
