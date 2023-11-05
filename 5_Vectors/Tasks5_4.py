import numpy as np

# Найти коллинеарные вектора
a = np.array([23, 34, 27])
b = np.array([-54, 1, 46])
c = np.array([46, 68, 54])

print(np.linalg.norm(a) + np.linalg.norm(b) == (np.linalg.norm(a + b)))
print(np.linalg.norm(a) + np.linalg.norm(c) == (np.linalg.norm(a + c)))
print(np.linalg.norm(b) + np.linalg.norm(c) == (np.linalg.norm(a + b)))
