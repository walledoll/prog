import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    """Целевая функция"""
    return 7*x**2 - 10*x*y + 7*y**2 - 4*x + 4*y - 8

# Определяем диапазон X и Y
x = np.linspace(-2, 2, 200)
y = np.linspace(-2, 2, 200)

# Создаем сетку координат и вычисляем значения функции Z
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# --- ГРАФИК ЛИНИЙ УРОВНЯ (Contour Lines) ---

# Устанавливаем стиль по умолчанию (белый фон)
plt.style.use('default') 

fig = plt.figure(figsize=(8, 6), facecolor='white') # Явно задаем белый фон фигуры
ax = fig.add_subplot(111)

# Используем ax.contour() для рисования линий уровня
# cmap='viridis' или 'plasma' автоматически присваивает уникальный цвет каждому уровню
contour_lines = ax.contour(X, Y, Z, levels=20, cmap=plt.cm.viridis)

# Добавляем подписи к линиям уровня (масштаб/значение), inline=True делает подписи "встроенными" в линии
ax.clabel(contour_lines, inline=True, fontsize=10, fmt='%1.1f') # fmt='%1.1f' для 1 знака после запятой

# Настраиваем внешний вид графика
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Линии уровня функции f(x,y) (Без градусника)')
ax.axis('equal') # Делает масштаб осей одинаковым
ax.grid(True, linestyle=':', alpha=0.6)

# Сохраняем и отображаем график
plt.savefig("contour_lines_clean.png", facecolor='white') # Сохраняем с белым фоном
plt.show()
