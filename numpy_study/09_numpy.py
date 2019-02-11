import numpy as np

"""现在希望把之前案例中两个国家的数据方法一起来研究分析，
同时保留国家的信息（每条数据的国家来源），应该怎么办
"""

# 加载国家数据
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"
us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
t_us = np.loadtxt(us_file_path, delimiter=",", dtype="int")  # dtype默认为float
t_uk = np.loadtxt(uk_file_path, delimiter=",", dtype="int")

# 添加国家信息
# 构造全为0的数组，元素为float型
zeros_data = np.zeros((t_us.shape[0], 1)).astype(int)
# 构造全为1的数组，元素为float型
ones_data = np.ones((t_uk.shape[0], 1)).astype(int)

# 分别添加一列全为0 和 1 的数组
t_us = np.hstack((t_us, zeros_data))
t_uk = np.hstack((t_uk, ones_data))

# 拼接两组数据
final_data = np.vstack((t_us, t_uk))
print(final_data)
