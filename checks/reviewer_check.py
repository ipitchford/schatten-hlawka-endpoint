"""Independent finite checks for the endpoint note; not a proof certificate."""
import json
import math
import platform
import time
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp
from guards import require, finite, domain
import numpy as np

started = time.monotonic()

def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

exact_count = 0
for r in [Q(1,7), Q(1,3), Q(2,5)]:
    c, s = (1-r*r)/(1+r*r), 2*r/(1+r*r)
    t, a = s*s, c*c
    X = [[a,c*s],[c*s,t]]
    Y = [[a,-c*s],[-c*s,t]]
    Z = [[Q(0),Q(0)],[Q(0),-2*t]]
    require(matmul(X, X) == X and matmul(Y, Y) == Y, 'REVIEW_PROJECTOR')
    require(X[0][0] + X[1][1] == 1, 'REVIEW_TRACE')
    require([[X[i][j] + Y[i][j] + Z[i][j] for j in range(2)] for i in range(2)] == [[2 * a, Q(0)], [Q(0), Q(0)]], 'REVIEW_TOTAL')
    exact_count += 1

worst_triple = worst_pair = 0.0
svd_count = 0
for t in [0.001,0.01,0.1,0.3,0.49]:
    a = 1-t
    X = np.array([[a,math.sqrt(a*t)],[math.sqrt(a*t),t]])
    Y = np.array([[a,-math.sqrt(a*t)],[-math.sqrt(a*t),t]])
    Z = np.diag([0.,-2*t])
    d = math.sqrt(1+4*t-4*t*t)
    u,v = (d+1-2*t)/2, (d-1+2*t)/2
    for p in [1.0001,1.01,1.5,2.,8.]:
        N = lambda A: np.sum(np.linalg.svd(A,compute_uv=False)**p)**(1/p)
        sizes = [N(X),N(Y),N(Z)]
        triple = sum(sizes)-N(X+Y+Z)
        pair = 2*sum(sizes)-N(X+Y)-N(X+Z)-N(Y+Z)
        f = lambda x,y: (x**p+y**p)**(1/p)
        expected_pair=4+4*t-2*f(a,t)-2*f(u,v)
        worst_triple=max(worst_triple,abs(triple-4*t))
        worst_pair=max(worst_pair,abs(pair-expected_pair))
        require(pair > 0, 'REVIEW_POSITIVE')
        require(abs(triple - 4 * t) < 1e-12, 'REVIEW_TRIPLE')
        require(abs(pair - expected_pair) < 1e-12, 'REVIEW_PAIR')
        svd_count += 1

mp.mp.dps=180
asymptotic=[]
for k in [2,4,8,12,20,30,40]:
    eps=mp.mpf(10)**(-k)
    t=mp.mpf(3)*eps/4
    p=1+eps
    d=mp.sqrt(1+4*t-4*t*t)
    u=(d+1-2*t)/2
    v=2*t*(1-t)/u
    F=lambda x,y: (x**p+y**p)**(1/p)
    reciprocal=(2+2*t-F(1-t,t)-F(u,v))/(2*t)
    L=mp.log(1/eps)
    K=3+mp.mpf('1.5')*mp.log(mp.mpf(4)/3)-mp.log(2)
    approx=mp.mpf('1.5')*eps*L+K*eps
    ratio_scaled=eps*L/reciprocal
    remainder_scaled=(reciprocal-approx)/(eps**2*L**2)
    require(reciprocal > 0, 'ASYMPTOTIC_POSITIVE')
    require(abs(remainder_scaled) < 2, 'ASYMPTOTIC_REMAINDER')
    asymptotic.append({
        'epsilon':str(eps),
        'scaled_ratio':mp.nstr(ratio_scaled,18),
        'remainder_over_eps2_log2':mp.nstr(remainder_scaled,18),
    })

location=[]
for k in [2,4,8,12,20]:
    eps=mp.mpf(10)**(-k)
    p=1+eps
    def energy_derivative(t):
        domain(p,t)
        d=mp.sqrt(1+4*t-4*t*t)
        dt=(2-4*t)/d
        u=(d+1-2*t)/2
        v=2*t*(1-t)/u
        ut=(dt-2)/2
        vt=(dt+2)/2
        def norm_and_derivative(x,y,xt,yt):
            S=x**p+y**p
            return S**(1/p),S**(1/p-1)*(x**(p-1)*xt+y**(p-1)*yt)
        A,At=norm_and_derivative(1-t,t,-1,1)
        B,Bt=norm_and_derivative(u,v,ut,vt)
        numerator=2+2*t-A-B
        return ((2-At-Bt)*t-numerator)/(2*t*t)
    lo=eps/4
    hi=eps*mp.mpf('1.5')
    require(energy_derivative(lo) < 0 < energy_derivative(hi), 'STATIONARY_BRACKET')
    root=mp.findroot(energy_derivative,(lo,hi),solver='anderson')
    require(0 < root < 1, 'STATIONARY_DOMAIN')
    require(abs(energy_derivative(root)) < mp.mpf('1e-100'), 'STATIONARY_RESIDUAL')
    location.append({
        'epsilon':mp.nstr(eps,10),
        'stationary_t_over_epsilon':mp.nstr(root/eps,18),
        'location_error_over_eps2_log':mp.nstr((root-mp.mpf(3)*eps/4)/(eps**2*mp.log(1/eps)),18),
        'correction_plus_3_over_8':mp.nstr((root-mp.mpf(3)*eps/4)/(eps**2*mp.log(1/eps))+mp.mpf(3)/8,18),
    })

report={
    'status':'All specified finite checks passed; no unrestricted theorem certified.',
    'python':platform.python_version(),
    'numpy':np.__version__,
    'mpmath':mp.__version__,
    'exact_projector_cases':exact_count,
    'svd_cases':svd_count,
    'max_absolute_triple_error':worst_triple,
    'max_absolute_pair_error':worst_pair,
    'mpmath_decimal_precision':mp.mp.dps,
    'asymptotic_cases':asymptotic,
    'stationary_location_cases':location,
    'elapsed_seconds':time.monotonic()-started,
}
print(json.dumps(report,indent=2))
