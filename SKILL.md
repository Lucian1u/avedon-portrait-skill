---
name: avedon-portrait
description: Transform a user-provided single-person image into an Avedon-style formal portrait using an exact supported route when available and a safe crop or treatment fallback otherwise. May crop inward, recenter, remove backgrounds, and remap monochrome tone while preserving visible identity and never inventing unseen facial structure. Do not use for fashion, reportage, groups, or product-led scenes.
---

# Avedon Portrait

Produce a useful portrait for any eligible single-person input. Prefer exact evidence; otherwise crop safely or transfer only the photographic treatment. Composition may change, but visible identity may not be rebuilt.

## Workflow

1. Require one user-provided image with `subject_count=1`. Any second visible person is outside V1, even when one person dominates.
2. Read [references/input-taxonomy.md](references/input-taxonomy.md) and classify the input on each structural axis.
3. Select `formal_portrait_general` by default, or `in_the_american_west` when the user explicitly requests it or provides an IAW reference. Build the canonical input key: `analysis_subset|framing_scale|head_view|face_visibility|crop_pattern`.
4. Read [references/supported-routes.md](references/supported-routes.md). If the input key is supported, use `execution_mode=exact_route` and read only its matching section in [references/portrait-routes.md](references/portrait-routes.md).
5. Otherwise read [references/transformation-fallbacks.md](references/transformation-fallbacks.md). Choose the safe target that removes the least identity-bearing information; do not crop farther merely to earn an exact-route label. After choosing the target, use `crop_fallback` only when that target is an exact supported key, otherwise use `treatment_only`.
6. Read [references/style-dna.md](references/style-dna.md) for exact routes. For fallbacks, apply only the transferable treatment core in `transformation-fallbacks.md`.
7. Apply [references/identity-preservation.md](references/identity-preservation.md). Preserve head view, face visibility, visible facial geometry, expression category, clothing, and sitter-authored gesture. Never reveal an unseen face unless a separate identity reference shows it.
8. Read [references/rejection-rules.md](references/rejection-rules.md). Reject only inputs outside the single-person formal-portrait product boundary or requests that require identity invention without a usable identity reference.
9. Read [references/generation-execution.md](references/generation-execution.md), compile the edit prompt, and perform a reference-conditioned image edit with the user's source image attached as the authoritative identity input. Never substitute text-only image generation.
10. Evaluate the result with [references/quality-check.md](references/quality-check.md). Make at most one corrective regeneration unless the user asks for more.

## Invariants

- A partial face remains partial, a back view remains back, and a profile remains profile unless an additional identity reference supplies the missing facial evidence.
- Full-body and three-quarter-body inputs may be cropped inward. Never expand the frame or reveal hidden facial or body structure merely to make the result look conventional.
- Evidence status controls internal route selection, not ordinary user-facing disclaimers. Never invent an exact route, but do not stop an otherwise safe treatment-only result.
- Never use fashion, reportage, group, or environmental-portrait rules as evidence for this Skill.
- Treat `In the American West` as a separate analysis subset; when its route supplies a crop fallback, transfer photography mechanics only and never sitter-specific social styling.
- Never select the IAW subset from the user's perceived occupation, ethnicity, clothing, class, age, or physical condition.
- Do not describe a style rule as established unless its reference cites corpus record IDs.
- A generated lookalike is not an acceptable edit. If the source image cannot be supplied to the image tool, stop and ask the user to attach it again.
