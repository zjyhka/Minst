import pandas as pd
import numpy as np

"""使用loc和iloc"""

# 读取CSV中的文件
df = pd.read_csv("./dogNames2.csv")

t1 = pd.DataFrame(np.array(range(12)).reshape((3, 4)), index=list("abc"), columns=list("CDEF"))

print(t1)
# 通过标签索引数据
print(t1.loc["a", "E"])
print(t1.loc["a", :])  # 取一整行
print(t1.loc[:, "F"])  # 取一整列

print(t1.loc["a":"c", "C"])  # 右边"c"是闭合的

# 通过位置获取数据
print(t1.iloc[:, [2, 1]])

# 布尔索引
t2 = df[df["Count_AnimalName"] > 800].copy()
print(t2)

# 多个条件使用 &且 |或 ，不同的条件使用括号括起来
t3 = df[(df["Count_AnimalName"] > 800) & (df["Count_AnimalName"] < 1000)].copy()
print(t3)




