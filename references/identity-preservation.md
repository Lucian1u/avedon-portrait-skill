# Identity Preservation

Identity preservation must be calibrated to the evidence visible in the input.

## Full or mostly visible face

Preserve:

- facial proportions and asymmetry
- eye spacing and visible eye shape
- nose and mouth geometry
- jaw and chin structure
- age cues, skin texture, hairline, and distinctive visible features

Do not beautify, de-age, symmetrize, change ethnicity, or replace distinctive features unless requested.

## Clothing, accessories, and social meaning

Preserve visible clothing, jewelry, eyewear, hairstyle, and pose-defining held objects unless the user asks to change them. A route changes photographic treatment, not the subject's occupation, class, era, or biography.

Never add work grime, torn clothing, cowboy styling, insects, scars, uniforms, jewelry, status symbols, or period costume merely because a corpus example contains them. `In the American West` provides composition, background, light, tone, and sitter-to-frame evidence; it is not permission to recast the user as one of its historical subjects.

## Partial face

- Preserve the visible geometry closely enough to remain recognizable.
- Keep the same missing or cropped region missing.
- Do not invent the hidden half of the face and then reframe it into view.
- Evaluate only visible identity evidence.
- Background replacement, tonal remapping, and a small inward trim are allowed.

## Profile

Prioritize forehead, nose, lips, chin, ear, hairline, and neck silhouette. Do not rotate toward the camera unless a separate identity reference shows the newly visible planes.

## Back view or no visible face

Set facial identity as not assessable. Preserve only evidence that exists:

- head and hair silhouette
- shoulder and neck relationship
- body proportions
- clothing and visible identifying details
- pose and stance

Never claim facial identity preservation when no face is visible.

A back-view input may be cropped inward to three-quarter body or waist-up while remaining a back view. Turning it into a visible face requires another clear reference image of the same person.

## Safe composition change

Cropping may remove body area but must not reconstruct identity-bearing content. Preserve:

- visible head and body orientation;
- facial visibility and recognizable facial geometry;
- expression category;
- body proportions inside the retained frame;
- visible hands and their relation when they remain inside the target crop;
- clothing continuity and pose-defining objects.

When a lower crop removes hands or objects, ensure the cut is intentional and anatomically clean; never regenerate a substitute hand or object elsewhere.

Subject placement and empty canvas are not identity-bearing by themselves. The Skill may move the crop window around the unchanged sitter or add seamless background-only canvas to repair imbalance. Background extension must not continue hair, face, skin, clothing, limbs, or held objects beyond their source boundary.

Do not treat missing technical detail as an invitation to reconstruct identity. Missed focus, motion blur, compression, opaque glare, or deep occlusion may limit what can be recovered. Never invent an eye behind opaque glare, new skin texture in a blurred face, or body shape hidden by the frame.

## Evaluation labels

- `facial_identity_assessable: true|false`
- `visible_identity_preserved: pass|review|fail`
- `unseen_structure_invented: true|false`
- `safe_crop_applied: true|false`
