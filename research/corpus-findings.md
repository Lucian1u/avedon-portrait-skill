# Corpus Findings

统计日期：2026-08-28。所有数字都来自 `reference-pool.csv` 与 `annotated-corpus.csv`，不包含照片文件。

## Evidence ledger

| Evidence stage | Count | Meaning |
| --- | ---: | --- |
| authoritative candidates | 216 | 权威来源目录；未看图的候选不能支持风格结论 |
| pilot annotations | 20 | 用于修订 schema 的分层试标 |
| visually reviewed annotations | 85 | 实际打开权威来源图像并完成 55 字段标注 |
| V1 scope-eligible | 83 | `v1_candidate=true` 且为单帧 |
| route-eligible | 70 | 另加 `needs_review=false`，可进入路线统计 |

85 条正式标注由 43 条 `formal_portrait_general` 和 42 条 `in_the_american_west` 构成。需要复核的记录仍留在 corpus 中，但不能决定路线。

## Promotion rule

V1 采用保守门槛：一个**精确结构键**只有在至少 6 条 route-eligible 记录中重复出现，且背景、构图、影调和人物关系足以写成可验收规则时，才标记为 `supported`。2–5 条为 `provisional`；0–1 条或只有范围外证据为 `unsupported`。

精确结构键为：

```text
analysis_subset|framing_scale|head_view|face_visibility|crop_pattern
```

这个计数门槛只是必要条件，不是充分条件。来源重复、双联画、时装语境、低清无法判断和 `needs_review=true` 均不能用于凑数。

## Promoted exact routes

### General waist-up, frontal, full face, no structural crop

- route-eligible count: 15
- supporting records: `AP-PIL-MUS-03`, `AP-PIL-MUS-04`, `AP-EXP-FND-04`, `AP-EXP-FND-08`, `AP-EXP-FND-10`, `AP-EXP-FND-12`, `AP-EXP-FND-15`, `AP-EXP-FND-17`, `AP-EXP-MUS-01`, `AP-EXP-MUS-03`, `AP-EXP-MUS-04`, `AP-EXP-MUS-07`, `AP-EXP-MUS-08`, `AP-EXP-MUS-09`, `AP-EXP-MUS-10`
- status: `supported`

### In the American West waist-up, frontal, full face, no structural crop

- route-eligible count: 7
- supporting records: `AP-PIL-CAR-03`, `AP-PIL-CAR-06`, `AP-PIL-CAR-07`, `AP-PIL-CAR-10`, `AP-EXP-CAR-07`, `AP-EXP-CAR-14`, `AP-EXP-CAR-32`
- status: `supported`

### In the American West three-quarter body, frontal, full face, leg/foot crop

- route-eligible count: 12
- supporting records: `AP-EXP-CAR-01`, `AP-EXP-CAR-02`, `AP-EXP-CAR-06`, `AP-EXP-CAR-11`, `AP-EXP-CAR-12`, `AP-EXP-CAR-13`, `AP-EXP-CAR-16`, `AP-EXP-CAR-17`, `AP-EXP-CAR-20`, `AP-EXP-CAR-23`, `AP-EXP-CAR-27`, `AP-EXP-CAR-28`
- status: `supported`

## Important non-promotions

- IAW three-quarter body + frontal + full + no crop has 5 route-eligible records (`AP-PIL-CAR-01`, `AP-PIL-CAR-02`, `AP-PIL-CAR-04`, `AP-PIL-CAR-05`, `AP-PIL-CAR-09`): `provisional`.
- IAW bust + frontal + full + no crop has 4 (`AP-EXP-CAR-08`, `AP-EXP-CAR-22`, `AP-EXP-CAR-26`, `AP-EXP-CAR-29`): `provisional`.
- General bust + frontal + full + no crop has 2 (`AP-EXP-FND-02`, `AP-EXP-MUS-06`): `provisional`.
- General tight head + frontal + full + no crop has 7 (`AP-EXP-FND-05`, `AP-EXP-MUS-05`, `AP-EXP-MUS-17`, `AP-EXP-MUS-18`, `AP-EXP-GET-01`, `AP-EXP-GET-02`, `AP-EXP-GET-03`): `provisional`. 数量门槛已达到，但只有 2 条属于 1969 年后的成熟方法期，且背景与光线存在明显时期差异，尚不能写成稳定的成熟期操作规则。
- No route-eligible record supports `face_detail`, `full_body`, `back`, or `over_shoulder`: `unsupported`.
- The corpus contains one strict-profile annotation (`AP-EXP-FND-18`), but it is `v1_candidate=review` and `needs_review=true`; the route-eligible strict-profile count is 0. Additional institutional leads remain unpromoted: `unsupported` in V1 runtime.

The absence of a promoted route remains an evidence result. Runtime may still use an identity-safe inward crop or treatment-only fallback, but it must not relabel that fallback as an exact corpus route.

半张脸、正面近肖像与完整全身的补充检索和严格反例见 `v2-framing-search.md`。
