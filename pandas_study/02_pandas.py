import pandas as pd
import numpy as np

"""读取外部数据"""
"""创建DataFrame"""
"""配合MongoDB使用"""

# 读取CSV中的文件
df = pd.read_csv("./dogNames2.csv")

print(df.head())
print(df.info())
print("-" * 100)

# DataFrame中的排序方法，找Count_AnimalName最大的前五个
df = df.sort_values(by="Count_AnimalName", ascending=False)
print(df.head())

print("-" * 100)

# pandas中的索引和切片
# 方括号写数字，对行进行操作，方括号写字符串，对列进行操作
print(df[:20])
print(df["Row_Labels"])
print(type(df["Row_Labels"]))  # Series类型

# 行索引是index，列索引是column，每一行是一条数据
t1 = pd.DataFrame(np.array(range(12)).reshape((3, 4)))
print(t1)

t2 = pd.DataFrame(np.array(range(12)).reshape((3, 4)), index=list("abc"), columns=list("CDEF"))
print(t2)

d1 = {"name": ["xiaohong", "xiaoming"], "age": [30, 22], "tel": [10086, 10032]}
t3 = pd.DataFrame(d1)
print(t3)

# 部分columns（key值）对应不上，使用nan填充
d2 = [{"name": "xiaoming", "age": 32, "tel": 11010}, {"name":"xiaohong", "tel": 10086},
      {"name": "xiaowang", "age": 22}]
t4 = pd.DataFrame(d2)
print(t4)

# 基础属性
print(t4.index)
print(t4.columns)
print(t4.values)
print(t4.shape)
print(t4.dtypes)
print(t2.ndim)
print("-" * 100)

# 整体情况查询
print(t4.head(1))  # 默认是5行
print("-" * 100)
print(t4.tail(2))
print("-" * 100)
print(t4.info())
print(t2.describe())