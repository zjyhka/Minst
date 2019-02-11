from matplotlib import pyplot as plt
from matplotlib import font_manager

"""在美国2004年人口普查发现有124 million的人在离家相对较远的地方工作。根据他们从家到上班地点所需要的时间,通过
   抽样统计(最后一列)出了下表的数据"""
my_font = font_manager.FontProperties(fname='C:/Windows/Fonts/simhei.ttf')

# 原始数据才能绘制直方图，使用hist()方法，统计过的数据绘制条形图
# 将统计过的数据绘制成直方图的样子

interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]

# 设置图形大小
plt.figure(figsize=(20,10), dpi=80)
# 绘制直方图
plt.bar(range(len(quantity)), quantity, width=1, color="#DC143C")
# 设置x轴的刻度
_x = [i-0.5 for i in range(13)]  # len(interval)为12
_xtick_labels = interval+[150]
plt.xticks(_x, _xtick_labels)
# 绘制网格
plt.grid(alpha=0.5)
# 展示
plt.show()
