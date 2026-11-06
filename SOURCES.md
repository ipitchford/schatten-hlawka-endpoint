# Sources, attribution and bounded novelty comparison

Sources were compared on 6 November 2026. The contribution asserted is quantitative analysis near p=1 of an inherited construction, not discovery of the construction or the endpoint obstruction. No absolute priority guarantee is made.

## Original problem

Audenaert and Kittaneh, *Problems and conjectures in matrix and operator inequalities*: [arXiv:1201.5232v3, Section 8.2, Problem 7, equation (48)](https://arxiv.org/html/1201.5232v3#S8.SS2). The published 2017 version in *Études opératorielles*, Banach Center Publications 112, numbers the problem as Problem 6 in Section 8.2. The question concerns unpowered norm deficits of complex rectangular matrices. It records the Hilbert benchmark C₂=1; it does not state the coupled near-one expansion proved here.

## Inherited construction and nearby results

Ezzeri Esa, *hlawka-schatten*, pinned commit `1829591140522193a81ae721330e4d775c81123e`:

- [HlawkaSchatten/TraceEndpoint.lean](https://github.com/savarin/hlawka-schatten/blob/1829591140522193a81ae721330e4d775c81123e/HlawkaSchatten/TraceEndpoint.lean): definitions `traceEndpointX`, `traceEndpointY`, `traceEndpointZ` at lines 84–91; identities `traceEndpoint_tripleGap` and `traceEndpoint_pairGapSum` beginning at lines 206 and 217; endpoint obstruction `no_hlawkaConstant_schattenPNorm_one_fin2` beginning at line 255. The substitution is source s=√t and source c=√(1−t). This is the same matrix construction. The present general-p singular-value calculation and asymptotic analysis are not covered by that attribution as formally verified new results.
- [HlawkaSchatten/ScalarRatio.lean](https://github.com/savarin/hlawka-schatten/blob/1829591140522193a81ae721330e4d775c81123e/HlawkaSchatten/ScalarRatio.lean): definitions at lines 23–38 and compactification/bounds at lines 344–363, 500–542 and 600–608. Its scalar Bregman-to-Mazur quotient is distinct from the projector ratio R_p(t). Fixed-p compactness establishes positive finite comparison constants, not the coupled family asymptotics here.
- [BLUEPRINT.md](https://github.com/savarin/hlawka-schatten/blob/1829591140522193a81ae721330e4d775c81123e/BLUEPRINT.md), “Interior existence and endpoints” and “Sharp diagonal constant (p ≥ 256)”: the former reports interior existence; the latter concerns a different three-coordinate cyclic diagonal family at large p. Neither is asserted here as a newly established result. The full formal dependency graph was not compiled or audited for this note.

The repository's current head was also checked (`5eb5b1b665c566ddba25f1597ba2d30a54cafa07`); this was not an exhaustive review of branches or related projects.

M. J. Colbrook, [MI-25 trace-norm endpoint solution](https://github.com/ajt60gaibb/OpenProblemsInNLA/blob/main/matrix-inequalities-and-norms/MI-25/solution.tex), dated 11 September 2026, Theorem 1.1: a distinct real rectangular construction at fixed p=1. Its endpoint ratio is not a joint p↓1 statement, even though a coefficient 2/3 appears in that calculation. The [living MI-25 record](https://github.com/ajt60gaibb/OpenProblemsInNLA/blob/main/matrix-inequalities-and-norms/MI-25/README.md) provides status and provenance, not independent certification by this note.

Seokbin Lee, [*Constructions and reductions on the Hornich–Hlawka inequality and its generalizations*, arXiv:2610.23785v1](https://arxiv.org/html/2610.23785v1), Section 4.1, Theorem 4.3: a coordinate-space reduction. It is not a reduction of arbitrary noncommuting Schatten triples to the two-dimensional family studied here.

## Search coverage and exclusions

The search combined Schatten/Hlawka/endpoint, Hlawka/2/3/epsilon, Schatten/Hlawka/logarithmic, Hlawka/Schatten/p−1 and Hlawka/Schatten/3/4 terms, alongside an Evidence Press site search. The current public OpenAI mathematics contents index was searched for Hlawka, Hornich and Schatten; this was an index-level check, not a reading of every linked paper. The 252-release Evidence Press catalogue's authored Markdown and metadata were searched for Hlawka/Hornich. No matching endpoint-rate claim was located in those checks.

The search did not cover every archived attachment, all terminology variants, subscription MathSciNet or zbMATH records, every repository branch, or unpublished communications. Authors were not contacted. Search results and project summaries were treated as leads, not substitutes for inspected mathematical statements. The outcome supports a bounded non-duplication assessment, not proof that the result has never appeared anywhere.

No external papers or formal-library source files are redistributed in this package. Source attribution does not transfer their licences to the original prose or code here.
