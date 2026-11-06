"""Optimization-safe finite-diagnostic rejection codes; not proof certificates."""
import math

class VerificationError(RuntimeError):
    def __init__(self, code):
        self.code=code
        super().__init__(code)

def require(condition, code):
    if not condition: raise VerificationError(code)

def finite(value, code='NONFINITE'):
    try: ok=math.isfinite(value)
    except (TypeError,ValueError,OverflowError): ok=False
    require(ok,code)

def domain(p,t):
    finite(p,'DOMAIN_NONFINITE'); finite(t,'DOMAIN_NONFINITE')
    require(p>=1,'DOMAIN_EXPONENT')
    require(0<t<1,'DOMAIN_PARAMETER')
