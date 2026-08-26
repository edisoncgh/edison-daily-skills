# Edison Daily Skills

## Content

这个repo用来保存一些我自己日常vibe-coding经常使用的优质skills。

- **Project Continuity Suite**（自制整合包）：`project-continue` + `project-memory` + `handoff-driven-development` + `neat-freak` 四个 skill 组成的跨 Agent/Session 连续性套件。`project-continue` 是用户面协调器（closeout / resume / checkpoint / status 四种模式），`project-memory` 管历史记忆（HISTORY），`handoff-driven-development` 管当前状态（CURRENT STATE），`neat-freak` 管收尾审计（AUDIT）。neat-freak 为卡兹克上游 MIT 快照，见其 `UPSTREAM.md`。

- **Matt Pocock 系列 skill**（mp- 前缀）：From [mattpocock/skills](https://github.com/mattpocock/skills)。节选了一部分日常 vibe coding 常用的 skill，为了避免重名添加了 mp 前缀。已同步上游最新版（含上游改名：review→code-review、diagnose→diagnosing-bugs、to-prd→to-spec、write-a-skill→writing-for-agents；zoom-out 上游已移除）。当前收录：
  - mp-tdd（Test-driven development）
  - mp-diagnose（bug 诊断闭环）
  - mp-review（Standards + Spec 双轴代码审查）
  - mp-grill-me / mp-grill-with-docs（方案压力测试）
  - mp-handoff（会话交接文档）
  - mp-improve-codebase-architecture（架构深化机会挖掘）
  - mp-setup-matt-pocock-skills（issue tracker / 领域文档初始化）
  - mp-to-prd（对话→规格文档→issue tracker）

- **design-taste-frontend**：From [lazylizardai/skill-design-taste-frontend](https://github.com/lazylizardai/skill-design-taste-frontend)（Lovable 开源）。资深 UI/UX 工程师视角的前端设计 skill：设计方差、动效强度、视觉密度主动配置，严格组件架构与 CSS 硬件加速规则。

- **frontend-design**：From [Ilm-Alan/frontend-design](https://github.com/Ilm-Alan/frontend-design)。八种美学锚点的前端设计 skill，每个锚点把 palette / typography / structure / texture 锁定到具体 CSS tokens，按 brief 选取，杜绝默认风格。

- **Darwin-skill**：花叔开源的 skill，用于优化其他 skill。

## Use

```bash
npx skills add edisoncgh/edison-daily-skills
```