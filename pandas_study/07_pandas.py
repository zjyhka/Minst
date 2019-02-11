import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

"""
对于这一组电影数据，如果我们希望统计电影分类(genre)的情况，应该如何处理数据？
思路：重新构造一个全为0的数组，列名为分类，如果某一条数据中分类出现过，就让0变为1
"""

file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

print(df.info())
print(df["Genre"])  # 同一电影所属类型，用"," 隔开

# 获取电影类型信息
temp_genre_data = df["Genre"].str.split(",").tolist()  # 列表嵌套列表，需要展开
genre_list = list(set([i for j in temp_genre_data for i in j]))  # 去掉重复值利用set
genre_num = len(genre_list)
print(genre_num)

# 构造一个全为0的数组进行统计
zero_df = pd.DataFrame(np.zeros((df.shape[0], genre_num)), columns=genre_list)

# 给每个电影出现分类的位置赋值加1
for i in range(df.shape[0]):
    # zero_df.loc[0, [" Action", "Adventure", "Sci-Fi"]] = 1 布尔索引
    zero_df.loc[i, temp_genre_data[i]] = 1

# 统计每个电影类别的总和
genre_count = zero_df.sum(axis=0)

# 排序
genre_count = genre_count.sort_values()
print(genre_count)
_x = genre_count.index
_y = genre_count.values

# 画图展示
plt.figure(figsize=(20, 10), dpi=80)
plt.bar(_x, _y)

plt.show()
