import numpy as np

seed = 2021
np.random.seed(seed)
simple = np.random.rand()
randoms = np.random.uniform(-150, 2021, 120)
table = np.random.randint(1, 101, size=(3, 2))
even = np.arange(2, 17, 2)
mix = even.copy()
np.random.shuffle(mix)
select = np.random.choice(even, size=3, replace=False)
triplet = np.random.permutation(select)
