from typing import Type
# solution for 8.4.3
from scipy import integrate
import sympy
import math

h = 0.5
# actual integration
t = sympy.Symbol('t')
z = t ** (1/3)
intgral = sympy.integrate(z, (t, 0, 1))
actual_area = (h ** 4) * intgral 
print("acutal area:", actual_area)

for i in [2, 3, 4]:
    f = lambda a : a ** (1/3)
    guas_integral = integrate.fixed_quad(func=f, a=0, b=1, n=i)[0]
    guas_area = (h ** 4) * guas_integral
    error = math.fabs(actual_area - guas_area)
    print("n =", i , ",guas area=", actual_area  ,",error =", error)


# finding order of accuracy of guad quadrature of order 2 
hs = [0.01, 0.02, 0.05, 0.1, 0.2]
errors = []
f = lambda a : a ** (1/3)

# actual area
t = sympy.Symbol('t')
z = t ** (1/3)
intgral = sympy.integrate(z, (t, 0, 2))
actual_area = intgral

# using guas quadrature
for h in hs:
    guas_integral = 0
    for i in range(int(2 / h)):
        guas_integral += integrate.fixed_quad(func=f, a=i*h, b=(i+1)*h, n=2)[0]
    guas_area = guas_integral
    error = math.fabs(actual_area - guas_area)
    print(error, h)
    print(math.log(error, h))
    errors.append(error)

exit(0)


orders = []

for i in range(len(hs)):
    for j in range(len(hs)):
        if i != j:
            hi = hs[i]
            hj = hs[j]
            ei = errors[i]
            ej = errors[j]
            print(math.log(ei/ej, hi/hj))
