# Corpus V1 Scope

## Authoritative basis

- The Metropolitan Museum of Art describes Avedon's mature portrait method as using a bright white seamless background without props or extraneous details, concentrating attention on face, gaze, dress, and gesture: <https://www.metmuseum.org/exhibitions/listings/2002/richard-avedon>
- Amon Carter Museum states that `In the American West` used a seamless white backdrop to remove references to place and focus on the individual: <https://www.cartermuseum.org/carter-collection/collection-group/american-west>
- The Richard Avedon Foundation describes his career as spanning portrait, reportage, and fashion practices: <https://www.avedonfoundation.org/the-work>

These sources support the research boundary but do not make every listed work eligible. The Met exhibition includes group portraits, and `In the American West` also contains multi-person records. `subject_count = 1` is therefore an explicit product rule applied per work, not an assumed property of an entire series.

## Product rule

Skill 优先寻找输入的同构证据；没有精确 route 时，可以安全向内裁切到最近的支持结构，或保持现有脸部方向并只迁移背景、黑白影调、对比和质感。

构图允许收缩，不允许向外发明。Skill 可以调整人物占比、留白、下缘裁切、背景、光线和影调；必须保持人物朝向、脸部可见度、可见五官、表情类别和身份。背影或半张脸只有在另有同一人物身份参考时才能露出原图没有显示的脸部结构。

## Corpus inclusion

- `subject_count = 1`
- 正式肖像实践
- 受控、白色或极简背景
- 人物结构足以分类，即使只显示局部脸部或背面
- 面部细节、近景、头肩、胸像、半身、3/4 身和全身均可
- 正面、3/4 侧面、侧面、回望和背面均可作为候选，但必须由作品证据决定是否支持
- 名人和普通人均可
- 成熟肖像实践优先
- `In the American West` 作为独立分析子集

## Corpus exclusion

- Fashion editorial
- Reportage、街头摄影和明显环境肖像
- 双人和群像
- 双联、三联或其他多画面组合，即使每个画面都是同一人物
- 产品广告主导画面
- 复杂道具或复杂叙事场景
- 来源无法核验的转载图

## Input boundary

用户输入不必具有白色背景，也不必按 Skill 的标准预先拍摄。只要是单人、单帧，并且能可靠判断人物结构，就可以处理。精确 route、裁切 fallback 和 treatment-only fallback 的选择见 `supported-routes.md` 与 `transformation-fallbacks.md`。

## Unsupported behavior

当输入结构没有可靠 route 时，先尝试最小安全向内裁切；仍无法进入支持路线时，保持脸部方向和可见身份，只迁移摄影处理。普通交付不向用户解释内部证据等级。不得自动补全脸部、旋转未见人脸或扩大画面来生成缺失身体。
