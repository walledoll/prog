import numpy as np
import matplotlib.pyplot as plt

# define t range
t = np.linspace(-2, 2, 400)
y = 1 - t**3

plt.figure()
plt.plot(t, y)
plt.xlabel("t")
plt.ylabel("y = 1 - t^3")
plt.title("График функции y = 1 - t^3")
plt.grid(True)
plt.show()
plt.savefig("parametric_function.png")