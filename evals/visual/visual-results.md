# Visual Evaluation Results

Run status: complete. Each result was visually compared side by side with its synthetic source fixture on 2026-08-28.

Score order: `structure / transformation / identity / route / shared style / technical / source conditioning`, each on the 0–4 scale in `../rubric.md`.

| Run | Input | Mode and target | Result | Hard failures | Score | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `VE-01` | frontal full body | general `treatment_only`, thigh crop | `result-ve-01-general-fullbody.png` | none | `4/4/4/3/4/4/4` PASS | feet removed at upper-to-mid thigh; glasses, ring, both hands, clothes, frontal view, and pose retained |
| `VE-02` | profile waist | general `treatment_only`, profile retained | `result-ve-02-profile.png` | none | `4/4/4/3/4/4/4` PASS | strict left profile, hair, hoop earring, visible facial silhouette, and top retained; no frontalization |
| `VE-03` | face fragment | general `treatment_only`, fragment retained | `result-ve-03-face-fragment.png` | none | `4/4/4/3/4/4/4` PASS | the same left facial region remains outside the frame; no face completion |
| `VE-04` | frontal waist | `GEN-WAIST-FRONT-FULL-NONE` exact | `result-ve-04-general-waist.png` | none | `4/4/4/4/4/4/4` PASS | framing, glasses, braid, earrings, parted lips, jacket, blouse, and both lapel hands retained; broad frontal soft treatment |
| `VE-05` | frontal waist | `IAW-WAIST-FRONT-FULL-NONE` exact | `result-ve-05-iaw-waist.png` | none | `4/4/4/4/4/4/4` PASS | identity and clothing retained with no worker, cowboy, period, dust, or prop styling; lighting kept broad because confidence is medium |
| `VE-06` | frontal full body | `IAW-3Q-FRONT-FULL-LEG` crop fallback | `result-ve-06-iaw-fullbody-corrected.png` | none in final | `4/4/4/4/4/4/4` PASS | first attempt stopped below the knees and failed structure; one corrective edit restarted from the original source and placed the edge at mid-thigh while retaining both hands and clothing |

## Evidence limits

These runs prove that the written execution contract can drive the available editor through the six declared behaviors. They do not prove real-user identity robustness across ages, skin textures, low-resolution inputs, occlusion, or different image-editing backends. Synthetic fixtures cannot promote an unsupported route or raise corpus confidence.
