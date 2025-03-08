import numpy as np
import numexpr as ne
import time

# Создаём тестовый массив на 2 миллиона строк и 5 колонок
agents = np.random.randint(0, 10, size=(2_000_000, 5), dtype=np.int32)

# Обычный NumPy
start = time.time()
mask = (agents[:, 2] > 5) & (agents[:, 3] > 2)
agents[mask, 4] += 10
print("NumPy time:", time.time() - start)

# NumExpr
agents = np.random.randint(0, 10, size=(2_000_000, 5), dtype=np.int32)  # Сбросим массив
col2, col3 = agents[:, 2], agents[:, 3]  # Вынесем колонки
start = time.time()
mask = ne.evaluate("(col2 > 5) & (col3 > 2)")
agents[mask, 4] += 10
print("NumExpr time:", time.time() - start)
