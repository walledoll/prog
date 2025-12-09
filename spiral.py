import numpy as np
import matplotlib.pyplot as plt

phi = np.linspace(0.1, 10*np.pi, 2000)
r = np.pi / phi

plt.figure()
ax = plt.subplot(111, projection='polar')
ax.plot(phi, r)
ax.set_title("Гиперболическая спираль: r = π / φ")
plt.show()
plt.savefig("hyperbolic_spiral.png")