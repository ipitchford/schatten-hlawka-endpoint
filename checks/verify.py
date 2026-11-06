#!/usr/bin/env python3
"""Finite checks for the Schatten--Hlawka endpoint note.

Run from any directory: python3 checks/verify.py
Requires NumPy for the independently evaluated singular-value checks.
No finite computation in this file proves the asymptotic theorem.
"""

from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
import json
import platform
from guards import require, finite, domain
import numpy as np

ROOT = Path(__file__).resolve().parent.parent


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]


def exact_checks():
    records = []
    for k in (2, 3, 4):
        t = Fraction(1, k*k+1)
        a, b = 1-t, k*t
        x = [[a, b], [b, t]]
        y = [[a, -b], [-b, t]]
        z = [[Fraction(0), Fraction(0)], [Fraction(0), -2*t]]
        require(matmul(x, x) == x and matmul(y, y) == y, 'PROJECTOR')
        total = [[x[i][j]+y[i][j]+z[i][j] for j in range(2)] for i in range(2)]
        require(total == [[2 * a, 0], [0, 0]], 'TOTAL_SUM')
        xz = [[x[i][j]+z[i][j] for j in range(2)] for i in range(2)]
        require(xz[0][0] + xz[1][1] == 1 - 2 * t, 'MIXED_TRACE')
        require(xz[0][0] * xz[1][1] - xz[0][1] * xz[1][0] == -2 * a * t, 'MIXED_DETERMINANT')
        require(1 + 1 + 2 * t - 2 * a == 4 * t, 'TRIPLE_EXACT')
        records.append({"t": str(t), "X": [[str(v) for v in row] for row in x],
                        "triple_deficit": str(4*t), "status": "PASS (exact Fraction arithmetic)"})
    return records


def norm_p(a, p):
    finite(p,'NORM_EXPONENT_NONFINITE')
    require(p>=1,'NORM_EXPONENT')
    require(np.isfinite(a).all(),'MATRIX_NONFINITE')
    s = np.linalg.svd(a, compute_uv=False)
    return float(np.sum(s**p)**(1/p))


def svd_checks():
    records = []
    max_abs_error = 0.0
    for p in (1.0, 1.001, 1.01, 1.1, 1.5, 2.0, 3.0, 10.0):
        for t in (0.001, 0.01, 0.1, 0.2, 0.4, 0.5, 0.75, 0.9, 1.0):
            a, b = 1-t, np.sqrt(t*(1-t))
            x = np.array([[a, b], [b, t]])
            y = np.array([[a, -b], [-b, t]])
            z = np.diag([0.0, -2*t])
            norms = [norm_p(m, p) for m in (x, y, z)]
            numerator = sum(norms)-norm_p(x+y+z, p)
            denominator = 2*sum(norms)-sum(norm_p(m, p) for m in (x+y, x+z, y+z))
            d = np.sqrt(1+4*t-4*t*t)
            u, v = (d+1-2*t)/2, (d-1+2*t)/2
            formula = 4+4*t-2*((1-t)**p+t**p)**(1/p)-2*(u**p+v**p)**(1/p)
            err = max(abs(numerator-4*t), abs(denominator-formula))
            max_abs_error = max(max_abs_error, err)
            require(err < 2e-12, 'SVD_IDENTITY')
            require(denominator > 0, 'POSITIVE_DENOMINATOR')
            ratio = numerator/denominator
            if p == 2.0:
                require(ratio <= 1 + 2e-12, 'HILBERT_SANITY')
            records.append({"p": p, "t": t, "ratio": ratio, "max_abs_identity_error": err})
    return {"cases": len(records), "maximum_absolute_identity_error": max_abs_error,
            "p2_sanity": "All nine ratios <= 1 within 2e-12", "records": records}


def decimal_pow(x, p):
    return (p*x.ln()).exp()


