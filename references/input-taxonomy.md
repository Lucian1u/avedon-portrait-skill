# Input Taxonomy

Classify structure before applying style. Do not compress the axes into a single ambiguous `shot_type`.

## Eligibility

- Exactly one visible person (`subject_count=1`), not merely one dominant person.
- Exactly one image frame; diptychs, triptychs, and repeated-person composites are outside V1.
- The person's structural class can be read with reasonable confidence.
- The input background may be environmental; the output may replace it with a controlled background.
- A face does not have to be fully visible. Partial-face, profile, over-shoulder, and back-view inputs remain eligible through treatment-only fallback even when no exact route is supported.

## Structural axes

### Framing scale

- `face_detail`: the frame cuts into the face itself; at least one major facial region or one side of the face is outside the frame.
- `tight_head`: the face dominates and the major facial features remain visible; hair, scalp, ear edge, chin edge, or neck may meet or cross the frame.
- `head_and_shoulders`: head and shoulders, without lower torso.
- `bust`: head through chest or ribcage.
- `waist_up`: head through waist.
- `three_quarter_body`: lower edge falls between thigh and shin.
- `full_body`: head through feet.

### Head view

- `frontal`
- `three_quarter_facing_image_left`
- `three_quarter_facing_image_right`
- `profile_facing_image_left`
- `profile_facing_image_right`
- `back`
- `over_shoulder`

### Head attitude

Classify horizontal view separately from:

- `head_tilt`: level, toward image left, or toward image right;
- `chin_angle`: neutral, raised, or lowered.

### Torso view

Use the same directional labels plus `not_visible`.

### Face visibility

- `full`: essentially the whole face is visible.
- `partial`: the frame or an object removes a meaningful facial region.
- `none`: no facial features are visible.
- `occluded`: the face position is present but covered.

### Crop pattern

- `none`
- `face_fragment_image_left_edge`
- `face_fragment_image_right_edge`
- `top_of_head`
- `chin_or_jaw`
- `hand_or_arm`
- `leg_or_foot`
- `multiple`
- `other`

## Canonical route key

After choosing an analysis subset, build the complete route key from:

```text
analysis_subset|framing_scale|head_view|face_visibility|crop_pattern
```

Examples:

```text
formal_portrait_general|waist_up|frontal|full|none
in_the_american_west|three_quarter_body|frontal|full|leg_or_foot
```

`GEN-WAIST-FRONT-FULL-NONE` and `IAW-3Q-FRONT-FULL-LEG` are human-readable display aliases only.

Use torso view, head attitude, and still-versus-dynamic pose as secondary discriminators. Do not create a unique route for every theoretical combination. Promote a combination only after corpus evidence shows a repeatable language.

## Transformation rule

Classify both the input and intended output. Exact routes preserve the complete key. Fallbacks may reduce framing scale through an inward crop and may change the lower crop pattern that results from that crop. They must preserve head view, face visibility, visible facial geometry, expression category, and identity.

The route key does not encode whether the photograph is well composed. Classify `composition_intent`, `composition_defects`, `composition_action`, `tone_defects`, and `capture_limits` separately with `composition-and-tone.md`.

The Skill may refine subject scale, headroom, side spacing, background, light, and tone. It may extend featureless background when that avoids cutting protected sitter content. It may not complete a partial face, expose an unseen face, or rotate a profile/back view toward the camera without an additional identity reference that shows the missing facial structure. Read `transformation-fallbacks.md` for the permitted matrix.
