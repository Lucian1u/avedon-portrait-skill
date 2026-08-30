---
name: avedon-portrait
description: Diagnose and edit a user-provided single-person portrait into an Avedon-style formal result. Repairs accidental imbalance through safe crop, recentering, or background-only canvas extension; then applies evidence-backed background, light, and monochrome treatment while preserving visible identity. Do not use for fashion, reportage, groups, or product-led scenes.
---

# Avedon Portrait

Produce a useful portrait for any eligible single-person input. Diagnose the photograph before choosing a route: identity protection, composition repair, and photographic treatment are separate decisions. Evidence status may limit a style claim, but it must not prevent a safe composition correction.

## Workflow

1. Require one user-provided, single-frame image with `subject_count=1`. Read [references/rejection-rules.md](references/rejection-rules.md) only if eligibility or identity evidence is uncertain.
2. Read [references/input-taxonomy.md](references/input-taxonomy.md) and classify the protected structure. Then read [references/composition-and-tone.md](references/composition-and-tone.md) and record composition intent, visible defects, protected edges, tonal defects, output canvas, and an ordered set of repair actions. Do this even when the structural route is already supported.
3. Select `formal_portrait_general` by default, or `in_the_american_west` only when the user explicitly requests it or provides an IAW reference. Build the canonical structural key: `analysis_subset|framing_scale|head_view|face_visibility|crop_pattern`.
4. Read [references/supported-routes.md](references/supported-routes.md). For a supported input key, use `exact_route` and read its section in [references/portrait-routes.md](references/portrait-routes.md) plus [references/style-dna.md](references/style-dna.md). Otherwise read [references/transformation-fallbacks.md](references/transformation-fallbacks.md) and choose the smallest safe structural change. If that target key is supported, use `crop_fallback` and read its matching section in `portrait-routes.md`; use `treatment_only` for every other safe target.
5. Apply [references/identity-preservation.md](references/identity-preservation.md). Build one edit plan in this priority order: preserve identity and sitter-authored structure; repair accidental composition; apply background, light, and tone. `treatment_only` is an evidence label, not a ban on crop, recentering, or background-only extension.
6. Read [references/generation-execution.md](references/generation-execution.md), translate the internal analysis into a short visual instruction, and perform a source-conditioned edit. Evaluate source and result with [references/quality-check.md](references/quality-check.md); make at most one targeted correction from the original source unless the user asks for more.

## Invariants

- A partial face remains partial, a back view remains back, and a profile remains profile unless an additional identity reference supplies the missing facial evidence.
- Full-body and three-quarter-body inputs may be cropped inward. Never expand the frame or reveal hidden facial or body structure merely to make the result look conventional.
- Extending featureless background is allowed when it is the least destructive way to recenter a cramped sitter. The extension must contain background only; never outpaint missing hair, face, hands, clothing, or body.
- Off-center placement is not automatically intentional. Preserve it when gaze, gesture, pose, an edge crop, or meaningful space supports it; otherwise correct obvious dead space, edge crowding, or excessive headroom.
- Evidence status controls internal route selection, not ordinary user-facing disclaimers. Never invent an exact route, but do not stop an otherwise safe treatment-only result.
- Never use fashion, reportage, group, or environmental-portrait rules as evidence for this Skill.
- Treat `In the American West` as a separate analysis subset; when its route supplies a crop fallback, transfer photography mechanics only and never sitter-specific social styling.
- Never select the IAW subset from the user's perceived occupation, ethnicity, clothing, class, age, or physical condition.
- Do not describe a style rule as established unless its reference cites corpus record IDs.
- A generated lookalike is not an acceptable edit. If the source image cannot be supplied to the image tool, stop and ask the user to attach it again.
