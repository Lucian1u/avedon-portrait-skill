# Supported Routes

## Status meanings

- `supported`: repeated corpus evidence defines a usable route and its quality can be evaluated.
- `provisional`: candidate examples exist, but the pattern is not stable enough for generation.
- `unsupported`: evidence is absent, contradictory, or outside Corpus V1.
- `not_evaluated`: reserved for a future corpus expansion; V1 has completed evaluation.

## Runtime selection policy

The three keys below are the exact corpus-supported routes. They are also valid targets for a safe inward crop. A related crop does not become evidence-supported merely because the Skill can still produce it through `treatment_only`.

General formal portrait is the default subset. Never choose `In the American West` from the person's occupation, clothing, ethnicity, apparent social class, or physical condition. Use the IAW waist-up route only when the user explicitly requests that subset or provides an IAW reference.

For unsupported inputs, read `transformation-fallbacks.md`. First choose the same-subset target that removes the least identity-bearing information while preserving head view, face visibility, visible facial geometry, expression, and identity. Only then label the mode: use `crop_fallback` when that chosen target is an exact supported key and `treatment_only` otherwise. Never tighten a crop farther merely to obtain a supported label, and never switch a general request into IAW to obtain one.

Keep `exact_route`, `crop_fallback`, and `treatment_only` distinct internally. Ordinary output does not need to explain these corpus labels to the user.

## Supported exact keys

| Display alias | Canonical route key | Count | Supporting records |
| --- | --- | ---: | --- |
| `GEN-WAIST-FRONT-FULL-NONE` | `formal_portrait_general|waist_up|frontal|full|none` | 15 | `AP-PIL-MUS-03`, `AP-PIL-MUS-04`, `AP-EXP-FND-04`, `AP-EXP-FND-08`, `AP-EXP-FND-10`, `AP-EXP-FND-12`, `AP-EXP-FND-15`, `AP-EXP-FND-17`, `AP-EXP-MUS-01`, `AP-EXP-MUS-03`, `AP-EXP-MUS-04`, `AP-EXP-MUS-07`, `AP-EXP-MUS-08`, `AP-EXP-MUS-09`, `AP-EXP-MUS-10` |
| `IAW-WAIST-FRONT-FULL-NONE` | `in_the_american_west|waist_up|frontal|full|none` | 7 | `AP-PIL-CAR-03`, `AP-PIL-CAR-06`, `AP-PIL-CAR-07`, `AP-PIL-CAR-10`, `AP-EXP-CAR-07`, `AP-EXP-CAR-14`, `AP-EXP-CAR-32` |
| `IAW-3Q-FRONT-FULL-LEG` | `in_the_american_west|three_quarter_body|frontal|full|leg_or_foot` | 12 | `AP-EXP-CAR-01`, `AP-EXP-CAR-02`, `AP-EXP-CAR-06`, `AP-EXP-CAR-11`, `AP-EXP-CAR-12`, `AP-EXP-CAR-13`, `AP-EXP-CAR-16`, `AP-EXP-CAR-17`, `AP-EXP-CAR-20`, `AP-EXP-CAR-23`, `AP-EXP-CAR-27`, `AP-EXP-CAR-28` |

## Evidence matrix

| Structural family | General formal portrait | In the American West |
| --- | --- | --- |
| face detail / fragment | `unsupported` | `unsupported` |
| tight head | `provisional` (7 exact records; mature-period rule not stable) | `provisional` |
| head and shoulders | `unsupported` | `unsupported` |
| bust | `provisional` | `provisional` |
| waist up | `supported` only for frontal + full + no crop | `supported` only for frontal + full + no crop |
| three-quarter body | `provisional` | `supported` only for frontal + full + leg/foot crop |
| full body | `unsupported` | `unsupported` |
| profile | `unsupported` | `unsupported` |
| over shoulder | `unsupported` | `unsupported` |
| back view | `unsupported` | `unsupported` |
| occluded or non-visible face | `unsupported` | `unsupported` |

## Dimension-specific confidence

`supported` describes the complete structural key, not equal certainty for every photographic variable.

| Route | Structure | Background and tone | Light direction and hardness |
| --- | --- | --- | --- |
| `GEN-WAIST-FRONT-FULL-NONE` | high | high | high |
| `IAW-WAIST-FRONT-FULL-NONE` | high | high | medium |
| `IAW-3Q-FRONT-FULL-LEG` | high | high | medium, series-level inference only |

For either IAW route, do not invent a precise key position or theatrical shadow pattern. Preserve the source face planes and use broad descriptive tonal mapping.

## Promotion evidence

A route can become `supported` only when:

- at least six route-eligible records show the exact structural key;
- the relevant composition, crop, background, light, tone, pose, and expression observations are sufficiently consistent to write an operational rule;
- the rule cites its supporting `record_id` values;
- at least one evaluation case can distinguish a correct route from structural normalization;
- the route does not depend on fashion, reportage, group, or environmental examples.

Count alone is not enough. Coverage across works and consistency of the observed pattern both matter.

The general frontal tight-head exact key has seven route-eligible records, but only two are from the mature 1969-onward method period and the lighting/background observations remain heterogeneous. It therefore stays `provisional` as an exact route; the structure may still be completed through `treatment_only`.
