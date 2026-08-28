# Avedon Portrait Skill

一个以作品证据为基础、保留人物身份的单人人像转换 Skill。

它先识别输入结构，再选择删除身份信息最少的安全目标：有精确证据时使用完整路线；安全目标恰好命中支持路线时使用 crop fallback；否则保留脸部方向和可见身份，只迁移受控背景、黑白影调、对比和质感。不会为了获得 supported 标签而多裁一刀。

用户不需要为了迎合 Skill 专门上传标准正脸。Skill 可以自动裁切、重新居中、删除背景并调整光影，但不会补出输入中看不见的脸，也不会把背影、侧脸或局部脸擅自变成正脸。运行时必须把用户照片作为图像编辑的权威输入，不能退化成文字生成一个相似的人。

## 安装入口

仓库根目录就是可安装的 Skill：`SKILL.md` 是入口，`agents/` 提供界面信息，`references/` 保存生成时按需读取的规则。

`research/`、`evals/` 和 `scripts/` 是独立证据层，仅用于审计、测试和后续改进，不会自动进入普通生成上下文。

## Corpus V1

- 权威候选：216 条
- 实际看图并完成 55 字段标注：85 条
- 可进入路线统计的低争议记录：70 条
- 已支持的精确路线：3 条
- 已完成 6 条合成源图的真图回归验收，最终全部通过；其中 1 条错误裁切按正式纠错流程从原始输入重做后通过
- `In the American West` 与一般正式肖像分开统计

Corpus V1 只纳入单人、受控或极简背景的正式肖像。排除 fashion editorial、reportage、街拍、环境肖像、群像、产品主导广告和复杂道具场景。

仓库不保存或分发 Richard Avedon 的照片，只保存权威来源网址、元数据、结构化观察和由此推导的规则。

## 结构

```text
SKILL.md                  运行入口
agents/openai.yaml        界面与默认调用信息
references/               生成时按需读取的规则
research/                 corpus、schema、来源与研究记录
evals/                    行为测试、合成源图和视觉验收记录
scripts/                  corpus 分析与验证工具
```

完整研究统计见 `research/corpus-findings.md`，正式标注见 `research/annotated-corpus.csv`，真图回归记录见 `evals/visual/visual-results.md`。
