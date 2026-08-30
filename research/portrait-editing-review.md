# Portrait Editing Review for Runtime Repair

Checked: 2026-08-30

This review addresses a runtime gap: the corpus records composition and tone, but the V1 Skill originally routed mainly by framing scale, head view, face visibility, and crop pattern. The purpose is to add general portrait-repair knowledge without promoting new Avedon route evidence.

## Source facts

### Avedon's mature formal method

The Metropolitan Museum of Art describes the mature portrait work as using a bright white seamless background without props or extraneous details, emphasizing the specificity of face, gaze, dress, and gesture. It also describes sharp clarity, non-idealizing treatment, shadowless diffuse sunlight or comparable flat studio light, disciplined tight framing, and Avedon's use of the entire uncropped sheet. Source: <https://www.metmuseum.org/exhibitions/listings/2002/richard-avedon>.

These are historical and curatorial facts about Avedon's practice. They do not prove that a post-capture crop is itself an Avedon method.

### General composition and crop craft

Nikon's framing guidance treats excess headroom and cuts through major joints as common errors. It recommends a small amount of headroom, placing eyes near the upper third for a tight close-up, avoiding cuts at wrists, knees, and ankles, and placing a medium lower crop above rather than through the knee. Source: <https://www.nikonusa.com/learn-and-explore/c/tips-and-techniques/video-composition-rules-establishing-medium-and-close-up-shots>.

The National Portrait Gallery defines negative space as the area around the sitter and demonstrates that changing a crop can change mood, atmosphere, and the story told about the sitter. Source: <https://www.npg.org.uk/schools-hub/how-to-analyse-a-portrait>.

These are general portrait heuristics, not substitutes for corpus-specific route evidence.

### Tone and clipping

Adobe's Levels guidance separates black point, white point, and midtone control and recommends backing away when black or white clipping removes desired detail. Camera Raw documentation defines clipping as values forced to output white or black with resulting detail loss. Sources: <https://www.adobe.com/learn/photoshop/paths/photo-editing/photoshop/series/photography/learn-photo-editing-essentials/photoshop/web/photoshop-improve-tones-levels> and <https://helpx.adobe.com/ca/camera-raw/desktop/using/make-color-tonal-adjustments-camera.html>.

## Corpus observations

The current 85-record annotated corpus contains 80 `centered` placements and 73 `balanced` negative-space records. The three supported exact routes are described in `style-dna.md` as 34 route-eligible records with centered placement; representative support includes `AP-EXP-FND-08`, `AP-EXP-MUS-08`, `AP-PIL-CAR-07`, `AP-EXP-CAR-32`, `AP-EXP-CAR-02`, and `AP-EXP-CAR-23`.

The same corpus also contains offset and directional examples. Off-center placement therefore cannot be treated as an error without examining gaze, gesture, edge crop, and negative-space function.

## Operational interpretation

1. **Separate structure from composition quality.** A waist-up, frontal, full-face input can match an exact structural key and still be badly composed. `subject_placement`, negative space, headroom, and crop tangencies must be diagnosed independently.
2. **Do not equate treatment-only with tone-only.** `treatment_only` is an evidence label for an unsupported structural route. It does not forbid a safe crop, recentering, scale refinement, or background-only extension.
3. **Interpret asymmetry before correcting it.** Preserve open space that is activated by gaze, gesture, pose, deliberate edge tension, or meaningful retained context. Correct one-sided dead space, edge crowding, and excess headroom when no such relationship exists.
4. **Prefer geometry over regeneration.** A deterministic crop should be used when available. If crop-only recentering would cut protected sitter content, extend only featureless background. Never extend the sitter.
5. **Make crop boundaries anatomical.** Avoid joints and accidental tangencies. State the new source edges or body landmark rather than asking generically for a “better crop.”
6. **Make tone local.** A white background, black anchor, and broad contrast are insufficient if skin, eyes, hair, hands, or clothing merge or clip. Evaluate those regions separately and use light gray when pure white would erase pale sitter edges.
7. **Preserve source light topology.** Broad descriptive light is a target treatment, but reconstructing a new face plane or catchlight is an identity change. Prefer tonal rebalance over theatrical relighting.
8. **Respect capture limits.** Blur, opaque glare, missed focus, compression, and severe perspective distortion are not missing details to invent.

## Product boundary

Avedon's full-sheet discipline was achieved during capture. This Skill serves imperfect user inputs, so post-capture crop and background-only extension are justified as conservative product repairs. They must be presented internally as adaptations, not as historical claims about his process or as support for new exact routes.
