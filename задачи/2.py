import numpy as np 
from scipy.integrate import odeint # для решения дифюуравнений
import matplotlib.pyplot as plt

#определение переменной величины
t = np.arange(-1,1,0.01)
e = 2,7182
#определение функции для системы диф.уравнений
def diff_func(o, t): # z - изменяемая величина для системы(z = кортеж)
    y, x = o# Указание изменяемых функций, через z

    # Первое уравнение системы
    dx_dt = 3 *x - 2 * y + e ** 3 * t/e ** t + 1
    # Второе уравнение систем
    dy_dt = x - e ** 3*t/e**t + 1
    return dx_dt, dy_dt

y0  = -7
x0 = 5
t0 = y0, x0

# Решаем систему диф. уравнений
sol = odeint(diff_func, o0, t)

# Строим решение в виде графика
plt.plot(t, sol[:, 0], 'b', label='y(t)')
plt.plot(t, sol[:, 1], 'r', label='x(t)')

plt.legend()
plt.savefig('fig_4.png')