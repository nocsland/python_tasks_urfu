import numpy as np

# Найдите пару перпендикулярных векторов с помощью скалярного произведения (оно должно быть равно нулю).

a = np.array([23, 34, 27])
b = np.array([-54, 1, 46])
c = np.array([46, 68, 54])

print(np.dot(a, b) == 0)
print(np.dot(a, c) == 0)
print(np.dot(b, c) == 0)
