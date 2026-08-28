# Evaluation Rubric

## Purpose

Evaluate observable behavior, not whether generated wording matches a template.

## Hard gates

A result fails immediately when:

- framing changes outside the declared safe inward-crop matrix;
- an inward crop changes head view, face visibility, expression category, or visible identity;
- a hidden face or body region is brought into view;
- the output contains more than one person;
- an exact route is claimed when the complete key is not `supported`;
- visible identity changes materially;
- clothing, accessories, held objects, or social identity are replaced by corpus-specific sitter styling;
- the result leaves the controlled-background formal-portrait domain.
- the image tool did not receive the source image as an edit target;
- the result is a text-generated lookalike rather than a source-conditioned edit;
- visible hands, clothing, accessories, objects, or face structure drift outside the declared crop;
- a general full-body input is tightened to waist-up merely to obtain an exact supported label;

## Scores

Use 0–4 for each applicable dimension.

### Structure preservation

- `4`: exact mode preserves the complete key, or crop fallback reaches the declared target while preserving every protected identity axis.
- `3`: target crop is correct with one noticeable but non-identity-bearing shift.
- `2`: target crop or one protected axis is ambiguous.
- `1`: an unauthorized structural axis clearly changed.
- `0`: hidden identity was invented or the result normalized into an unrelated portrait type.

### Transformation integrity

- `4`: only authorized crop, recentering, background, and tonal changes occur.
- `3`: one permitted change is slightly over-applied but identity remains intact.
- `2`: unnecessary information is removed or the target crop is weak.
- `1`: pose, view, or identity-bearing content changes.
- `0`: unseen face or anatomy is invented.

### Visible identity preservation

- `4`: all visible identity evidence remains consistent.
- `3`: recognizable with minor drift.
- `2`: recognizable but several features drift.
- `1`: weak resemblance.
- `0`: different person.

Mark `not_assessable` for facial identity when no face is visible; evaluate silhouette and visible features separately.

### Route fidelity

- `4`: matches every required rule and no negative constraint.
- `3`: one secondary route cue is weak.
- `2`: several route cues are generic.
- `1`: only a superficial black-and-white treatment remains.
- `0`: contradicts the selected route.

### Shared style fidelity

Score only evidence-backed shared rules. Do not reward unsupported mythology about Avedon.

### Technical integrity

Check anatomy, duplicate features, hands, clothing continuity, edge artifacts, unintended text, halos, background seams, and tonal damage.

### Source-conditioning integrity

- `4`: the supplied source is visibly authoritative for identity, pose, expression, clothing, hands, and all retained structure.
- `3`: clearly source-derived, with only minor non-identity texture drift.
- `2`: recognizable but one protected source attribute changed materially.
- `1`: resembles the source description more than the actual source image.
- `0`: text-only lookalike or different sitter.

## Pass rule

- no hard-gate failure;
- `structure_preservation = 4`, `transformation_integrity = 4`, and `source_conditioning_integrity = 4`;
- every other applicable dimension at least `3`;
- route and shared-style scores cite the evidence rules used.
