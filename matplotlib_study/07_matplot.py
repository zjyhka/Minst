from matplotlib import pyplot as plt
from matplotlib import font_manager

"""列表a中电影分别在2017-09-14(b_14), 2017-09-15(b_15), 2017-09-16(b_16)三天的票房,
   为了展示列表中电影本身的票房以及同其他电影的数据对比情况,应该如何更加直观的呈现该数据"""
my_font = font_manager.FontProperties(fname='C:/Windows/Fonts/simhei.ttf')

# 原始数据
a = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

bar_width = 0.2

# x往右移，让三个条形图不重叠
x_14 = list(range(len(a)))
x_15 = [i+bar_width for i in range(len(a))]
x_16 = [i+bar_width*2 for i in range(len(a))]

# 设置图形大小
plt.figure(figsize=(20, 10), dpi=80)

# 绘制条形图
plt.bar(x_14, b_14, width=bar_width, color="#D2691E", label="9月14日")
plt.bar(x_15, b_15, width=bar_width, color="#FF4500", label="9月15日")
plt.bar(x_16, b_16, width=bar_width, color="#008B8B", label="9月16日")
# 调整x轴的刻度
plt.xticks(x_15, a, fontproperties=my_font)  # 让电影名字居中显示

# 设置图例
plt.legend(prop=my_font)
# 绘制网格
plt.grid(alpha=0.5)
# 展示
plt.show()