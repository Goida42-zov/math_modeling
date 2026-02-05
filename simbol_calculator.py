import math
print(math.sqrt(3)) # численное вычисление

import sympy as sym
print(sym.sqrt(3)) # СИМВОЛЬНОЕ ВЫЧИСЛЕНИЕ

print(2 * sym.sqrt(3))

x, y = sym.symbols('x, y')
expr = x + 2*y # выражение
print(expr)

print(expr + 1)

print(expr ** 2)
print(expr * x)

print(sym.sin(x**2) - sym.exp(-2*x) + sym.cos(sym.pi / x))
      

      # exp(e) - число Эйлера