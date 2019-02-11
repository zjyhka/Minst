import pandas as pd
import string

"""
series 一维数组 带标签
data frame 二维数组 是series的容器
"""

t = pd.Series([2, 21, 34, 12, 45, 6])
print(t)
print(type(t))

# 自定义索引
t1 = pd.Series([1, 2, 3, 4, 5], index=list("abcde"))
print(t1)

# 使用字典创建pandas
temp_dict = {"name": "xiaohong", "age": 30, "Tel": 10086}
t3 = pd.Series(temp_dict)
print(t3)

a = {string.ascii_uppercase[i]:i for i in range(10)}
t4 = pd.Series(a)
print(t4)

# 切片和索引
print(t3["age"])
print(t3.index)
print(len(t3.index))
print(list(t3.index))

print(t3.values)
print(type(t3.values))  # numpy.ndarray类型

# where方法
