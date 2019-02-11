from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

"""
Windows和Linux下设置字体的方式
font = {'family': 'monospace',
        'weight': 'bold',
        'size': 'larger'}
matplotlib.rc("font", **font)
matplotlib.rc("font", family='MicroSoft YaHei', weight="Bold")
"""
# 另外一种设置字体的方式，实例化一个my_fonte
my_font = font_manager.FontProperties(fname='C:/Windows/Fonts/simhei.ttf')

"""表示10点到12点每一分钟的气温，绘制折线图"""
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 10), dpi=80)
plt.plot(x, y)

# 调整x轴的刻度
_x = list(x)  # range函数不能用[::3]的形式取步长，必须转换为列表形式
_xticks_labels = ["10点{}分".format(i) for i in range(60)]
_xticks_labels += ["11点{}分".format(i) for i in range(60)]
# 取步长，数字和字符串一一对应，数据的长度一样
# 第一个参数为数字，第二个参数为对应的字符串，第三个为旋转角度,第四个为中文字体
plt.xticks(_x[::3], _xticks_labels[::3], rotation=45, fontproperties=my_font)

# 添加描述信息
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度 单位(°C)", fontproperties=my_font)
plt.title("10点到12点每分钟的气温变化情况", fontproperties=my_font)

plt.show()