import numpy as np 
from scipy.integrate import odeint # для решения дифюуравнений
import matplotlib.pyplot as plt

#определение переменной величины
x = np.arange(-5,5,0.01)

#определение функции для системы диф.уравнений
def diff_func(o, x): # z - изменяемая величина для системы(z = кортеж)
    y, z = o# Указание изменяемых функций, через z

    # Первое уравнение системы
    dy_dx = y ** 2 *z
    # Второе уравнение системы
    dz_dx = z/x + 0.01 - y * z**2
    return dy_dx, dz_dx

y0  = 1
z0 = -3
o0 = y0, z0

# Решаем систему диф. уравнений
sol = odeint(diff_func, o0, x)

# Строим решение в виде графика
plt.plot(x, sol[:, 0], 'b', label='y(x)')
plt.plot(x, sol[:, 1], 'r', label='z(x)')

plt.legend()
plt.savefig('fig_3.png')