import matplotlib.pyplot as plt
import numpy as np

def extract_data_slice(filename, x_min, x_max):
    """
    Вырезает данные в указанном диапазоне по оси X
    """
    # Чтение всех данных
    data = np.loadtxt(filename)
    x_all = data[:, 0]
    y_all = data[:, 1]
    
    # Поиск индексов в заданном диапазоне
    mask = (x_all >= x_min) & (x_all <= x_max)
    x_slice = x_all[mask]
    y_slice = y_all[mask]
    
    return x_slice, y_slice, x_all, y_all

# Параметры вырезки
filename = 'spcpz_PAM_7x3_cut16.dat'
x_min = 11.0  # начальное значение X
x_max = 15.65  # конечное значение X

# Вырезка данных
x_slice, y_slice, x_all, y_all = extract_data_slice(filename, x_min, x_max)

# Построение графиков
plt.figure(figsize=(12, 6))

# Полный график
plt.subplot(1, 2, 1)
plt.plot(x_all, y_all, 'gray', alpha=0.5, label='Все данные')
plt.axvspan(x_min, x_max, color='red', alpha=0.2, label='Вырезаемая область')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Все данные с выделением области')
plt.legend()
plt.grid(True, alpha=0.3)

# Вырезанный кусок
plt.subplot(1, 2, 2)
plt.plot(x_slice, y_slice, 'b-', linewidth=2)
plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'Вырезанный кусок: X от {x_min} до {x_max}')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"Вырезано {len(x_slice)} точек из {len(x_all)}")


# После вырезки данных


# Сохранение в файл .dat
np.savetxt('piece_1.dat', 
           np.column_stack((x_slice, y_slice)),  # объединяем X и Y в один массив
           fmt='%.6f',                          # формат чисел (6 знаков после запятой)
           delimiter='\t',                      # разделитель - табуляция
           header='X\tY',                       # заголовок колонок
           comments='')                         # убираем символ комментария перед header

print(f"Данные сохранены в 'piece_1.dat'")