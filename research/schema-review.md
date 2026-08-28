# Pilot Schema Review

## Result

20 条 pilot 已完成：10 条 `formal_portrait_general`，10 条 `in_the_american_west`。全部是单人、单帧、受控背景作品。试标验证了拆分景别、头部朝向、躯干朝向、脸部可见度和裁切类别的必要性，但也暴露出五个缺口。

## Changes made

### 1. Separate face detail from a tight head

`AP-PIL-FND-01` 初标为 `face_detail`。复核发现完整五官仍在画面中，只有头部边缘非常接近画框，因此改为 `tight_head`。V2 只有在画框切入脸部本身时才使用 `face_detail`。

### 2. Record head attitude independently

`AP-PIL-FND-02` 的头部向后仰，但旧 schema 只能把它塞进 `head_view=frontal`。V2 新增 `head_tilt` 和 `chin_angle`，避免把水平转向、左右倾斜和抬头低头混成一个字段。

### 3. Record the visible black print border

全部 10 条 Carter pilot 以及 `AP-PIL-MUS-01`、`AP-PIL-MUS-03`、`AP-PIL-MUS-04` 的来源图可见黑色印框。旧 schema 只能把这件事写在 notes 中。V2 新增 `black_border_visible`。

### 4. Exclude multi-panel works from route evidence

稀有构图搜索找到双联和三联作品，但它们不等价于用户上传的一张单帧照片。V2 新增 `image_structure`，Corpus V1 route 只使用 `single_frame`。

### 5. Distinguish a still pose from dynamic movement

背面搜索只找到动态舞蹈姿态的 Rudolph Nureyev。它既不满足 V1 的脸部清晰要求，也不能直接支持正式静态背影 route。V2 新增 `pose_motion`。

## Re-annotation checks

- `AP-PIL-FND-01`: framing changed from `face_detail` to `tight_head`.
- `AP-PIL-FND-02`: `chin_angle=raised` added.
- `AP-PIL-FND-05`: hand relation downgraded to `unclear`; available authoritative previews do not support a stable object-holding claim.
- `AP-PIL-CAR-01`: upper-thigh lower edge remains `three_quarter_body` under the clarified boundary; it is not `waist_up`.

## Coverage gaps exposed by the pilot

- no strict lateral half-face fragment;
- no `face_visibility=partial` or `none`;
- no full-body record;
- no strict profile, over-shoulder, or back-view record;
- 17 of 20 heads are frontal;
- 19 of 20 subjects are centered;
- all 10 `In the American West` records are frontal and white-background.

The pilot therefore validates the schema but cannot by itself support every product route. Expansion must be stratified toward these gaps. No rare route is promoted merely because a neighboring crop exists.
