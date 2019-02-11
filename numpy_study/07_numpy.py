import numpy as np
from matplotlib import pyplot as plt

"""
现在这里有一个英国和美国各自youtube1000多个视频的
点击,喜欢,不喜欢,评论数量(["views","likes","dislikes","comment_total"])的csv,
希望了解英国的youtube中视频的评论数和喜欢数的关系，应该如何绘制改图
"""

uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"
t_uk = np.loadtxt(uk_file_path, delimiter=",", dtype="int")

# 对原始数据进行处理，选择喜欢数比50万小的
t_uk = t_uk[t_uk[:, 1] <= 500000]

t_uk_like = t_uk[:, 1]
t_uk_comment = t_uk[:, -1]

# 绘制散点图
plt.figure(figsize=(20, 10), dpi=80)
plt.scatter(t_uk_like, t_uk_comment)
plt.show()
