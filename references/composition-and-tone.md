# Composition and Tone Diagnosis

Use this reference for every eligible input before route execution. It separates repairable photographic defects from protected sitter structure. These repair heuristics are not new exact Avedon routes.

## Diagnostic record

Record only visible facts before proposing an edit:

```text
composition_intent: purposeful_asymmetry | accidental_imbalance | ambiguous
composition_defects: none | side_imbalance | edge_crowding | excessive_headroom | weak_crop | joint_tangency | mixed
protected_edges: <face, hair, hands, gesture, clothing, object, existing deliberate crop>
output_canvas: preserve_source | portrait | square | user_specified
composition_actions: <ordered list from keep, crop_recenter, tighten_crop, background_extend_recenter>
tone_defects: none | flat | clipped_highlights | blocked_shadows | muddy_midtones | subject_background_merge | uneven_face | overprocessed | mixed
capture_limits: none | low_resolution | motion_blur | focus_error | glare_occlusion | perspective_distortion | compression_artifacts | mixed
```

Do not infer intent from subject placement alone. First inspect the relationship among the sitter, gaze, gesture, frame edges, and negative space.

## Decide whether asymmetry is intentional

Treat off-center placement as purposeful when at least one visible relationship uses the open space: the gaze or face direction points into it; a hand, gesture, or torso movement activates it; a deliberate face or body crop creates stable edge tension; or retained scene information gives the space meaning. Preserve that directionality and remove only accidental excess.

Treat it as accidental when a frontal or visually still sitter is crowded against one side while the opposite side is blank, the open space has no relationship to gaze or gesture, headroom dominates without purpose, or a body edge nearly touches the frame while unused space remains elsewhere. For the three supported routes, centered placement and balanced side space are high-confidence corpus observations (`AP-EXP-FND-08`, `AP-EXP-MUS-08`, `AP-PIL-CAR-07`, `AP-EXP-CAR-32`, `AP-EXP-CAR-02`, `AP-EXP-CAR-23`). When those conditions apply and no purposeful asymmetry is visible, repair to a centered, balanced formal portrait.

If intent remains ambiguous, preserve mild asymmetry. Correct only obvious crowding or surplus space; do not normalize every portrait to a template.

Re-evaluate intent after background removal. Negative space that depended on a location, prop, or graphic background may no longer have a function against a seamless field.

## Composition repair hierarchy

Use the first safe action that creates an intentional frame:

1. **Crop and recenter inside the source.** Trim surplus space asymmetrically while keeping the selected output aspect ratio and every protected edge inside the crop.
2. **Tighten without changing the structural class.** A waist-up portrait may lose dead side or top space and remain waist-up. Route keys describe visible structure, not whether the original camera placement was good.
3. **Extend background only.** When an inward crop would cut hair, face, hands, clothing, or a pose-defining object, add featureless seamless background on the cramped side and rebalance the opposite side. Do not generate any new sitter pixels.
4. **Keep the placement.** If neither crop nor background-only extension can improve balance without identity reconstruction, preserve the source composition and complete only safe treatment.

Use an ordered action list when repair needs more than one operation. For example, a left-cramped sitter with excess right and top space may require `[background_extend_recenter, crop_recenter, tighten_crop]`: extend only the left background, trim the right, then reduce headroom.

## Output canvas

- Honor a user-specified aspect ratio only when it can be reached through a safe crop or background-only extension.
- Without a specified ratio, preserve the source canvas for purposeful asymmetry.
- For an accidentally imbalanced waist-up or three-quarter portrait, prefer a portrait canvas when every protected edge fits; use square when it preserves more sitter information; otherwise preserve the source ratio and repair only what is safe.
- Never force a portrait or square canvas by cutting protected sitter content or generating new sitter pixels.

For a frontal supported route, aim for the sitter's visual mass and face to read near the vertical centerline with balanced side space. Use modest headroom. Do not use a generic rule-of-thirds placement when it contradicts the route's stronger centered evidence.

