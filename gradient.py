import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return 7*x**2 - 10*x*y + 7*y**2 - 4*x + 4*y - 8

def grad_fx(x, y):
    return 14*x - 10*y - 4

def grad_fy(x, y):
    return -10*x + 14*y + 4

x = np.linspace(-2, 2, 200)
y = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# 1) surface
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, linewidth=0, antialiased=True)
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('f(x,y)')
ax.set_title('Поверхность f(x,y)')
plt.show()
plt.savefig("surface.png")

# 2) gradient field (quiver)
GX = grad_fx(X, Y)
GY = grad_fy(X, Y)
step = 10
fig = plt.figure(figsize=(7,7))
plt.quiver(X[::step, ::step], Y[::step, ::step],
           GX[::step, ::step], GY[::step, ::step],
           angles='xy', scale_units='xy', scale=40)
plt.xlabel('x'); plt.ylabel('y'); plt.title('Градиент ∇f(x,y)')
plt.axis('equal'); plt.grid(True)
plt.show()
plt.savefig("field.png")

# 3) streamlines of -∇f (descent direction)
U = -GX; V = -GY
fig = plt.figure(figsize=(7,7))
plt.streamplot(X, Y, U, V, density=1.5, linewidth=1)
plt.xlabel('x'); plt.ylabel('y'); plt.title('Линии тока (по −∇f)')
plt.axis('equal'); plt.grid(True)
plt.show()
plt.savefig("streamlines.png")