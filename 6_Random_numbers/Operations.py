import numpy as np

# Генерация случайного float (от 0 до 1)
print(np.random.rand())

# Генерация случайного float (от 0 до 100)
print(np.random.rand() * 100)

# Генерация случайного float массива из 5 элементов
print(np.random.rand(5))

# Генерация случайного многомерного float массива из m x n элементов
print(np.random.rand(2, 3))

# Генерация случайного многомерного float массива с передачей в качестве параметра формы, через shape
shape = (2, 3)
print(np.random.sample(shape))

# Генерация случайного многомерного float массива с указанием нижней и верхней границы, а также количества элементов
print(np.random.uniform(0.5, 0.75, size=5))

# Генерация случайного int массива заданной размерности
print(np.random.randint(1, 10, size=5))

# Генерация случайного многомерного int массива заданной размерности, с указанием пределов
print(np.random.randint(1, 10, size=(3, 3, 3)))

# Перемешать исходный массив
arr = np.arange(6)
np.random.shuffle(arr)
print(arr)

# Перемешать и вернуть новый массив
arr = np.arange(10)
print(np.random.permutation(arr))

# Генерация случайной выборки из одномерного массив. Параметр replace - повторения
arr = np.arange(10)
print(np.random.choice(arr, size=5, replace=False))

# Задать исходное число для генерации псевдослучайных чисел (вернет всегда одинаковый архив)
np.random.seed(23)
print(np.random.randint(10, size=(3, 4)))


