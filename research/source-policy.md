# Source and Copyright Policy

## Source priority

按以下顺序收集：

1. Richard Avedon Foundation
2. 收藏该作品的博物馆或公共机构作品页
3. 博物馆展览、研究档案或正式馆藏目录
4. 其他可审计的学术或出版来源，仅用于补充

不使用 Pinterest、无署名博客、社交媒体转载、图片聚合站或无法确认作品信息的页面作为 corpus 事实源。

## What the repository stores

- 作品标题
- 创作日期
- 权威来源机构
- 作品详情 URL
- 馆藏编号或目录编号（若有）
- 正式系列名（若有）
- 结构化视觉观察
- 标注置信度和复核状态
- `evals/visual/` 下明确标注为 AI 合成、仅用于回归测试的非 Avedon 输入与输出夹具

## What the repository never stores

- Avedon 原始照片文件
- 网页缩略图缓存
- 截图或裁切副本
- 去除水印后的版本
- 未经授权的训练素材包

URL 只用于人工查看和审计，不代表仓库取得图片再分发权。

合成视觉夹具必须有 manifest，记录生成用途、非真实人物声明和对应测试用例；不得混入 `research/`、`references/` 或 Avedon corpus。

## Pool and pilot

- 候选参考池目标：不少于 80 条权威记录。
- schema 试标：从候选池分层选择 20 条。
- 试标必须覆盖不同景别、人物朝向、脸部可见度、裁切方式、手部状态和两个分析子集。
- 候选池中的未标注作品不能用来支持 Style DNA 结论。

## Expanded corpus

- 试标通过后，扩展到至少 80 条实际查看作品图并完成结构标注的记录。
- `formal_portrait_general` 和 `in_the_american_west` 各至少 30 条；其余名额按结构覆盖缺口分配。
- 半脸、侧面、回头、背影等稀有类型必须定向搜索，找不到时记录负面结果，不用常规正面肖像补数。
- 同一作品被多个机构收录时，只计算一次视觉证据，其他页面只作为来源交叉验证。
- 标注为 `needs_review=true` 的记录可以保留在 corpus 中，但不能单独决定 route 规则。

三个数字必须分开报告：候选记录数、已看图标注数、可用于 route 统计的低争议记录数。
