# Response to scientific and editorial review

6 November 2026. This document describes manuscript revisions, not external human referee approval. The candidate remains AI-assisted and unrefereed.

| Concern | Manuscript action | Boundary |
|---|---|---|
| Reader context and signposting | Section 1 explains triangle deficits, dimension-independent control, the Hilbert benchmark and the proof route before the main theorem. | No application-level error guarantee is claimed. |
| Inherited construction and endpoint history | Sections 1–2 name Esa's pinned definitions and trace identities, the parameter substitution, Colbrook's different earlier endpoint construction, and Lee's coordinate-space result. | General-p calculations and new asymptotics are not attributed to the predecessor's formal declarations. |
| Public presentation | Removed commissioning and internal evaluation prose, replacing it with mathematical scope and an early assurance disclosure. | No external endorsement is inferred. |
| Full parameter domain | Section 2 defines the family on the complete interval and explicitly handles the degenerate t=1 singular value and ratio. | Small-t estimates remain restricted to their stated ranges. |
| Uniform localization clarity | Section 5 states why epsilon log epsilon tending to zero makes the scale comparison valid. Original uniform proofs are retained. | No unproved uniqueness assertion is added. |
| Logarithmic location correction | Corollary 4 proves the coefficient −3/8 uniformly over all global family maximizers. | Only the maximizing location is sharpened. |
| Near-optimality explanation | Corollary 5 gives the compact-linear-scale loss (3/2)epsilon(x−1−log x), with a uniform remainder. | No converse for arbitrary near-maximizing sequences is claimed. |
| Broader fixed-amplitude check | Proposition 6 computes the exact general-p triple deficit and carries it through the expansion; the original amplitude uniquely maximizes the limiting coefficient among fixed positive amplitudes. | Moving amplitudes and all-scale optimization for other amplitudes are not covered. |
| Numerical conditioning and evidence hierarchy | Section 8 explains cancellation sensitivity, numerical versus exact evidence, and the noncommuting limits. | Numerical checks are not analytic proof or interval certification. |
| Executable guards | Manuscript does not assert repaired-checker completion. Companion checker repairs and replay receipts are separate release tasks. | The scientific proof is self-contained and does not depend on a numerical PASS label. |

The proposal to prove a matching unrestricted upper bound is not adopted as a routine revision: it requires control beyond the one-family calculation. Eventual uniqueness and explicit finite-epsilon remainder constants are also left unclaimed. Additional decimal checks alone would not settle any of these questions.

## Targeted verification requested

Review Corollary 4's uniform exponential and rational expansions, Corollary 5's compact-scale subtraction, and Proposition 6's corrected triple deficit and division error. The original Theorems 1 and 3 and their complete proofs are retained. Source and release checks remain distinct from these mathematical additions.
