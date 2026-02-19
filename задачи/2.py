import numpy as np
from scipy.integrate import odeint, trapezoid
import matplotlib.pyplot as plt

def model(I, t, k):
    return -k * I

I0 = 1000
k = 0.08
t_years = 4

t = np.linspace(0, t_years, 100)
I_t = odeint(model, I0, t, args=(k,))

# Используем trapezoid вместо trapz
total_investment = trapezoid(I_t.ravel(), t)

plt.figure(figsize=(8, 5))
plt.plot(t, I_t)
plt.fill_between(t, I_t.ravel(), color='skyblue', alpha=0.3)
plt.grid(True)
plt.show()

print(f"Объем за {t_years} года: {total_investment:.4f}")
plt.savefig('for2')