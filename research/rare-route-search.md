# Rare Route Search

Checked on 2026-08-27 and expanded on 2026-08-28. Only institutional or artist-foundation pages count as evidence.

## Tight head and partial visibility

| Work | Source | Observation | V1 use |
| --- | --- | --- | --- |
| Marian Anderson, 1955 | [Met](https://www.metmuseum.org/art/collection/search/270362) | tight horizontal crop, figure offset right, eyes closed, mouth open, top of head cropped | eligible after full annotation; not a strict half-face |
| Marcel Duchamp, 1958 | [Smithsonian NPG](https://npg.si.edu/object/npg_NPG.98.58) | tight head; fingers cover eyes and parts of face | review; occlusion route, not frame-edge fragment |
| Malcolm X, 1963 | [Avedon Foundation](https://www.avedonfoundation.org/the-work) | tight frontal head; sunglasses cover eyes | eligible tight-head evidence; not a half-face |
| Francis Bacon, 1979 | [Getty](https://www.getty.edu/art/collection/object/108GRQ) | diptych with a center divider | excluded from single-frame route evidence |

The focused expansion again found zero strict lateral half-face crops. Top-of-head crop, a large face, and object occlusion remain distinct from `face_detail`; see `v2-framing-search.md`.

## Frontal tight head

The exact key `formal_portrait_general|tight_head|frontal|full|none` now has seven route-eligible records: `AP-EXP-FND-05`, `AP-EXP-MUS-05`, `AP-EXP-MUS-17`, `AP-EXP-MUS-18`, `AP-EXP-GET-01`, `AP-EXP-GET-02`, `AP-EXP-GET-03`.

It remains `provisional`: only two records are from the mature 1969-onward method period, and the seven observations do not yet establish one stable mature-period background and lighting instruction.

## Full body

The focused expansion found zero eligible records with head through both feet in a single controlled-background formal portrait. `In the American West` standing portraits stop above the feet; full-body Foundation and museum examples found in the search belong to fashion, reportage, dance, environmental, or complex-prop contexts. The exact family remains `unsupported`.

## Profile

| Work | Source | Observation | V1 use |
| --- | --- | --- | --- |
| Gloria Vanderbilt, 1953 | [Avedon Foundation](https://www.avedonfoundation.org/the-work) | bust, three-quarter toward image right | eligible but not strict profile |
| Marella Agnelli, 1953 | [Avedon Foundation](https://www.avedonfoundation.org/the-work) | bust, near profile toward image right | eligible pre-mature evidence |
| Marella Agnelli in Profile | [Smithsonian NMAH](https://americanhistory.si.edu/collections/object/nmah_557143) | strict profile toward image right, controlled gray background | review; exact date not shown on page |

These records justified continued profile annotation but did not reach the V1 promotion gate. The completed corpus contains only one route-eligible strict-profile record.

## Over-shoulder and back view

- No eligible over-shoulder formal portrait was confirmed in the Foundation, Met, MoMA, Smithsonian/NPG, Smithsonian/NMAH, Getty, or Carter sources searched.
- [Rudolph Nureyev, 1961](https://npg.si.edu/object/npg_NPG.91.54) shows a full-body back/side dynamic dance pose with no visible face. It is negative evidence: outside the V1 formal, face-clear route boundary.

Exact-route status remains `face_fragment=unsupported`, `full_body=unsupported`, `over_shoulder=unsupported`, `back_view=unsupported`, `profile=unsupported`, `frontal_tight_head=provisional`. These labels prevent false exact-route claims; they no longer block generation because identity-safe inputs can use `crop_fallback` or `treatment_only`.
