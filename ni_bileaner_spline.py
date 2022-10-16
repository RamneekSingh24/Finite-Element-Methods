# Solution to 8.4.1
from sympy import *

def bspline_linear(k, x):  # B-spline
    z = x - k
    s = Piecewise(
        (z, (0 <= z)  & (z <= 1)),
        (2 - z, (1 < z) & (z <= 2)),
        (0, True)
    )
    return s

x1 = Symbol('x1')
x2 = Symbol('x2')
z = Symbol('z')

ks = [(-1, -1), (0, -1), (-1, 0), (0, 0)]  # k indexes

# P_k, each is product of linear splines 
p_ks = [bspline_linear(k[0], x1) * bspline_linear(k[1], x2) for k in ks] 

# gamma_ks, integration over 0 <= x2 <= x1^2, 0 <= x1 <= 1 of the bilinear splines 
gamma_ks = [integrate(p, (x2, 0, x1**2), (x1, 0, 1)).evalf() for p in p_ks] 

print(ks)
print(gamma_ks)

print(sum([1/gamma for gamma in gamma_ks]))

