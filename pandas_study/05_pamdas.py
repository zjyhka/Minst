import pandas as pd
from matplotlib import pyplot as plt

"""
对于这一组电影数据，如果我们想rating，runtime的分布情况，应该如何呈现数据
选择直方图
"""

file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)
print(df.head(1))
print(df.info())

# 准备数据
runtime_data = df["Runtime (Minutes)"].values
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

rating_data = df["Rating"].values
max_rating = rating_data.max()
min_rating = rating_data.min()

print(min_runtime)
print(max_runtime)
print(min_rating)
print(max_rating)

# x轴分布
num_bin_list = [min_runtime]
i = min_runtime + 16
num_bin_list.append(i)
while i <= max_runtime:
    i += 5
    num_bin_list.append(i)

num_bin_list2 = [min_rating]
i = min_rating + 1.6
num_bin_list2.append(i)
while i <= max_rating:
    i += 0.5
    num_bin_list2.append(i)


# 设置图形大小
plt.figure(figsize=(20, 10), dpi=80)
# 分区
ax1 = plt.subplot(2, 1, 1)
ax2 = plt.subplot(2, 1, 2)
plt.sca(ax1)
plt.hist(runtime_data, num_bin_list, color="orange")
plt.xticks(num_bin_list)
plt.sca(ax2)
plt.hist(rating_data, num_bin_list2, color="blue")
plt.xticks(num_bin_list2)

# 展示
plt.show()
