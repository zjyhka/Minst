import numpy as np
import random

"""
numpy的基本操作，建立数组，元素类型，数组转置
"""

t1 = np.array(range(1, 25))
t2 = np.array([1, 2, 3, 4, 5, ])
t3 = np.arange(1, 10, 2)

print(t1)
print(type(t1))
print(t2)
print(type(t2))
print(t3)
print(type(t3))
# 打印数组中元素的类型
print(t3.dtype)

# 指定数据类型，使用dtype
t4 = np.array(range(1, 5), dtype="float64")
print(t4)
print(t4.dtype)

t5 = np.array([1, 0, 1, 0, 1], dtype="bool")
print(t5)
print(t5.dtype)

# 调整数据类型
t6 = t5.astype("int8")
print(t6)
print(t6.dtype)

# numpy中的小数
t7 = np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)

# 保留两位小数
t8 = np.round(t7, 2)
print(t8)
print(t8.dtype)

# 数组转置,4x6变为6x4
t9 = np.array(range(24)).reshape((4, 6))
t10 = t9.transpose()
t11 = t9.T
t12 = t9.swapaxes(1, 0)
print(t9)
print("-" * 100)
print(t10)
print("-" * 100)
print(t11)
