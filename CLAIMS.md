# Claim register

All logarithms are natural. Put ε=p−1>0 and L=log(1/ε). The constant C_p is defined over all finite complex rectangular triples in Section 1 of [the paper](paper.md), including triples whose pair-deficit sum is zero. The family ratio R_p and family supremum M_p are defined separately. A lower bound for C_p is not a usable upper estimate for arbitrary matrices.

| ID | Precise claim | Proof location and dependencies |
|---|---|---|
| SH-01 | For the inherited rank-one projector family, the triple deficit is 4t and the pair-deficit sum is D_p(t)=4+4t−2F_p(1−t,t)−2F_p(u(t),v(t)). For p>1 and 0<t≤1, D_p(t)>0 and R_p(t)=4t/D_p(t)≤C_p. | Section 2, equations (5)–(9); direct eigenvalue calculation. The matrices and trace-endpoint identities are inherited, not claimed as new. |
| SH-02 | For every fixed c>0, R_(1+ε)(cε)^−1=(3/2)εL+ε[2c−(3/2)log c+3/2−log 2]+O_c(ε²L²). Consequently liminf εL C_(1+ε)≥2/3, including the possibility C_(1+ε)=∞. | Theorem 1; Lemma 2 and Section 4. The small-argument factor in the exponent-derivative remainder is essential. |
| SH-03 | Over the entire original family 0<t≤1, the supremum M_(1+ε) is attained in (0,1) for sufficiently small ε. Its reciprocal is (3/2)εL+Kε+O(ε²L²), where K=3+(3/2)log(4/3)−log 2. | Theorem 3; controlled first-derivative remainder and localization of every minimizer. This is not an upper bound for C_p. |
| SH-04 | Every maximizing parameter in SH-03 satisfies t_ε=(3/4)ε−(3/8)ε²L+O(ε²), uniformly over the maximizing set. | Corollary 4, using Theorem 3's uniform localization and stationary equation. No uniqueness assertion. |
| SH-05 | For k in any fixed compact interval J⊂(0,∞), E_(1+ε)(kε)−M_(1+ε)^−1=(3/2)ε(x−1−log x)+O_J(ε²L²), x=4k/3 and E=1/R. | Corollary 5. The displayed leading loss vanishes only at k=3/4; this does not characterize arbitrary near-maximizing sequences. |
| SH-06 | Fix z>0 and c>0 independently of ε and replace Z_t by diag(0,−zt). With m=min(z,2), R_(1+ε,z)(cε)^−1=((1+z)/m)εL+B_z(c)ε+O_(z,c)(ε²L²), where B_z(c)=[2zc−(1+z)log c+(1+z)−z log z]/m. | Proposition 6; fixed-amplitude eigenvalue reduction and exponent estimates. |
| SH-07 | The limit εL R_(1+ε,z)(cε) is min(z,2)/(1+z). Among fixed positive amplitudes it is uniquely largest at z=2. For each fixed z, B_z(c) is uniquely minimized among fixed positive c at c=(1+z)/(2z). | Proposition 6; elementary differentiation of the coefficients after the fixed-parameter limit. Not an optimization over moving amplitudes or all scales for z≠2. |

For SH-06–07 the exact numerator is T_(p,z)=2+zt−F_p(2(1−t),|2−z|t). It equals 2min(z,2)t at p=1; at general p it is not that expression unless z=2. The ratio is T_(p,z)/D_(p,z), not a trace-endpoint numerator substituted at p>1.

The evidence for the universally quantified claims is the analytic proof. Exact finite arithmetic and numerical diagnostics are supporting checks, not formal certification or independent reproduction. See [limitations](LIMITATIONS.md) and [source attribution](SOURCES.md).
