# Scope and limitations

This is an AI-assisted, unrefereed mathematical note. Its main result is a necessary growth rate for dimension-independent Schatten–Hlawka constants near p=1. It is not a sufficient perturbation bound or an algorithm for bounding arbitrary matrix triples.

## Mathematical boundaries

- No matching unrestricted upper bound is proved. The true C_p may diverge faster than 1/[(p−1)log(1/(p−1))]. The coefficient K and optimizer describe the specified family, not an expansion or optimizer for C_p.
- The matrices are inherited from Esa's trace-endpoint construction. Trace-norm failure, interior finiteness, and the Hilbert benchmark are prior results, not contributions of this note. The lower-bound argument does not depend on independently certifying the reported interior finiteness theorem.
- The maximizing-parameter expansion holds uniformly over all maximizers of the original family for sufficiently small ε. It proves neither uniqueness nor a classification of every stationary point.
- The scale-loss formula is uniform only on each fixed compact interval of positive linear-scale parameters. It is not a general converse for near-maximizing sequences.
- In the amplitude comparison, z>0 and c>0 are fixed before ε tends to zero. Constants may depend on both. No uniform claim is made for z=z(ε), including amplitudes tending to zero or infinity or approaching two at an ε-dependent rate. For z≠2, optimization over every t is not established.
- The limits cannot be interchanged: at fixed p>1, R_p(t) tends to 2/3 as t tends to zero; the divergent ratio uses the joint limit t comparable to p−1.

## Evidence boundaries

The proofs are informal analytic proofs. No new theorem here has been formally verified in Lean or another proof assistant. Source-code inspection of a cited formal development does not constitute a replay of its complete dependency graph.

Finite rational checks establish their selected instances. Floating-point singular-value checks and high-precision asymptotic or stationary-point evaluations are numerical diagnostics, not rigorous interval enclosures or universal proofs. Near the endpoint, cancellation in the closed denominator demands particular care: quantities of order one are subtracted to obtain a much smaller deficit. Numerical evidence cannot exclude unsampled extrema; the written localization argument supplies the family-wide result.

AI-assisted internal checking is not external human refereeing or independent reproduction. Execution status and test coverage must be read from the accompanying verification record rather than inferred from the presence of scripts.

## Historical boundary

The bounded search described in [SOURCES.md](SOURCES.md) found no earlier statement of the claimed endpoint rate and family asymptotics. It cannot guarantee absolute originality across all published or unpublished work. The inherited construction and endpoint obstruction are explicitly attributed.
