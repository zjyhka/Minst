import pandas as pd
import numpy as np

"""
缺失数据处理，处理nan

"""

# 读取CSV中的文件
df = pd.read_csv("./dogNames2.csv")

# 使用isnull和notnull
# print(pd.isnull(df))
# print(pd.notnull(df))

t1 = pd.DataFrame(np.arange(12).reshape((3, 4)), index=list("abc"), columns=list("WXYZ"))
print(t1)

t1.loc[["b", "c"], ["W", "X"]] = np.nan
print(t1)
print(pd.isnull(t1))
print(pd.notnull(t1))

print("-" * 100)
print(t1[pd.notnull(t1["W"])])
print(t1[pd.isnull(t1["X"])])
print("-" * 100)

# 删除数据，原地修改使inplace = True
print(t1.dropna(axis=0, how="any"))
print(t1.dropna(axis=0, how="all"))

# 替换nan
print(t1.mean())
print(t1.fillna(t1.mean()))