def decimal_ratio(eps, t):
    p = Decimal(1)+eps
    domain(p,t)
    require(eps>0,'POSITIVE_EPSILON')
    d = (1+4*t-4*t*t).sqrt()
    u, v = (d+1-2*t)/2, (d-1+2*t)/2
    def f(x, y):
        return decimal_pow(decimal_pow(x, p)+decimal_pow(y, p), 1/p)
    denominator = 4+4*t-2*f(1-t, t)-2*f(u, v)
    require(denominator > 0, 'DECIMAL_DENOMINATOR')
    return 4*t/denominator


def high_precision_checks():
    with localcontext() as context:
        context.prec = 90
        K = 3+Decimal('1.5')*(Decimal(4)/3).ln()-Decimal(2).ln()
        records = []
        for power in (2, 3, 4, 5, 6, 8, 10, 12):
            eps = Decimal(10)**(-power)
            t = Decimal('0.75')*eps
            log = (1/eps).ln()
            ratio = decimal_ratio(eps, t)
            scaled = eps*log*ratio
            second = (1/ratio-Decimal('1.5')*eps*log)/eps
            residual = (1/ratio-Decimal('1.5')*eps*log-K*eps)/(eps*eps*log*log)
            finite(residual,'DECIMAL_REMAINDER_NONFINITE')
            require(abs(residual)<2,'DECIMAL_REMAINDER')
            records.append({"epsilon": str(eps), "t": str(t), "ratio": str(ratio),
                            "scaled_ratio": str(scaled), "second_coefficient": str(second),
                            "remainder_over_epsilon2_log2": str(residual)})
        # Separate endpoint identity, using a rationalised expression to avoid cancellation.
        endpoint = []
        for power in (2, 4, 8, 12):
            t = Decimal(10)**(-power)
            d = (1+4*t-4*t*t).sqrt()
            e_one = 4*t/(1+2*t+d)
            e_one_direct = (1+2*t-d)/(2*t)
            require(abs(e_one - e_one_direct) < Decimal('1e-60'), 'TRACE_ENDPOINT')
            endpoint.append({"t": str(t), "t_times_trace_ratio": str(t/e_one)})
        return {"decimal_precision": context.prec, "K": str(K), "endpoint_rows": records,
                "trace_endpoint_rows": endpoint}


def main():
    result = {"python": platform.python_version(), "numpy": np.__version__,
              "scope": "Finite algebraic and numerical checks only; not a proof certificate.",
              "exact_projectors": exact_checks(), "svd": svd_checks(),
              "high_precision": high_precision_checks()}
    output = ROOT/'checks'/'results.json'
    output.write_text(json.dumps(result, indent=2)+'\n')
    lines = ['Verification run: PASS', f'Python {result["python"]}; NumPy {result["numpy"]}',
             'Exact rational projector instances: 3 PASS',
             f'SVD identity checks: {result["svd"]["cases"]} PASS',
             f'Maximum absolute SVD/formula discrepancy: {result["svd"]["maximum_absolute_identity_error"]:.3e}',
             result['svd']['p2_sanity'], 'Decimal arithmetic: 90 significant digits',
             f'K = {result["high_precision"]["K"]}', '',
             'epsilon | R at t=0.75 epsilon | epsilon log(1/epsilon) R | second coefficient']
    for row in result['high_precision']['endpoint_rows']:
        lines.append(f'{row["epsilon"]} | {float(row["ratio"]):.10g} | '
                     f'{float(row["scaled_ratio"]):.10f} | {float(row["second_coefficient"]):.10f}')
    lines += ['', 'Limit targets: scaled ratio 2/3; second coefficient K.',
              'Trace sanity check: t R_1(t) approaches 1/2.',
              'These checks do not prove asymptotics or establish global optimality.']
    log = '\n'.join(lines)+'\n'
    (ROOT/'checks'/'verification_log.txt').write_text(log)
    print(log)


if __name__ == '__main__':
    main()
