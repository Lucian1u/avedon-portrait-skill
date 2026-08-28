# Corpus Coverage Plan

## Why the pool is not the corpus

候选池用于防止遗漏作品，完整标注 corpus 才用于提炼摄影语言。页面标题或机构描述不能替代对作品图的结构观察。

## Scale target

- candidate reference pool: at least 80 authoritative records;
- schema pilot: exactly 20 fully annotated records, split 10/10 between the two subsets;
- expanded annotated corpus: at least 80 unique works;
- each analysis subset: at least 30 low-review or reviewed records.

如果某一子集没有足够合格作品，不为达到数字而纳入 fashion、reportage、群像或环境肖像。缺口必须显式报告。

## Stratification axes

扩展抽样优先补齐以下交叉覆盖，而不是按名气挑照片：

- framing scale;
- head and torso view;
- face visibility and crop class;
- gaze and mouth state;
- hand visibility and relation;
- subject placement and negative space;
- background tone;
- light, contrast, and deep-black distribution;
- mature portrait period versus earlier eligible portraits;
- general formal portraits versus `In the American West`.

## Rare-route search

对 `face_fragment`、`profile`、`over_shoulder`、`back` 和 `full_body` 分别做权威来源定向搜索。每类都记录：

1. 搜索过的机构入口；
2. 找到并实际看图的合格作品；
3. 被排除作品及原因；
4. 最终证据是否足以支持 route。

## Promotion thresholds

一个结构 route 标记为 `supported` 至少需要：

- 6 条独立、合格、已看图记录；
- 至少 4 条为 `needs_review=false`；
- 能写出稳定的构图、裁切、背景、光线与人物处理规则；
- 每条规则列出 supporting 和 contradicting record IDs；
- 有一个能识别“结构被标准化”的 eval case。

2–5 条记录只可标记为 `provisional`。0–1 条或观察彼此冲突时标记为 `unsupported`。数量达到阈值但规律不稳定时仍不得升级。

## V1 completion

- authoritative candidates: 214;
- visually reviewed annotations: 85;
- `formal_portrait_general`: 43;
- `in_the_american_west`: 42;
- route-eligible low-review records: 70;
- promoted exact routes: 3.

最终覆盖与未晋级路线见 `corpus-findings.md`。半张脸、正面近肖像和完整全身的定向补充见 `v2-framing-search.md`；背影未在这次补充中继续扩展。数量目标已经完成；V1 不再用一般正面肖像填补稀有路线缺口。
