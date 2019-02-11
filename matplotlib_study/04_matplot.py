from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='C:/Windows/Fonts/simhei.ttf')
"""自己和同桌11岁到30岁每年交的男女朋友数量"""
x = range(11, 31)
y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y_2 = [1,0,3,1,2,2,3,3,2,1 ,2,1,1,1,1,1,1,1,1,1]


plt.figure(figsize=(20,10), dpi=80)
plt.plot(x, y_1, label="自己", color="#DC143C", linestyle="--", linewidth=4, alpha=0.6)
plt.plot(x, y_2, label="同桌", color="cyan", linestyle="-.", linewidth=2, alpha=0.8)
# 设置x轴刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x, _xtick_labels, fontproperties=my_font)
plt.yticks(range(0, 9))

# 绘制网格，alpha设置透明度
plt.grid(alpha=0.5)

# 添加图例
plt.legend(prop=my_font, loc="upper left")

# 添加文字注释用plt.text()使用正则表达式传递
# 添加水印，先用plt.subplot分区，再使用分区后的fig.text()添加水印
"""
fig.text(0.75, 0.45, '我的花花世界',
         fontsize=40, color='gray',
         ha='right', va='bottom', alpha=0.4)
"""
# 展示
plt.show()