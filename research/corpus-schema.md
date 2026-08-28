# Corpus Schema V2

## Design principle

Schema 优先记录可观察事实。历史来源事实、视觉观察和后续推断必须分开。不得用一个扁平的 `shot_type` 同时表达景别、朝向和裁切。

## Source fields

| Field | Required | Definition |
| --- | --- | --- |
| `record_id` | yes | 稳定 ID，例如 `AP-PIL-CAR-01` 或 `AP-EXP-FND-01` |
| `title` | yes | 权威来源显示的作品标题 |
| `work_date` | yes | 原始日期文本；无法确认时填 `unknown` |
| `source_institution` | yes | Foundation、博物馆或机构名称 |
| `source_url` | yes | 优先直接作品页 |
| `accession_id` | no | 馆藏或目录编号 |
| `source_series` | no | 只填写可证实的正式系列名 |
| `analysis_subset` | yes | `formal_portrait_general` 或 `in_the_american_west` |
| `source_checked_on` | yes | `YYYY-MM-DD` |

## Eligibility fields

| Field | Values |
| --- | --- |
| `practice` | `portrait`, `fashion`, `reportage`, `advertising`, `unclear` |
| `subject_count` | 整数或 `unclear` |
| `controlled_background` | `yes`, `no`, `unclear` |
| `environment_visible` | `none`, `minor`, `dominant`, `unclear` |
| `v1_candidate` | `true`, `review`, `false` |
| `exclusion_reason` | 空值或明确原因 |
| `image_structure` | `single_frame`, `diptych`, `triptych`, `other_composite`, `unclear` |

V1 route 只使用 `single_frame`。同一人物重复出现在双联或三联作品中，仍然不是单人单帧输入的直接证据。

## Structural axes

### `framing_scale`

- `face_detail`：画框切入脸部本身，至少一个主要五官区域或一侧脸明确出框；不能只因为头发、头顶或颈部被裁就使用此值。
- `tight_head`：脸部主导，主要五官仍完整可见；允许头发、头顶、耳缘、下巴外缘或颈部接近或越过画框。
- `head_and_shoulders`：完整或近完整头部与肩部，胸部以下不出现。
- `bust`：头部至胸廓附近。
- `waist_up`：头部至腰部附近。
- `three_quarter_body`：下缘位于大腿至小腿之间。
- `full_body`：头部至双脚整体进入画面。
- `unclear`：来源图不足以可靠判断。

### `head_view`

- `frontal`
- `three_quarter_facing_image_left`
- `three_quarter_facing_image_right`
- `profile_facing_image_left`
- `profile_facing_image_right`
- `back`
- `over_shoulder`
- `unclear`

### Head attitude

| Field | Values |
| --- | --- |
| `head_tilt` | `level`, `toward_image_left`, `toward_image_right`, `not_assessable`, `unclear` |
| `chin_angle` | `neutral`, `raised`, `lowered`, `not_assessable`, `unclear` |

`head_view` 记录水平旋转；`head_tilt` 记录左右倾斜；`chin_angle` 记录抬头或低头。三者不得混写。

### `torso_view`

- `frontal`
- `three_quarter_facing_image_left`
- `three_quarter_facing_image_right`
- `profile_facing_image_left`
- `profile_facing_image_right`
- `back`
- `not_visible`
- `unclear`

### `face_visibility`

- `full`
- `partial`
- `none`
- `occluded`
- `unclear`

### `crop_pattern`

- `none`
- `face_fragment_image_left_edge`
- `face_fragment_image_right_edge`
- `top_of_head`
- `chin_or_jaw`
- `hand_or_arm`
- `leg_or_foot`
- `multiple`
- `other`
- `unclear`

## Expression and gaze

| Field | Values |
| --- | --- |
| `gaze_direction` | `camera`, `image_left`, `image_right`, `up`, `down`, `eyes_closed`, `not_visible`, `unclear` |
| `mouth_state` | `closed_neutral`, `lips_parted`, `closed_smile`, `open_smile_teeth`, `open_expression`, `not_visible`, `unclear` |
| `expression_intensity` | `low`, `medium`, `high`, `not_assessable`, `unclear` |

`expression_intensity` 只记录面部肌肉变化的可见幅度，不解释人物的心理或人格。

## Hands, posture, and body

| Field | Values |
| --- | --- |
| `hands_visibility` | `none`, `one`, `both`, `partial`, `unclear` |
| `hand_relation` | `not_applicable`, `resting`, `touching_face`, `touching_body`, `holding_clothing`, `clasped`, `gripping_object`, `gesturing`, `multiple`, `unclear` |
| `shoulder_state` | `level`, `one_raised`, `both_raised`, `slumped`, `not_visible`, `unclear` |
| `torso_rotation` | `none`, `slight`, `strong`, `not_visible`, `unclear` |
| `posture_openness` | `open`, `closed`, `mixed`, `not_assessable`, `unclear` |
| `weight_distribution` | `centered`, `image_left`, `image_right`, `seated`, `not_assessable`, `unclear` |
| `pose_motion` | `still`, `gesture_in_progress`, `dynamic`, `not_assessable`, `unclear` |

不要直接标注主观的 `body_tension`。后续只能从这些可观察字段推导。

## Composition and background

| Field | Values |
| --- | --- |
| `image_orientation` | `portrait`, `square`, `landscape`, `unclear` |
| `subject_placement` | `centered`, `image_left`, `image_right`, `dynamic`, `unclear` |
| `negative_space_bias` | `balanced`, `top`, `bottom`, `image_left`, `image_right`, `multiple`, `minimal`, `unclear` |
| `background_tone` | `white`, `light_gray`, `mid_gray`, `dark`, `other`, `unclear` |
| `seamless_background` | `yes`, `no`, `unclear` |
| `backdrop_edge_visible` | `yes`, `no`, `unclear` |
| `black_border_visible` | `yes`, `no`, `unclear` |
| `face_frame_height_ratio` | 可选，0–1 估计值 |
| `figure_frame_height_ratio` | 可选，0–1 估计值 |

## Light and tone

| Field | Values |
| --- | --- |
| `tonality` | `black_and_white`, `color`, `unclear` |
| `key_direction` | `frontal`, `image_left`, `image_right`, `top`, `mixed`, `unclear` |
| `shadow_hardness` | `soft`, `medium`, `hard`, `unclear` |
| `facial_shadow_pattern` | `minimal`, `one_side`, `under_features`, `mixed`, `not_assessable`, `unclear` |
| `overall_contrast` | `low`, `medium`, `high`, `unclear` |
| `highlight_clipping_visible` | `yes`, `no`, `unclear` |
| `deep_black_area` | `none`, `small`, `medium`, `large`, `unclear` |

## Annotation control

| Field | Definition |
| --- | --- |
| `observed_notes` | 只写可见事实，不解释意义 |
| `annotation_confidence` | `high`, `medium`, `low` |
| `needs_review` | `true` 或 `false` |
| `review_reason` | 需要复核的具体原因 |
| `annotator` | 标注者或 agent 名称 |
| `annotated_on` | `YYYY-MM-DD` |

## Derived fields

`method_period` 从作品年份与来源史料推导；当前分析把 1969 年开始使用 8×10 Deardorff 视图相机作为成熟方法的分界线，标为 `pre_mature_before_1969` 或 `mature_1969_onward`，日期不足时为 `unclear`。它不是视觉观察字段。

`route_key`、`route_status`、`body_tension` 和 Style DNA 结论也不是原始观察。只有完成试标和统计后才能生成，并且必须可追溯到 `record_id`。
