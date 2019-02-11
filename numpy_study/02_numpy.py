import numpy as np

"""
现在这里有一个英国和美国各自youtube1000多个视频的
点击,喜欢,不喜欢,评论数量(["views","likes","dislikes","comment_total"])的csv,
读取数据，取行，取列，取元素的操作
"""

gb_file_path = "./youtube_video_data/GB_video_data_numbers.csv"
us_file_path = "./youtube_video_data/US_video_data_numbers.csv"

t1 = np.loadtxt(us_file_path, delimiter=",", dtype="int")  # dtype默认为float
print(t1)
"""
print("*" * 100)
t2 = np.loadtxt(us_file_path, delimiter=",", dtype="int", unpack=True)  # 转置效果
print(t2)
"""

print("-" * 100)
# 取行
print(t1[2])
print("-" * 100)
# 取连续的多行
print(t1[2:])
print("-" * 100)
# 取不连续的多行
print(t1[[2, 4, 8]])

print("-" * 100)
# 取行
print(t1[1, :])
print("-" * 100)
print(t1[2:, :])
print("-" * 100)
print(t1[[2, 10, 3], :])
print("-" * 100)
# 取列
print(t1[:, 2])
print("-" * 100)
print(t1[:, 2:])
print("-" * 100)
print(t1[:, [1, 2, 3]])
print("-" * 100)

# 取单行和单列，取第三行，第四列的值
a = t1[2, 3]
print(a)
print(type(a))
print("-" * 100)
# 取多行和多列，第三行到第五行，第二列到第四列的结果
# 取的是交叉点的位置
b = t1[2:5, 1:4]
print(b)
print("-" * 100)
# 取多个不相邻的点，取的三个点是(0, 0) (2, 1) (2, 3)
c = t1[[0, 2, 2], [0, 1, 3]]
print(c)
print("-" * 100)
print(t1[:2])
