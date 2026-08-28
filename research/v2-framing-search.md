# Focused Framing Search: Face Fragment, Frontal Close, Full Body

检索日期：2026-08-28。此轮按用户要求只补三类：严格半张脸、正面近肖像、完整全身；背影不在本轮范围内。所有判断来自实际打开的艺术家基金会或博物馆官方作品图。项目只保存 URL、元数据和结构化观察，不保存照片文件。

## Hard definitions

- `face_detail`：画面边缘必须切入脸部本身，使眼、鼻、嘴中的一个主要区域或一侧脸明确出框。只裁头顶、头发、耳缘、下巴、颈肩，或被手、眼镜遮挡，都不算半张脸。
- frontal close target：`formal_portrait_general|tight_head|frontal|full|none`。
- `full_body`：从头到双脚完整进入画面；站立但小腿或脚未入画仍是 `three_quarter_body`。

## Result ledger

| Target | Newly annotated | Exact route-eligible total | Mature-period exact total | Status |
| --- | ---: | ---: | ---: | --- |
| strict face fragment | 0 | 0 | 0 | `unsupported` |
| frontal tight head, full face, no crop | 5 | 7 | 2 | `provisional` |
| full body with both feet visible | 0 | 0 | 0 | `unsupported` |

正面近肖像虽达到 7 条精确结构记录，但 5 条来自 1960–1968，只有 `AP-EXP-MUS-17` 与 `AP-EXP-MUS-18` 属于 1969 年后的成熟方法期。七条记录的背景和光线也并不完全一致：白色背景占多数，但 `AP-EXP-FND-05` 为深色硬侧光，`AP-EXP-MUS-05` 为中灰背景并有双手动作。因此数量门槛已到，稳定的成熟期操作语言门槛尚未通过，保持 `provisional`。

## Newly annotated frontal-close evidence

| Record | Work | Official source | Structural observation |
| --- | --- | --- | --- |
| `AP-EXP-MUS-17` | Oscar Levant, 1972 | [Met](https://www.metmuseum.org/art/collection/search/284305) | 单人单帧；紧头部；正面；完整脸；无结构裁切；白背景 |
| `AP-EXP-MUS-18` | Jean Renoir, 1972 | [Met](https://www.metmuseum.org/art/collection/search/284306) | 单人单帧；紧头部；正面；完整脸；无结构裁切；目光偏画面右侧 |
| `AP-EXP-GET-01` | Henry Miller, 1968 | [Getty](https://www.getty.edu/art/collection/object/108GRD) | 单人单帧；紧头部；正面；完整脸；无结构裁切；目光偏画面左侧 |
| `AP-EXP-GET-02` | Walter Hickock, 1960 | [Getty](https://www.getty.edu/art/collection/object/108GRJ) | 单人单帧；紧头部；正面；完整脸；无结构裁切；直视镜头 |
| `AP-EXP-GET-03` | Dick Hickock, 1960 | [Getty](https://www.getty.edu/art/collection/object/108GRH) | 单人单帧；紧头部；正面；完整脸；无结构裁切；与现有腰上肖像是不同画面结构 |

精确键的另外两条既有记录为 `AP-EXP-FND-05` 与 `AP-EXP-MUS-05`。

## Strict face-fragment audit

合格记录为 0。以下实际看图样本均为容易误标的反例：

- [Marian Anderson, Met](https://www.metmuseum.org/art/collection/search/270362)：头顶裁切，但眼、鼻、嘴仍完整；`tight_head`。
- Chet Baker、Dorothy Parker、Linus Pauling，[Avedon Foundation](https://www.avedonfoundation.org/the-work)：脸很大或头部贴近画框，但主要五官完整；不是 `face_detail`。
- [Isak Dinesen, MoMA](https://www.moma.org/collection/works/44355)：帽子/头顶裁切，脸部仍完整。
- [Marcel Duchamp, MoMA](https://www.moma.org/collection/works/128616) 与 [John Ford, MoMA](https://www.moma.org/collection/works/128635)：手或眼罩造成遮挡，不是画框切掉脸部结构。
- [William Burroughs, Nelson-Atkins](https://art.nelson-atkins.org/objects/47646/william-burroughs-writer-new-york-city)：画面边缘裁到身体/肩部，脸完整。

因此半张脸输入仍必须保持半张脸。它没有精确同构 route，运行时使用 `treatment_only`：可以更换背景、重做黑白影调和对比，但不得补全成整脸，也不得借用紧头部构图来露出隐藏五官。

## Full-body audit

合格记录为 0。

- Amon Carter 的 `In the American West` 官方对象页定向核验了 91 个单人记录，其中 88 个作品图成功加载；站立肖像仍在腰、大腿、膝部或小腿处结束，没有双脚完整入画。代表性反例：[Jesse Kleinsasser](https://www.cartermuseum.org/collection/jesse-kleinsasser-pig-man-hutterite-colony-harlowton-montana-62383-p19852890)、[Richard Garber](https://www.cartermuseum.org/collection/richard-garber-drifter-interstate-15-provo-utah-82080-p198528110)、[Rick Davis](https://www.cartermuseum.org/collection/rick-davis-drifter-interstate-94-buffalo-north-dakota-71382-p198528113)。
- Avedon Foundation 官方作品页定向核验了 108 张已加载作品图；出现双脚的图像属于 fashion、reportage、环境或复杂道具语境，不能支持 V1 正式肖像路线。
- [Dovima with Elephants, Whitney](https://whitney.org/collection/works/12709) 虽为全身，但属于 fashion、环境和复杂道具场景。
- [Rudolph Nureyev, NPG](https://npg.si.edu/object/npg_NPG.91.54) 为全身动态舞蹈背/侧面，不是本项目的正式受控背景路线。
- [Lew Alcindor, MoMA](https://www.moma.org/collection/works/128622) 为户外环境和动态语境。

完整全身作为精确 route 仍保持 `unsupported`。产品运行时允许向内裁切：general 正面完整脸优先裁到同属 general 的三分之四身并使用 `treatment_only`；只有用户明确选择 IAW 时才使用 `IAW-3Q-FRONT-FULL-LEG`。侧身和背影保持原方向后裁到三分之四身并使用 `treatment_only`，不得旋转或创造未见人脸。
