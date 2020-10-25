from __init__ import *

# Testing
a = Symbol('a')
print(simplify(2 * (a + 1 + 3*a))) # 8 * a + 2
print(simplify(3*a)) # 3 * a + 0
print((2*a + 5 + (3*a + (2 * a + 3)))) # 7 * a + 8
print((a*a + 1) * 2 + 2*a) # 2 * a^2 + 2 + 2 * a
print(a * (a + 3) * 3) # 3 * a^2 + 9 * a
print(solve((5*a + 1) / 2 + (2 * a + 1) / 3, 2-a)) # 7/25
print(solve(a/2 + a/3, Fraction(1, 4))) # 3/10
print(solve(Add([1, 2, 3, a, a, a, a]), Add([5, 2]))) # 1/4
print(solve(a, 0)) # 0
print(solve(a**2 + 3*a + 2, 0)) # [-1. -2]
print(solve(a**2 - 25)) # [5, -5]
print(solve(Fraction(3, 1) * (a + 3) + 2)) # -11/3
print(solve(a**2 + 7*a + 6, 0)) # [-1, -6]