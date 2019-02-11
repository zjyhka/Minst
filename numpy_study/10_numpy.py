import numpy as np

"""
创建为0，为1，对角线为1的数组，获取最大值和最小值的位置，
创建随机数组
使用copy和view
"""

# 对角线为1的正方形数组
t1 = np.eye(3)
print(t1)

# 获取最大值和最小值的位置
print(np.argmax(t1, axis=0))
t1[t1 == 1] = -1
print(np.argmin(t1, axis=0))

#  生成随机数
# 整数
t2 = np.random.randint(1, 50, (3, 4))
print(t2)

# 小数
t3 = np.random.uniform(1, 50, (3, 4))
print(t3)

# 随机种子
np.random.seed(8)
t4 = np.random.randint(1, 50, (3, 4))
print(t4)

"""
a = b 完全不复制 a和b相互影响
a = b[:] 视图操作 a的数据完全由b保管 a受b的变化影响
a = b.copy() a和b互补影响
* 重新赋值给自身，不开辟新的空间
"""