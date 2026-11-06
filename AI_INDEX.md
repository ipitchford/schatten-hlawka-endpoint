# Reader and machine index

Start with [paper.md](paper.md), Section 1, for the question and the distinction between a necessary lower bound and a sufficient upper bound. Section 2 gives the inherited matrices. Sections 3–5 prove the endpoint rate and family optimum; Sections 5.1–6 give the extensions. The proofs are self-contained apart from the stated background and attribution.

| Question | Entry point | Evidence boundary |
|---|---|---|
| What is claimed? | [CLAIMS.md](CLAIMS.md), SH-01–07 | Exact quantifiers and family versus unrestricted scope. |
| Why does the lower bound hold? | [paper.md](paper.md), Theorem 1 and Lemma 2 | Analytic exponent expansion with a small-argument remainder factor. |
| Could another scale within this family do better? | [paper.md](paper.md), Theorem 3 | Every global maximizer is localized analytically; no numerical search is substituted. |
| What is the corrected maximizing scale? | [paper.md](paper.md), Corollary 4 | Uniform over maximizers, not a uniqueness theorem. |
| What changes with cancellation amplitude? | [paper.md](paper.md), Proposition 6 | Exact p-dependent numerator; fixed z and fixed c only. |
| What is inherited? | [SOURCES.md](SOURCES.md) | Pinned construction, original problem, endpoint history and bounded novelty comparison. |
| What remains open or unchecked? | [LIMITATIONS.md](LIMITATIONS.md) | Unrestricted upper rate, moving amplitudes, uniqueness, formal verification and independent reproduction. |
| What can be computationally inspected? | [checks/verify.py](checks/verify.py), [checks/reviewer_check.py](checks/reviewer_check.py) | Finite diagnostics only; consult the verification record for actual run status. |

Dependencies: SH-01 supplies the ratio; Lemma 2 and SH-01 support SH-02. The differentiated expansion and global localization support SH-03. SH-04 and SH-05 depend on SH-02–03. SH-06 uses a separate fixed-amplitude reduction and Lemma 2; SH-07 is coefficient optimization within SH-06's quantifiers. None supplies an unrestricted upper bound.

No empirical dataset is used. Do not interpret a checker filename, a source repository containing Lean, or AI review as evidence of a formally certified or independently reproduced theorem.
