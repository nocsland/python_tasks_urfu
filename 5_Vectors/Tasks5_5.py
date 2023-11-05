import numpy as np

# Найти вектора расстояние между которыми больше 100

a = np.array([23, 34, 27])
b = np.array([-54, 1, 46])
c = np.array([46, 68, 54])

print(np.linalg.norm(a - b) > 100)
print(np.linalg.norm(a - c) > 100)
print(np.linalg.norm(b - c) > 100)
