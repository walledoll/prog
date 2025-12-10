import numpy as np
import matplotlib.pyplot as plt

# Определяем диапазон t и функцию y
t = np.linspace(-2, 2, 400)
y = 1 - t**3

# Создаем основную фигуру и левую ось Y (ax1)
fig, ax1 = plt.subplots(figsize=(10, 6))

# Создаем вторую ось Y (ax2), которая использует ту же ось X, что и ax1
ax2 = ax1.twinx()

# --- Левая ось Y (Широкий масштаб Y) ---
ax1.plot(t, y, color='blue', label='Масштаб: -100 до 100')
ax1.set_xlabel("t")
ax1.set_ylabel("Левая ось Y (-100 до 100)", color='blue')
ax1.set_ylim(-100, 100)
ax1.tick_params(axis='y', labelcolor='blue')
ax1.grid(True, axis='x', linestyle='--', alpha=0.6) # Сетка только по X

# --- Правая ось Y (Увеличенный масштаб Y) ---
ax2.plot(t, y, color='red', label='Масштаб: -20 до 20')
ax2.set_ylabel("Правая ось Y (-20 до 20)", color='red')
ax2.set_ylim(-20, 20)
ax2.tick_params(axis='y', labelcolor='red')

# Общие настройки графика
plt.title("График функции на одной плоскости с двумя разными осями Y")
fig.tight_layout() # Автоматически регулируем параметры

# Сохраняем и отображаем график
plt.savefig("parametric_function_one_plot_two_y_axes.png")
plt.show()
