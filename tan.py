import numpy as np
import matplotlib.pyplot as plt

# Generate x values avoiding asymptotes
x = np.linspace(-np.pi/2 + 0.1, np.pi/2 - 0.1, 500)
y = np.tan(x)

plt.figure()
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("tan(x)")
plt.title("График функции тангенс")
plt.grid(True)

plt.show()
plt.savefig("tan_function.png")