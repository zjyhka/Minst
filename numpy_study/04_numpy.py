import numpy as np
import random

"""
numpy中常用的统计函数
"""
# 求和函数
t1 = np.arange(12).reshape((3,4))
print(np.sum(t1, axis=0))  # 分别计算每列的和
print(np.sum(t1, axis=1))  # 分别计算每行的和
print("-" * 100)

t2 = np.array([random.randint(0, 50) for i in range(12)]).reshape((3, 4))
# 求均值，受离群点影响较大
print(np.mean(t1, axis=0))
print(t1.mean(axis=0))
print(t2.mean())
print("-" * 100)

# 求中值
print(np.median(t1, axis=0))
print(np.median(t2))
print("-" * 100)

# 求最大值，最小值
print(t1.max(axis=1))
print(np.max(t1, axis=1))
print(t2.min())
print(np.min(t2))
print("-" * 100)

# 求极值，即最大值和最小值之差
print(np.ptp(t1))
print(np.ptp(t2, axis=0))
print("-" * 100)

# 求标准差，方差开方
print(np.std(t1, axis=0))
d = np.std(t2)
print(d)
print(round(d, 2))
