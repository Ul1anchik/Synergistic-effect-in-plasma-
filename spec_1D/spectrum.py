import matplotlib.pyplot as plt
import numpy as np

# Чтение данных из файла
filename = 'spcpz_PAM_7x3_cut16.dat'  

data = np.loadtxt(filename)
x = data[:, 0]  # первая колонка - X
y = data[:, 1]  # вторая колонка - Y

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2)  # синяя линия
plt.xlabel('X ось')
plt.ylabel('Y ось')
plt.title('График из файла .dat')
plt.grid(True, alpha=0.3)
plt.show()