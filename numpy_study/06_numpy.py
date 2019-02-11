import numpy as np
from matplotlib import pyplot as plt

"""
现在这里有一个英国和美国各自youtube1000多个视频的
点击,喜欢,不喜欢,评论数量(["views","likes","dislikes","comment_total"])的csv,
英国和美国各自youtube1000的数据结合之前的matplotlib绘制出各自的评论数量的直方图
"""

uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"
us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
t_us = np.loadtxt(us_file_path, delimiter=",", dtype="int")  # dtype默认为float
t_uk = np.loadtxt(uk_file_path, delimiter=",", dtype="int")

# 取评论的数据
t_us_comments = t_us[:, -1]
t_uk_comments = t_uk[:, -1]

# 取评论数大于5000的
t_us_comments = t_us_comments[t_us_comments <= 5000]
t_uk_comments = t_uk_comments[t_uk_comments <= 5000]

# 画直方图分组
# print(t_us_comments.max(), t_us_comments.min())
# 最大值582624 最小值0
d = 250
bin_nums = (t_us_comments.max() - t_us_comments.min())//d

# print(t_uk_comments.max(), t_uk_comments.min())
d1 = 250
bin_nums1 = (t_uk_comments.max() - t_uk_comments.min())//d

_x_labels = list(range(min(t_us_comments), max(t_us_comments)+d, d))
_x_labels += list(range(t_uk_comments.min(), t_uk_comments.max()+d1, d1))
_x = list(range(len(_x_labels)))
# 绘图
plt.figure(figsize=(40,10), dpi=80)
ax1 = plt.subplot(1, 2, 1)
ax2 = plt.subplot(1, 2, 2)
plt.sca(ax1)

plt.hist(t_us_comments, bin_nums, color="red")
plt.sca(ax2)

plt.hist(t_uk_comments, bin_nums1, color="orange")

# 展示
plt.show()
