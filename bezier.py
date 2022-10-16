# Solution to 8.3.1
from sympy import *; import math

def distance_bezier(C, W, x):
    # bezier function
    def bez(n,v,t):
        return math.comb(n, v) * ((1 - t) ** (n - v)) * (t ** v)

    # ith component of r(t): r_i(t)
    def ri(i, t):
        numer = 0; denom = 0
        for v in range(N + 1): 
            numer += C[v][i] * W[v] * bez(N,v,t)
        for v in range(N + 1):
            denom += W[v] * bez(N, v,t)
        return numer / denom

    t = Symbol('t')
    r1 = ri(0, t); r2 = ri(1, t);    # r(t) = (r1(t), r2(t))
    r1d = diff(r1); r2d = diff(r2)   # derivate of components of r(t)

    # distance b/w x and (r1(tv), r2(tv))
    def d2(x, tv):
        r1t = r1.subs('t', tv)
        r2t = r2.subs('t', tv)
        return math.dist(x, (r1t, r2t))

    # find distance b/w x and the given bezier curve
    # phi(t) = (x - r(t)) * r'(t) 
    # condition for minimum distance phi(t) = 0
    phi = (x[0] - r1) * r1d + (x[1] - r2) * r2d  
    # ts are solutions for phi(t) = 0 that lie in (0, 1) and the end points t=0 and t=1
    ts = [t for t in solve(phi) if t.is_real and float(t) > 0.0 and float(t) < 1.0] + [0, 1]
    # distances for the found solutions
    ds = [d2(x, t) for t in ts]
    # return the minimum distance
    return min(ds)

# Example of using function
# given parameters, can be changed to anything to provide input to the function 
N = 2
C = [(3, 0), (0, 0), (0, 2)]
W = [1,2,3]
print(distance_bezier(C, W, (1, 1)))
