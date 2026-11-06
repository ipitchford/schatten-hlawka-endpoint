"""Targeted semantic mutations of actual checker expressions, normal or -O."""
import contextlib, io, json
from pathlib import Path
from decimal import Decimal
import numpy as np
from guards import VerificationError, require, domain
R=Path(__file__).resolve().parent

def load(name,old=None,new=None):
    text=(R/name).read_text()
    if old is not None:
        require(text.count(old)==1,'MUTANT_TARGET_COUNT')
        text=text.replace(old,new)
    scope={'__name__':'guard_inspection','__file__':str(R/name)}
    with contextlib.redirect_stdout(io.StringIO()): exec(compile(text,str(R/name),'exec'),scope)
    return scope

def main():
    results=[]
    def rejection(label,code,action):
        try: action()
        except VerificationError as exc:
            require(exc.code==code,'WRONG_GUARD_'+label)
            results.append({'mutation':label,'intended_guard':code,'observed_guard':exc.code})
        else: raise RuntimeError('Mutation accepted: '+label)
    v=load('verify.py')
    require(len(v['exact_checks']())==3,'POSITIVE_FIXTURE')
    specs=[
      ('idempotence','a, b = 1-t, k*t','a, b = 1-t, 2*k*t','exact_checks','PROJECTOR'),
      ('total-sum','[Fraction(0), -2*t]','[Fraction(0), -3*t]','exact_checks','TOTAL_SUM'),
      ('mixed-trace','xz[0][0] + xz[1][1] == 1 - 2 * t','xz[0][0] + xz[1][1] == 1 - 3 * t','exact_checks','MIXED_TRACE'),
      ('mixed-determinant','== -2 * a * t','== -3 * a * t','exact_checks','MIXED_DETERMINANT'),
      ('svd-formula','formula = 4+4*t-2*','formula = 5+4*t-2*','svd_checks','SVD_IDENTITY'),
      ('asymptotic-coefficient',"K = 3+Decimal('1.5')", "K = 4+Decimal('1.5')",'high_precision_checks','DECIMAL_REMAINDER')]
    for label,old,new,function,code in specs:
        rejection(label,code,lambda old=old,new=new,function=function:load('verify.py',old,new)[function]())
    rejection('negative-denominator','DECIMAL_DENOMINATOR',lambda:load('verify.py','denominator = 4+4*t-2*f','denominator = -4+4*t-2*f')['decimal_ratio'](Decimal('.01'),Decimal('.0075')))
    rejection('stationary-residual','STATIONARY_RESIDUAL',lambda:load('reviewer_check.py',"abs(energy_derivative(root)) < mp.mpf('1e-100')","abs(energy_derivative(root)+1) < mp.mpf('1e-100')"))
    rejection('nan-parameter','DOMAIN_NONFINITE',lambda:domain(1.1,float('nan')))
    rejection('bad-exponent','DOMAIN_EXPONENT',lambda:domain(.5,.1))
    rejection('zero-parameter','DOMAIN_PARAMETER',lambda:domain(1.1,0))
    rejection('nan-matrix','MATRIX_NONFINITE',lambda:v['norm_p'](np.array([[float('nan')]]),2))
    print(json.dumps({'status':'passed','negative_controls':results,'positive_exact_cases':3,'boundary':'Intended rejection paths only; not proof or interval certification'},indent=2))
if __name__=='__main__': main()
