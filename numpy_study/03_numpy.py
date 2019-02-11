import numpy as np

"""
numpy的三元运算符，clip裁剪功能，布尔索引，nan和inf，以及nan的运算
"""

t = np.arange(24).reshape((4, 6))
print(t)

print("-" * 100)
t1 = np.where(t < 10, 0, 10)  # numpy的三元运算符
print(t1)
print("-" * 100)

t2 = t.clip(10, 18)  # 裁剪功能，小于等于10的变为10，大于等于18的变为18
print(t2)
print("-" * 100)

a = np.nan  # not a number = nan
b = np.inf  # 无穷大
print(type(a))  # 两个都为浮点类型
print(type(b))
print("-" * 100)

t2 = t2.astype("float")
t2[3, 3] = np.nan
print(t2)
print("-" * 100)

# 两个nan不相等
print(np.nan == np.nan)
print(np.nan != np.nan)

# 统计数组中nan的个数
print(np.count_nonzero(t2 != t2))  # t2 != t2 输出的为布尔索引数组
print(np.count_nonzero(np.isnan(t2)))

# nan和任何值计算结果都为nan
print(np.sum(t2))
print(np.sum(t2, axis=0))

# 将nan替换为0，通常替换为中值或均值
t2[np.isnan(t2)] = 0
print(np.sum(t2))





