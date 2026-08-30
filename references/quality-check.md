# Runtime Quality Check

Review the source and generated result side by side before delivery. Do not judge the result in isolation.

## Comparison order

1. Confirm that the image tool actually received the source image and performed an edit rather than text-only generation.
2. Compare head view, face visibility, expression, pose, hands, clothing, accessories, and objects against the source.
3. Compare the result with the declared composition diagnosis: intentional asymmetry preserved, or accidental imbalance actually repaired with the named crop or background-only extension.
4. Check tonal separation in background, skin, eyes, lips, hair, hands, and clothing. Inspect face, hair, hands, clothing edges, and background at high detail for artifacts.
5. Check route or fallback treatment only after protected structure and composition pass.

## Hard failures

- framing scale changed outside the safe inward-crop matrix
- the diagnosis marked accidental imbalance, but the result remains visibly crowded, lopsided, or dominated by purposeless headroom
- purposeful gaze, gesture, edge tension, or meaningful negative space was centered away without evidence
- crop or recentering grazed hair, chin, fingers, clothing, or cut directly through a major joint
- background extension added or reconstructed sitter pixels instead of featureless background only
- head or torso orientation changed
- gaze direction or eyelid state changed to force camera contact
- partial face was completed into view
- back view was turned into a visible face
- single person became multiple people
- identity-defining visible features changed materially
- clothing, accessories, or social identity were replaced by corpus-specific subject styling
- background or props moved the result outside the supported formal-portrait domain
- an exact route was claimed for an unsupported or provisional evidence class
- a fallback copied route-specific pose or social styling instead of the transferable treatment core
- the result is a newly guessed sitter or lookalike rather than an edit of the supplied source
- facial asymmetry, age cues, skin texture, hairline, eye spacing, nose, mouth, jaw, or profile silhouette drifted materially
- visible hands, fingers, limbs, clothing, accessories, or held objects were removed, duplicated, replaced, or rebuilt outside the declared crop
- beauty retouch, waxy skin, de-aging, face reshaping, or forced symmetry replaced descriptive texture
- IAW-specific grime, cowboy styling, period clothing, tools, insects, scars, occupation, or social narrative was introduced
- halos, backdrop seams, duplicate features, anatomical damage, posterized skin, crushed facial blacks, added text, or watermark remain
- skin, eyes, hair, hands, or clothing lost identity-bearing detail through highlight clipping or blocked shadows
- pale hair, skin, or clothing merged into the background, or separation was faked with an outline or hard rim-light halo
- low-resolution, blurred, compressed, or occluded source detail was replaced with invented eyes, teeth, pores, jewelry, or fabric

## Scored dimensions

Score each from 0 to 4:

- `structure_preservation`
- `composition_integrity`
- `transformation_integrity`
- `visible_identity_preservation`
- `route_fidelity`
- `shared_style_fidelity`
- `tonal_integrity`
- `technical_integrity`
- `source_conditioning_integrity`

Do not score facial identity when it is not assessable. `composition_integrity=4` means the output follows the declared intent and action with clean boundaries: purposeful asymmetry remains purposeful, or accidental imbalance is visibly corrected. `tonal_integrity=4` means the background reads continuous and the sitter retains distinct, unclipped face, hair, skin, hand, and clothing tones. For `crop_fallback`, structure preservation means the declared target crop is correct and every protected axis remains unchanged. `source_conditioning_integrity=4` requires that the output remains recognizably derived from the supplied image, not merely similar to its description. A result cannot pass if `structure_preservation < 4`, `composition_integrity < 4`, `transformation_integrity < 4`, `source_conditioning_integrity < 4`, or any hard failure is present.

## Correction limit

If a result fails, make one targeted correction from the original source that names the failed dimension and visible defect. Never use the failed output as the sole identity source. Stop after the second total generation unless the user requests additional attempts.
