import numpy as np

# Сумма векторов
vec1 = np.array([2, 4, 7, 2.5])
vec2 = np.array([12, 6, 3.6, 13])
print(vec1 + vec2)

# Умножение вектора на число
vec1 = np.arange(5)
print(vec1 * 10)

# Сравнение векторов
vec1 = np.array([2, 4, 7, 2.5])
vec2 = np.array([12, 6, 3.6, 13])
print(vec1 > vec2)

# Сравнение вектора с числом
vec = np.array([14, 15, 9, 26, 53, 5, 89])
print(vec <= 26)

# Нахождение длинны вектора
vec = np.array([3, 4])
print(np.linalg.norm(vec))

# Нахождение расстояния между векторами
vec1 = np.array([0, 3, 5])
vec2 = np.array([12, 4, 7])
print(np.linalg.norm(vec1 - vec2))

# Нахождение скалярного произведения
vec1 = np.arange(1, 6)
vec2 = np.linspace(10, 20, 5)
print(np.dot(vec1, vec2))

# Нахождение минимального значения
vec1 = np.arange(1, 11)
print(np.min(vec1))

# Нахождение максимального значения
vec1 = np.arange(1, 11)
print(np.max(vec1))

# Нахождение максимального значения
vec1 = np.arange(1, 11)
print(np.max(vec1))

# Нахождение среднего арифметического
vec1 = np.arange(1, 11)
print(np.mean(vec1))

# Нахождение медианы
vec1 = np.arange(1, 11)
print(np.median(vec1))

# Нахождение стандартного отклонения
vec1 = np.arange(1, 11)
print(np.std(vec1))
