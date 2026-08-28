# Generation Execution

Use this file after the input and target routes, execution mode, identity constraints, and safe transformation are known. It turns the research rules into one reference-conditioned image edit.

## Non-negotiable tool contract

- The user's source image is the authoritative edit target and identity input.
- Use an image capability that accepts image input and returns an edited image. If it exposes an `edit` versus `generate` action, choose `edit`. If it exposes one unified image action, attach the source image and state that it is the edit target.
- Use high input fidelity when the tool supports that control. Do not silently fall back to text-only generation.
- Never use an Avedon corpus image as a visual identity or style reference. The corpus supplies written rules only.
- If the source image is unavailable to the tool, ask the user to attach it again. Do not generate a guessed sitter.

## Source roles

Label every image before the tool call:

```text
Image 1: authoritative edit target; source of visible identity, expression, pose, clothing, hands, accessories, and objects.
Image 2: optional identity-only reference supplied by the user; may reveal missing facial structure only when the requested output needs it.
```

An optional identity reference never supplies clothes, pose, background, lighting, or route style.

## Canvas and crop

- Derive the output only through inward cropping and recentering of visible source content. Never outpaint hidden face, hair, hands, feet, clothing, or body merely to reach an aspect ratio.
- Preserve the source orientation and aspect ratio unless the declared target crop can be made entirely inside the source bounds. Choose the tool's closest supported canvas orientation only after the crop is fixed.
- For general frontal full-body fallback, place the lower edge at upper or mid-thigh, keep the head through thighs, and use `treatment_only`. Do not tighten to waist-up merely because that key is supported.
- For side, profile, over-shoulder, or back full-body fallback, use the same thigh-level target while preserving orientation.
- For face fragments, retain the same missing facial region and approximately the same face-to-frame dominance.

## Prompt compiler

Assemble one edit prompt from the fields below. Omit empty fields; do not replace them with generic Avedon mythology.

```text
Use case: identity-preserve portrait edit
Edit target: Image 1 is authoritative. Edit this person; do not generate a new sitter or lookalike.

Protected identity and structure:
- preserve: <head view, face visibility, visible facial geometry, expression category>
- preserve: <pose, visible-hand count and relation, clothing, accessories, existing objects>
- never reveal: <all face or body regions outside the source or target crop>

Declared transformation:
- execution mode: <exact_route | crop_fallback | treatment_only>
- target structure: <canonical target key>
- crop and placement: <explicit lower edge, headroom, side space, recentering>
- background: remove location information; use <route-approved seamless tone>

Photographic treatment:
- neutral black-and-white with skin, hair, and clothing separation
- <route-specific light and contrast instruction, limited by its confidence>
- retain pores, wrinkles, hair, garment texture, and natural asymmetry; no beauty retouch

Negative constraints:
- no frontalization, face completion, de-aging, beautification, symmetry correction, or gaze/expression replacement
- no invented hands, fingers, limbs, clothing, jewelry, props, text, watermark, print border, background seam, or duplicate person
- no IAW worker grime, cowboy styling, period costume, insects, tools, scars, occupation, or social narrative

Output: one finished formal portrait edit; no collage, before/after panel, caption, or added text.
```

For `exact_route` and `crop_fallback`, insert only the matching route section from `portrait-routes.md`. For `treatment_only`, insert only the transferable core from `transformation-fallbacks.md`; do not borrow an exact route's pose or social cues.

## Visual comparison and correction

Inspect source and result side by side using `quality-check.md`. The source, not the first generated result, is authoritative.

If a hard failure occurs, make at most one corrective edit:

```text
Re-edit from Image 1. Correct only: <named failed checks>.
Restore and preserve: <source-grounded identity and structure that drifted>.
Keep the previously declared crop, background, and treatment only where they passed.
Do not introduce any new change.
```

If the tool accepts both images, label the failed result as a diagnostic reference only. If it accepts one image, start again from the original source; never recursively edit the failed output alone.
