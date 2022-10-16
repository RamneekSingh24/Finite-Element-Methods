# Solution to 8.3.2
from sympy import *; import math

x1 = Symbol('x1'); x2 = Symbol('x2')
def distance_boundary(w, p, x0, tol):
    global x1, x2
    # gradients
    dx1 = (-diff(w, x1))
    dx2 = (-diff(w, x2))
    # condition for minimum distance
    # p - (x1, x2) = lambda grad(w(x1,x2))
    # dx1 * (p(1) - x2) - dx2 * (p(0) - x1) = 0 (Note the 0 indexing of p here)
    z = dx1 * (p[1] - x2) - dx2 * (p[0] - x1)

    x2sols = solve(z, x2)
    x1x2realSols = set()

    # We directly use inbuilt solvers instead of newton method
    for x2sol in x2sols:
        x1s = solve(w.subs('x2', x2sol))
        x2s = [x2sol.subs('x1', x1) for x1 in x1s]
        for x1 in x1s:
            for x2 in x2s:
                if x1.is_real and x2.is_real:
                    x1x2realSols.add((x1, x2))

    best_x = ()
    best_d = 1e100
    # Find the minimum distance among the solutions
    for x in x1x2realSols:
        print(math.dist(x, p), x)
        if math.dist(x, p) < best_d:
            best_d = math.dist(x, p)
            best_x = x
    
    return best_x, best_d
            
# Example of using the function 
# given eqn
w = (x1 ** 4) - 4 * x1 ** 2 + x2 ** 2 - 1
# given point
p = (1,0)
(x, d) = distance_boundary(w, p, x0=(0, 1), tol=1e-10)
print(f"d={d}, x={x}")
print(f"d={d}, x={(x[0].evalf(), x[1].evalf())}")
