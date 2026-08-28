# Rejection and Clarification Rules

## Reject from this Skill

- Any image where `subject_count != 1`, including a dominant sitter plus a background person
- Diptych, triptych, or other multi-panel/repeated-person composite
- Fashion editorial intent
- Reportage or documentary-scene transformation
- Product-led advertising composition
- Inputs where the primary person cannot be structurally identified
- Requests that require creating a visible identity from no usable identity evidence

## Authorized default changes

Do not ask before an inward crop, recentering, background removal/replacement, or monochrome tonal remap. These are part of the product behavior. Follow `transformation-fallbacks.md` and preserve head view, face visibility, expression, visible facial geometry, clothing, and identity.

Ask for another identity reference only when the requested result must expose facial structure that the input does not show. A back view, profile, or partial face may still be completed without asking if it remains back/profile/partial.

## No exact route

Do not stop merely because an exact route is `provisional` or `unsupported`.

1. Try `crop_fallback` to the nearest supported target.
2. If no identity-safe target exists, use `treatment_only` on the current structure.
3. Keep evidence status internal during ordinary delivery; do not tell the user that the result is “not Avedon.”
4. If the user explicitly asks about research support, answer accurately and distinguish the exact route from the fallback treatment.

Never expose a hidden face, rotate an unseen face toward camera, or invent missing anatomy simply to avoid a fallback.
