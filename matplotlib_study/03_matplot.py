from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='C:/Windows/Fonts/simhei.ttf')
"""11岁到30岁每年交的男女朋友数量"""
x = range(11, 31)
y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]

plt.figure(figsize=(20,10), dpi=80)
plt.plot(x, y)
# 设置x轴刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x, _xtick_labels, fontproperties=my_font)
plt.yticks(range(0, 9))

# 绘制网格，alpha设置透明度
plt.grid(alpha=0.5)

plt.show()