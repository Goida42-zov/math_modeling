#sups - из символа в число

import sympy as sym
x, y, z = sym.symbols(' x y z')
expr = sym.sin(x**2) - sym.exp(-2*x) + sym.cos(sym.pi / x)
expr_new = expr.subs(x, y) #заменяем x на y
print(expr_new)

expr_new = expr.subs(x, sym.pi)
print(expr_new)
expr_num = expr_new.evalf() # считает
print(expr_num)

expr_new = expr.subs(x, x**2)
print(expr_new)