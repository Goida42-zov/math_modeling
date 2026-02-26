import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Параметры задачи
g = 9.8
v0 = 15
alpha = np.radians(80)


t_flight = (2 * v0 * np.sin(alpha)) / g
frames = 100
t = np.linspace(0, t_flight, frames)


def move_func(z, t):
    x, vx, y, vy = z
    dx_dt = vx
    dvx_dt = 0
    dy_dt = vy
    dvy_dt = -g
    return dx_dt, dvx_dt, dy_dt, dvy_dt


x0 = 0
vx0 = v0 * np.cos(alpha)
y0 = 0
vy0 = v0 * np.sin(alpha)

z0 = [x0, vx0, y0, vy0]
sol = odeint(move_func, z0, t)


fig, ax = plt.subplots(figsize=(8, 5))
ball, = plt.plot([], [], 'o', color='r', markersize=8)
ball_line, = plt.plot([], [], '-', color='r', alpha=0.5)

max_x = v0**2 * np.sin(2*alpha) / g
max_y = (v0 * np.sin(alpha))**2 / (2 * g)

ax.set_xlim(0, max_x * 1.1)
ax.set_ylim(0, max_y * 1.1)
ax.set_xlabel('Дистанция (м)')
ax.set_ylabel('Высота (м)')
ax.set_title(f'Траектория)')
ax.grid(True)

def animate(i):
    ball.set_data([sol[i, 0]], [sol[i, 2]])
    ball_line.set_data(sol[:i, 0], sol[:i, 2])
    return ball, ball_line

ani = FuncAnimation(fig, animate, frames=frames, interval=30, blit=True)

ani.save('projectile_motion.gif', writer="pillow")