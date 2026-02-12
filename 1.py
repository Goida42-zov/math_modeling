import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def bacteria_function(N, t, k):
    return k * N
N0 = 10
k = 0.05
t_10x = np.log(10) / k
t = np.linspace(0, t_10x * 1.5, 1000)

N_t = odeint(bacteria_function, N0, t, args=(k,))

plt.figure(figsize=(10, 6))
plt.plot(t, N_t[:, 0], label='N(t)')
plt.axhline(y=10 * N0, color='r', linestyle='--')
plt.axvline(x=t_10x, color='g', linestyle=':')

plt.xlabel('t')
plt.ylabel('N')
plt.title('Bacterial Growth')
plt.legend()
plt.grid(True)

plt.savefig('bacteria_plot.png')
print(f"Time to 10x: {t_10x}")