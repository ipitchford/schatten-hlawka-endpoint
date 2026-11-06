# Finite verification and replay scope

The written proofs, not the finite scripts, support the universal asymptotic
claims. Recorded bounded repair replay on 6 November 2026 ran both checkers and
the guard suite once in normal mode and once with Python -O. All six executions
exited with code 0. This was an isolated producer-side run, not an unaffiliated reproduction
or a final frozen-archive replay.

## Coverage

| Check | Recorded scope | Evidence type |
|---|---|---|
| verify.py projector identities | 3 rational parameter instances | Exact Fraction arithmetic |
| verify.py norm identities | 72 (p,t) pairs, including t=1 | Floating SVD/formula agreement within 2e-12 |
| verify.py endpoint tables | 8 epsilon values, 90-digit Decimal; 4 trace endpoint values | Numerical; scaled residual sanity bound below 2 |
| reviewer_check.py projectors | 3 different rational instances | Exact Fraction arithmetic |
| reviewer_check.py norm identities | 25 pairs | Floating agreement within 1e-12 |
| reviewer_check.py endpoint tables | 7 epsilon values through 1e-40, 180-digit mpmath | Numerical scaled residual check |
| reviewer_check.py stationary points | 5 epsilon values | Numerical bracket/root/residual checks |
| test_guards.py | 12 semantic negative controls and 3 positive exact cases per mode | Intended guard-path checks |

The added correction_plus_3_over_8 column is only a numerical comparison with the
logarithmic location correction. Its agreement is not used to prove that correction.

Guard controls require PROJECTOR, TOTAL_SUM, MIXED_TRACE, MIXED_DETERMINANT,
SVD_IDENTITY, DECIMAL_REMAINDER, DECIMAL_DENOMINATOR, STATIONARY_RESIDUAL,
DOMAIN_NONFINITE, DOMAIN_EXPONENT, DOMAIN_PARAMETER and MATRIX_NONFINITE,
respectively. A wrong rejection code or an accepted mutation fails the suite.
No scientific verdict uses Python assert; -O must not remove acceptance criteria.

## Replay and retained records

Follow the six commands in README.md in fresh separate copies. verify.py writes
checks/results.json and checks/verification_log.txt; reviewer_check.py and
test_guards.py print JSON. Save stdout/stderr externally when retaining a replay.
Scripts use no network. NumPy 2.4.4 and mpmath 1.3.0 were used with Python 3.13.5.
The publisher retains the repair receipt and complete logs privately, bound by
source and output hashes; they are not silently relabelled as final archive evidence.

No finite table proves an O remainder, universal matrix identity, unrestricted
optimality or novelty. Numerical root residuals are not rigorous root enclosures.
