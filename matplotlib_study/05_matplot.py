from matplotlib import pyplot as plt
from matplotlib import font_manager

"""北京2016年3,10月份每天白天的最高气温(分别位于列表a,b),
   那么此时如何寻找出气温和随时间(天)变化的某种规律"""
my_font = font_manager.FontProperties(fname='C:/Windows/Fonts/simhei.ttf')

y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14,
       17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22, 22, 23]
y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23,
        17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13, 12, 13, 6]

x_3 = range(1, 32)
x_10 = range(50, 81)

# 设置图形大小
plt.figure(figsize=(20, 10), dpi=80)
# 使用scatter()方法绘制散点图
plt.scatter(x_3, y_3)
plt.scatter(x_10, y_10)

# 调整x轴的刻度
_x = list(x_3) + list(x_10)
_xtick_labels = ["3月{}日".format(i) for i in x_3]
_xtick_labels += ["10月{}日".format(i-49) for i in x_10]
plt.xticks(_x[::3], _xtick_labels[::3], fontproperties=my_font, rotation=45)

# 添加描述信息
plt.xlabel("温度", fontproperties=my_font)
plt.ylabel("时间", fontproperties=my_font)
plt.title("2016年3月和10月的气温分布", fontproperties=my_font)
# 展示
plt.show()