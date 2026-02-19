import numpy as np 
from scipy.integrate import odeint # для решения дифюуравнений
import matplotlib.pyplot as plt

#определение переменной величины
x = np.arange(1,3,0.01)

#определение функции для системы диф.уравнений
def diff_func(z, x): # z - изменяемая величина для системы(z = кортеж)
    y, omega = z # Указание изменяемых функций, через z

    # Первое уравнение системы
    dy_dx = omega
    # Второе уравнение системы
    domega_dx = omega * np.sin(y) - 3 * x * y - 5
    return dy_dx, domega_dx

y0  = 0.01
omega0 = 0.05
#начально езначение
z0=y0, omega0



# Решаем систему диф. уравнений
sol = odeint(diff_func, z0, x)

# Строим решение в виде графика
plt.plot(x, sol[:, 0], 'b', label='y(x)')
plt.plot(x, sol[:, 1], 'r', label='omega(x)')

plt.legend()
plt.savefig('fig_1.png')