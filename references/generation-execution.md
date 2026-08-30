# Generation Execution

Use this file after the source diagnosis, composition plan, target route, and identity constraints are known. It turns internal research labels into a short, visible, reference-conditioned edit instruction.

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

- Treat a simple crop as geometry, not generation. When a deterministic crop/canvas operation is available, use it before the style edit so retained sitter pixels are not re-synthesized. Keep the original source for comparison.
- First try inward cropping and recentering of visible source content. If that would cut protected sitter content, extend only the featureless controlled background on the cramped side. Never outpaint hidden face, hair, hands, feet, clothing, or body.
- Preserve the source orientation. Honor a user-specified ratio only when safe. Otherwise preserve the source ratio for purposeful asymmetry; for an accidentally imbalanced waist-up or three-quarter portrait, prefer portrait when every protected edge fits, square when it preserves more sitter information, and the source ratio when neither alternative is safe. Explain every crop or background-only extension to the image tool.
- For accidental side imbalance, name the edge to trim or extend and request balanced side space around the retained sitter. Do not merely say “improve the composition.”
- For excessive headroom, name the top trim and confirm that hair and head remain safely inside the frame. For a weak lower crop, name the intended body landmark and avoid major joints.
- For general frontal full-body fallback, place the lower edge at upper or mid-thigh, keep the head through thighs, and use `treatment_only`. Do not tighten to waist-up merely because that key is supported.
- For side, profile, over-shoulder, or back full-body fallback, use the same thigh-level target while preserving orientation.
- For face fragments, retain the same missing facial region and approximately the same face-to-frame dominance.

## Prompt compiler

Do not dump taxonomy, route keys, evidence labels, or every repository safeguard into the image prompt. They guide the agent, not the image model. Translate only the chosen action and relevant protections. Omit inapplicable negative constraints.

Keep the prompt in this order: edit target, identity protection, composition action, photographic treatment, then a short conditional negative list.

```text
Edit Image 1 into one formal black-and-white portrait. Image 1 is authoritative for this person's identity and all retained sitter content.

Preserve exactly: <visible facial geometry, head view, face visibility, expression, hair, eyewear, pose, retained hands, clothing, accessories, objects>.

Composition: <keep intentional asymmetry, or name the exact source edge trim / headroom trim / lower crop / background-only extension>. Place <the retained sitter relationship> with <balanced or intentionally directional> space. Do not alter the sitter to achieve placement.

Background and tone: remove location information and use <white or light-neutral seamless background>. Render neutral black-and-white with readable separation among skin, eyes, lips, hair, hands, and clothing. Use <route-appropriate broad descriptive light>; preserve source facial planes, highlight detail, shadow detail, pores, wrinkles, hair, garment texture, and natural asymmetry.

Do not: generate a new sitter; change face, gaze, expression, pose, or retained clothing; invent hidden anatomy or objects; beautify or smooth skin; add text, border, seam, halo, or duplicate person. <Add route-specific prohibition only when relevant.>

Output: one finished formal portrait edit; no collage, before/after panel, caption, or added text.
```

For `exact_route` and `crop_fallback`, translate only the applicable visual result from the matching route. For `treatment_only`, translate the transferable core plus the independent composition plan; do not borrow an exact route's pose or social cues. Mention IAW stereotypes only for an IAW edit or when the source makes that confusion likely.

## Execution priority

When instructions compete, preserve in this order:

1. visible identity and unseen-structure boundary;
2. sitter-authored head view, expression, gesture, clothing, and retained objects;
3. declared crop, recentering, headroom, and negative-space plan;
4. background isolation and tonal treatment;
5. optional presentation detail.

Style strength never justifies skipping the declared composition repair. Composition repair never justifies rebuilding the sitter.

## Visual comparison and correction

Inspect source and result side by side using `quality-check.md`. Compare composition and tone as separate passes. The source, not the first generated result, is authoritative.

If a hard failure occurs, make at most one corrective edit:

```text
Re-edit from Image 1. Correct only: <named failed checks>.
Restore and preserve: <source-grounded identity and structure that drifted>.
Keep the previously declared crop, background, and treatment only where they passed.
Do not introduce any new change.
```

If the tool accepts both images, label the failed result as a diagnostic reference only. If it accepts one image, start again from the original source; never recursively edit the failed output alone.
