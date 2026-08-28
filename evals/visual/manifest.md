# Synthetic Visual Evaluation Manifest

All images in this directory depict fictional AI-generated adults created solely to test the Skill's runtime behavior. They are not photographs of real users or public figures and are not Richard Avedon works, derivatives, thumbnails, screenshots, or corpus evidence.

## Source fixtures

| File | Case | Protected features |
| --- | --- | --- |
| `source-frontal-full-body.png` | general and IAW full-body crop fallback | frontal face, glasses, cardigan, ring, both hands, full stance |
| `source-profile-waist.png` | profile treatment-only | strict left-facing silhouette, hair, hoop earring, red top |
| `source-face-fragment.png` | partial-face treatment-only | same missing left facial region, visible eye/nose/mouth/beard geometry |
| `source-general-waist.png` | general and IAW waist-up exact routes | glasses, braid, jacket, both lapel-holding hands, parted lips |

Generated outputs and their scored observations are recorded in `visual-results.md`. None of these fixtures may be cited as Avedon evidence or used to promote a corpus route.

## Result fixtures

| File | Run | Purpose |
| --- | --- | --- |
| `result-ve-01-general-fullbody.png` | `VE-01` | least-loss general thigh crop |
| `result-ve-02-profile.png` | `VE-02` | profile orientation preservation |
| `result-ve-03-face-fragment.png` | `VE-03` | partial-face preservation |
| `result-ve-04-general-waist.png` | `VE-04` | exact general waist-up route |
| `result-ve-05-iaw-waist.png` | `VE-05` | exact IAW waist-up route without social restyling |
| `result-ve-06-iaw-fullbody-corrected.png` | `VE-06` | IAW full-body to mid-thigh crop fallback after one source-based correction |
