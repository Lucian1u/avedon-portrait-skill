# Runtime Quality Check

Review the generated result before delivery.

## Hard failures

- framing scale changed outside the safe inward-crop matrix
- head or torso orientation changed
- partial face was completed into view
- back view was turned into a visible face
- single person became multiple people
- identity-defining visible features changed materially
- clothing, accessories, or social identity were replaced by corpus-specific subject styling
- background or props moved the result outside the supported formal-portrait domain
- an exact route was claimed for an unsupported or provisional evidence class
- a fallback copied route-specific pose or social styling instead of the transferable treatment core

## Scored dimensions

Score each from 0 to 4:

- `structure_preservation`
- `transformation_integrity`
- `visible_identity_preservation`
- `route_fidelity`
- `shared_style_fidelity`
- `technical_integrity`

Do not score facial identity when it is not assessable. For `crop_fallback`, structure preservation means the declared target crop is correct and every protected axis remains unchanged. A result cannot pass if `structure_preservation < 4`, `transformation_integrity < 4`, or any hard failure is present.

## Correction limit

If a result fails, make one targeted correction that names the failed dimension. Stop after the second total generation unless the user requests additional attempts.
