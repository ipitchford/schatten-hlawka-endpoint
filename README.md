# An endpoint lower bound for Schatten–Hlawka constants

Anonymous · version 0.1.0-candidate · unrefereed, AI-assisted research.

How large must a constant be if it bounds the triangle deficit of three matrices
using their three pairwise deficits? This note studies what happens as the Schatten
exponent approaches the trace-norm endpoint. It analyzes an existing two-dimensional
projector construction, not arbitrary triples, to obtain a quantitative obstruction.

The main conclusion is

    liminf epsilon log(1/epsilon) C_(1+epsilon) >= 2/3.

The paper also determines the reciprocal optimum within that family to two terms
and refines the location of every maximizing parameter. Neither the exact general
constant nor a matching unrestricted upper bound is established. The construction
and prior finiteness results are attributed to their sources.

Start with [paper.md](paper.md), [CLAIMS.md](CLAIMS.md) and
[LIMITATIONS.md](LIMITATIONS.md). [AI_INDEX.md](AI_INDEX.md) maps the evidence;
[SOURCES.md](SOURCES.md) records attribution and source scope. See
[ASSURANCE.md](ASSURANCE.md) before interpreting computational checks.

Identifiers: reserved version DOI [10.5281/zenodo.23999268](https://doi.org/10.5281/zenodo.23999268),
concept identifier 23999267; intended repository
[ipitchford/schatten-hlawka-endpoint](https://github.com/ipitchford/schatten-hlawka-endpoint).
Reservation and an intended URL do not establish public availability.

## Reproduce the finite diagnostics

Use Python 3.13 and install the pinned dependencies from requirements.txt in your
own environment. Work in a fresh extracted copy: verify.py writes results.json
and verification_log.txt into checks/.

```sh
python -m pip install -r requirements.txt
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B checks/verify.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B checks/reviewer_check.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B checks/test_guards.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -O checks/verify.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -O checks/reviewer_check.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -O checks/test_guards.py
```

Run each mode in its own copy if retaining both outputs. The finite scripts must
exit successfully, and the negative suite must report all 12 intended guard IDs.
These are numerical/exact-instance diagnostics, not proof-assistant certificates.
Detailed scope and recorded repair-run results: [VERIFICATION.md](VERIFICATION.md).

Original prose/data are CC0-1.0; original code is MIT. Third-party cited research
is not redistributed or relicensed: [LICENSES.md](LICENSES.md).
