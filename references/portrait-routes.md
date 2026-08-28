# Portrait Routes

Use this file for `exact_route` or when a safe inward crop produces one of these exact target keys. Shared rules come from `style-dna.md`; this file supplies route-specific constraints. Unsupported target structures use `transformation-fallbacks.md`, not a route prompt copied by analogy.

## Route record format

Each supported route must include:

```text
route_key:
status:
analysis_subset:
structural_confidence:
lighting_confidence:
supporting_records:
framing_and_crop:
subject_placement:
background:
light_and_tone:
gaze_and_expression:
hands_and_posture:
identity_constraints:
negative_constraints:
quality_checks:
known_variation:
```

## `GEN-WAIST-FRONT-FULL-NONE`

- status: `supported`
- analysis_subset: `formal_portrait_general`
- structural_confidence: `high`
- lighting_confidence: `high`
- supporting_records: `AP-PIL-MUS-03`, `AP-PIL-MUS-04`, `AP-EXP-FND-04`, `AP-EXP-FND-08`, `AP-EXP-FND-10`, `AP-EXP-FND-12`, `AP-EXP-FND-15`, `AP-EXP-FND-17`, `AP-EXP-MUS-01`, `AP-EXP-MUS-03`, `AP-EXP-MUS-04`, `AP-EXP-MUS-07`, `AP-EXP-MUS-08`, `AP-EXP-MUS-09`, `AP-EXP-MUS-10`
- framing_and_crop: retain waist-up scale and keep face, head, hands, and lower frame regions visible or hidden exactly as the input class dictates; no face/head/limb crop.
- subject_placement: centered, balanced side space; portrait orientation preferred, square allowed if inherited from the input.
- background: continuous white is the dominant observation (14/15); continuous mid-gray is a supported variation (`AP-EXP-FND-04`). No backdrop edge or environment.
- light_and_tone: neutral black-and-white; broad frontal soft light; medium or high contrast; preserve highlight and deep-black detail.
- gaze_and_expression: retain direct gaze and the user's mouth state. Closed-neutral dominates, but supported smiles exist (`AP-PIL-MUS-04`, `AP-EXP-MUS-03`).
- hands_and_posture: keep the input's visible-hand count and relation. Evidence includes both hands, partial hands, and no hands; both open and closed postures are valid.
- identity_constraints: preserve face, age, skin, hair, clothing, eyewear, jewelry, and existing held objects.
- negative_constraints: no hard side-light drama, beauty retouch, invented props, occupational restyling, or print border unless requested.
- quality_checks: exact waist-up/frontal/full/no-crop key remains unchanged; subject centered; background contains no environment; visible identity passes.
- known_variation: white versus mid-gray background; neutral, slight smile, or open smile; seated or standing.

## `IAW-WAIST-FRONT-FULL-NONE`

- status: `supported`
- analysis_subset: `in_the_american_west`
- structural_confidence: `high`
- lighting_confidence: `medium`; broad series-level treatment, not a precise key-light claim
- supporting_records: `AP-PIL-CAR-03`, `AP-PIL-CAR-06`, `AP-PIL-CAR-07`, `AP-PIL-CAR-10`, `AP-EXP-CAR-07`, `AP-EXP-CAR-14`, `AP-EXP-CAR-32`
- framing_and_crop: retain waist-up scale, full face, frontal head, and no structural crop. Do not expose hands that begin outside the frame.
- subject_placement: centered in a portrait frame with balanced side space.
- background: featureless seamless white; no floor line, environment, or invented contextual cue.
- light_and_tone: neutral black-and-white, broad frontal soft-to-medium light, medium-to-high contrast. The exact Carter-source light field is unresolved in 3/7 supporting records, so do not add directional theatricality.
- gaze_and_expression: preserve direct gaze, mouth state, and intensity; closed neutral and parted lips are both evidenced.
- hands_and_posture: hands may be absent, single, or both. Preserve the input's relation to clothing, body, or existing object.
- identity_constraints: use IAW only for photographic treatment. Never add worker grime, cowboy styling, bees, nudity, a uniform, scars, tools, or historic dress from the supporting sitters.
- negative_constraints: no environmental West, documentary location, fictional occupation, or stereotype; no automatic black print border.
- quality_checks: exact waist-up/frontal/full/no-crop key; white seamless background; clothing and social identity unchanged.
- known_variation: slight torso rotation and one raised shoulder are valid only when inherited from the input.

## `IAW-3Q-FRONT-FULL-LEG`

- status: `supported`
- analysis_subset: `in_the_american_west`
- structural_confidence: `high`
- lighting_confidence: `medium`; all 12 exact-key expanded records have unresolved direction and hardness, so use series-level evidence only
- supporting_records: `AP-EXP-CAR-01`, `AP-EXP-CAR-02`, `AP-EXP-CAR-06`, `AP-EXP-CAR-11`, `AP-EXP-CAR-12`, `AP-EXP-CAR-13`, `AP-EXP-CAR-16`, `AP-EXP-CAR-17`, `AP-EXP-CAR-20`, `AP-EXP-CAR-23`, `AP-EXP-CAR-27`, `AP-EXP-CAR-28`
- framing_and_crop: show head through upper or mid-thigh; keep feet/lower legs outside the frame. Never widen to full body or tighten to waist-up.
- subject_placement: centered portrait frame with balanced side space.
- background: featureless seamless white, no floor line and no environmental context.
- light_and_tone: neutral black-and-white and medium-to-high contrast. Use the series-level broad frontal soft-to-medium light supported by `AP-PIL-CAR-01`, `AP-PIL-CAR-02`, `AP-PIL-CAR-04`, `AP-PIL-CAR-05`, `AP-PIL-CAR-09`; the expanded source images do not justify a more specific lighting claim.
- gaze_and_expression: preserve the input. Direct gaze/closed neutral is common, while closed eyes/open expression is supported by `AP-EXP-CAR-28`.
- hands_and_posture: hands usually participate in this scale, but their exact count, gesture, and relation must come from the input. Slight torso rotation is allowed without changing the frontal head class.
- identity_constraints: preserve clothing, body proportions, stance, accessories, and existing objects. The route may reveal texture already present, never invent biographical wear.
- negative_constraints: no full-body completion, no new hands or objects, no historical-worker styling, no environmental West, no automatic print border.
- quality_checks: lower crop remains thigh-level with feet hidden; head remains frontal/full; subject remains centered; identity and clothing pass.
- known_variation: still pose or inherited gesture in progress; neutral or expressive face; open, mixed, or closed posture.

## Structures without an exact route

Tight head, head-and-shoulders, bust, face fragment, full body, profile, over-shoulder, back view, occluded face, and every unlisted crop/view combination must not copy one of these complete route prompts by analogy. Follow `transformation-fallbacks.md`: use a safe inward crop when possible, otherwise apply only the transferable treatment core while preserving the input's visible identity.