## Crop craft

- Make every crop boundary explicit: which source edge moves, where the new lower edge falls, whether headroom changes, and which features remain protected.
- Avoid cuts directly through neck, shoulder joint, elbow, wrist, knee, or ankle. Prefer a clean interval between major joints. A three-quarter result normally ends above the knee or around upper-to-mid thigh, not through the knee.
- Do not graze hair, chin, fingers, elbows, or clothing edges by accident. Either include them with breathing room or exclude the larger region through a deliberate structural crop.
- Do not introduce a top-of-head crop unless the selected tight portrait makes it clearly intentional or the input already contains it.
- Preserve face-to-frame dominance for face fragments and profiles. Recenter the retained visible region, not an imagined complete face.
- Hands and pose-defining objects are protected when they remain within the selected scale. If a deliberate lower crop removes them completely, never cut through them or regenerate substitutes elsewhere.

## Tone and light diagnosis

Judge tone locally, not by a single global contrast adjective. Check the background, facial planes, eyes, hair, skin, clothing, and hands separately.

- Use neutral black-and-white. Separate skin, lips, eyes, hair, and clothing so adjacent colors do not collapse into one gray mass.
- Use a continuous white or light-neutral background. If white hair, pale skin, or white clothing disappears into it, choose light gray or preserve natural edge separation; do not draw an outline or invent a hard rim light.
- Establish a clear white point, black anchor, and readable midtones, but protect identity-bearing highlight and shadow detail. Background white may be clean; forehead, cheeks, eyes, hair, and dark clothing may not be clipped merely to look high contrast.
- Keep broad descriptive light for supported frontal routes. Preserve the source shadow topology and visible facial planes; soften or rebalance harshness through tone before attempting generative relighting. Do not reverse the key direction, invent catchlights, or create theatrical side light.
- Retain natural pores, wrinkles, hair, and garment texture without clarity halos, waxy skin, HDR microcontrast, fake grain, or global sharpening.
- Treat a dull source by expanding usable tonal separation, not by crushing blacks or bleaching highlights. The finished face must remain readable at normal viewing size.

## Capture limits

- Low resolution, missed focus, motion blur, and compression damage do not authorize invented eyelashes, pores, teeth, jewelry, or fabric detail. Improve legibility only within visible evidence.
- Do not remove opaque glasses glare or another occlusion when doing so would invent an eye. Reduce transparent glare only when the eye remains visibly evidenced.
- Severe wide-angle facial or body distortion is not a routine composition defect. Do not reshape the face or body to simulate another lens; use a safe crop if it helps and report the remaining source limitation.

## Why these rules exist

- The Metropolitan Museum of Art describes Avedon's mature formal portraits as bright seamless backgrounds with no extraneous detail, sharp clarity, descriptive non-idealizing treatment, diffuse or flat light, and disciplined tight framing: <https://www.metmuseum.org/exhibitions/listings/2002/richard-avedon>.
- Nikon's framing guidance identifies excess headroom and cuts through major joints as common crop defects: <https://www.nikonusa.com/learn-and-explore/c/tips-and-techniques/video-composition-rules-establishing-medium-and-close-up-shots>.
- The National Portrait Gallery notes that negative space can carry meaning and that cropping changes a portrait's mood and story; this is why off-center space must be interpreted before it is removed: <https://www.npg.org.uk/schools-hub/how-to-analyse-a-portrait>.
- Adobe's tonal guidance distinguishes black point, white point, and midtone control and warns that clipping destroys detail: <https://www.adobe.com/learn/photoshop/paths/photo-editing/photoshop/series/photography/learn-photo-editing-essentials/photoshop/web/photoshop-improve-tones-levels> and <https://helpx.adobe.com/ca/camera-raw/desktop/using/make-color-tonal-adjustments-camera.html>.

Avedon's use of the full sheet means post-capture reframing is a product adaptation for imperfect user inputs, not a claim that his original method depended on later cropping.
