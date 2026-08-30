# Edison Daily Skills

## Content

这个repo用来保存一些我自己日常vibe-coding经常使用的优质skills。

- **Project Continuity Suite**（自制整合包）：`project-continue` + `project-memory` + `handoff-driven-development` + `neat-freak` 四个 skill 组成的跨 Agent/Session 连续性套件。`project-continue` 是用户面协调器（closeout / resume / checkpoint / status 四种模式），`project-memory` 管历史记忆（HISTORY），`handoff-driven-development` 管当前状态（CURRENT STATE），`neat-freak` 管收尾审计（AUDIT）。neat-freak 为卡兹克上游 MIT 快照，见其 `UPSTREAM.md`。

- **Matt Pocock 系列 skill**（mp- 前缀）：From [mattpocock/skills](https://github.com/mattpocock/skills)。节选了一部分日常 vibe coding 常用的 skill，为了避免重名添加了 mp 前缀；**目录名与上游母仓库保持一致**（即 `mp-` + 上游目录名，如上游 `code-review` → 本仓库 `mp-code-review`）。已同步上游最新版（zoom-out 上游已移除，故未收录）。当前收录 16 个：

  - 工程开发流：`mp-tdd`、`mp-diagnosing-bugs`、`mp-code-review`（双轴审查）
  - 方案打磨流：`mp-grilling`（拷问引擎）、`mp-grill-me`（无状态拷问）、`mp-grill-with-docs`（拷问+文档沉淀）、`mp-to-questionnaire`（问卷挖信息）
  - 架构与建模：`mp-improve-codebase-architecture`、`mp-domain-modeling`（领域术语治理）、`mp-setup-matt-pocock-skills`（issue tracker 初始化）
  - 知识与交接：`mp-handoff`（会话交接）、`mp-to-spec`（对话→规格）、`mp-research`（后台调研）、`mp-teach`（跨 session 教学）、`mp-wait-what`（听不懂重说）、`mp-writing-for-agents`（为 agent 写文档/技能）

- **design-taste-frontend**：From [lazylizardai/skill-design-taste-frontend](https://github.com/lazylizardai/skill-design-taste-frontend)（Lovable 开源）。资深 UI/UX 工程师视角的前端设计 skill：设计方差、动效强度、视觉密度主动配置，严格组件架构与 CSS 硬件加速规则。

- **frontend-design**：From [Ilm-Alan/frontend-design](https://github.com/Ilm-Alan/frontend-design)。八种美学锚点的前端设计 skill，每个锚点把 palette / typography / structure / texture 锁定到具体 CSS tokens，按 brief 选取，杜绝默认风格。

- **Darwin-skill**：花叔开源的 skill，用于优化其他 skill。

## Use

```bash
npx skills add edisoncgh/edison-daily-skills
```