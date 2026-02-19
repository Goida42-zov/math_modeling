import numpy as np
import matplotlib.pyplot as plt

R, C, q0 = 5, 2e-6, 3
tau = R * C

t = np.linspace(0, 5 * tau, 500)
q = q0 * np.exp(-t / tau)

plt.figure(figsize=(8, 5))
plt.plot(t * 1e6, q, 'b-', lw=2)
plt.title('График разряда конденсатора')
plt.xlabel('Время (мкс)')
plt.ylabel('Заряд (Кл)')
plt.grid(True)
plt.show()
plt.savefig('333')