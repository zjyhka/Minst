import numpy as np

"""数组的拼接，数组的行列交换"""

t1 = np.array(range(0, 12)).reshape((2, 6))
t2 = np.array(range(12, 24)).reshape((2, 6))

# 竖直拼接
t3 = np.vstack((t1, t2))  # 里边传一个元组
print(t3)
print("-" * 100)
# 水平拼接
print(np.hstack((t1, t2)))

print("-" * 100)
# 行交换
t1 = t1.reshape((3, 4))
t1[[1, 2], :] = t1[[2, 1], :]
print(t1)

print("-" * 100)
# 列交换
t1[:, [0, 1]] = t1[:, [1, 0]]
print(t1)