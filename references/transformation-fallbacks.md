# Transformation Fallbacks

Use this file only when the input has no exact supported route. The Skill should still produce a useful portrait whenever identity can be preserved.

## Execution modes

Choose the target before choosing the label:

1. If the input key exactly matches a supported key, use `exact_route`.
2. Otherwise choose the safe target that removes the least identity-bearing information and still creates an intentional formal portrait.
3. If that chosen target is an exact supported key, use `crop_fallback`; otherwise use `treatment_only` with the transferable photographic treatment.

Never delete additional face, gesture, hands, clothing, or body information solely to convert `treatment_only` into `crop_fallback`.

Track the mode internally. In ordinary delivery, do not add a disclaimer that the result is “not Avedon” and do not ask the user to understand corpus terminology. Do not claim an exact route name unless `execution_mode=exact_route` or the target of `crop_fallback` actually matches that key.

## Safe transformation rule

Inward deletion is allowed; outward invention is not.

Allowed without asking:

- crop `full_body` to `three_quarter_body` or `waist_up`;
- crop `three_quarter_body` to `waist_up`;
- recenter the sitter and adjust side or top space;
- remove an environmental background and replace it with a continuous white or light neutral controlled background;
- convert to neutral black-and-white and remap contrast;
- preserve an existing side, profile, partial-face, over-shoulder, or back orientation while changing only scale and treatment.

Never do automatically:

- complete a face fragment into view;
- rotate a profile, partial face, over-shoulder view, or back view into a frontal face;
- widen the frame to reveal missing hands, legs, feet, hair, or clothing;
- invent a new pose, expression, garment, accessory, or object;
- use a crop that cuts through a major facial region when the input did not already do so.

## Target selection

Choose the target that removes the least identity-bearing information while satisfying the explicit matrix below. The matrix overrides any generic preference for a supported key.

| Input | Default result |
| --- | --- |
| general frontal full-body, full face | crop to `formal_portrait_general|three_quarter_body|frontal|full|leg_or_foot`; use `treatment_only`, keep the lower edge at thigh level, and preserve the visible face, pose, hands, clothing, and objects |
| explicitly requested or referenced IAW frontal full-body, full face | crop to `IAW-3Q-FRONT-FULL-LEG`; use `crop_fallback` and keep the lower edge at thigh level |
| frontal three-quarter body with an unsupported lower crop | retain the three-quarter scale and use `treatment_only` when tightening to waist-up would remove more pose, hand, clothing, or object information; crop to waist-up only when the source already supports that smaller intentional composition with less loss |
| side, profile, over-shoulder, or back full-body | crop to three-quarter body in the same orientation; use `treatment_only` unless the resulting complete key is supported |
| face fragment or partial face | keep the same facial region outside the frame; use `treatment_only` |
| unsupported tight head, head-and-shoulders, bust, or crop combination | keep its current head view and face visibility; use `treatment_only`, optionally with a small non-structural trim |

Never change the selected subset merely to obtain a supported target. Do not copy IAW clothing, occupation, historical period, dirt, scars, tools, insects, or social cues when IAW is explicitly selected.

## Transferable treatment core

These controls come from the repeated behavior of the three supported routes; they are treatment components, not evidence that every unsupported orientation was itself common in the corpus.

- background: remove readable location information and use a continuous controlled white or light-neutral background. Evidence: `AP-EXP-MUS-01`, `AP-EXP-MUS-07`, `AP-PIL-CAR-03`, `AP-EXP-CAR-14`, `AP-EXP-CAR-01`, `AP-EXP-CAR-20`.
- tonality: neutral black-and-white with separation in skin, hair, and clothing. Evidence: `AP-PIL-MUS-03`, `AP-EXP-FND-10`, `AP-PIL-CAR-06`, `AP-EXP-CAR-32`, `AP-EXP-CAR-11`, `AP-EXP-CAR-27`.
- contrast and texture: medium-to-high printable contrast; retain pores, wrinkles, garment detail, highlights, and deep blacks. Evidence: `AP-EXP-FND-08`, `AP-EXP-MUS-07`, `AP-PIL-CAR-01`, `AP-PIL-CAR-09`.
- light mapping: for a frontal visible face, broad descriptive light is preferred. For side, profile, partial-face, or back inputs, preserve the input's light direction and visible planes; remap tone without relighting an unseen face plane.
- expression and gesture: preserve the input. Evidence for valid variation: `AP-PIL-MUS-04`, `AP-EXP-MUS-03`, `AP-PIL-CAR-03`, `AP-EXP-CAR-28`.
- presentation: a black print border is never automatic.

## Hidden-face requests

If the user explicitly requests a visible frontal face from an input that does not show enough facial identity, require an additional clear reference image of the same person before revealing it. Use that image only as identity evidence; preserve the requested target crop and re-run route selection.

Without that reference, keep the face hidden or partial and complete the portrait through `treatment_only`.

## Internal decision record

Maintain these values while working:

```text
execution_mode: exact_route | crop_fallback | treatment_only
input_route_key:
target_route_key:
safe_transform:
facial_identity_assessable: true | false
unseen_structure_invented: false
```
