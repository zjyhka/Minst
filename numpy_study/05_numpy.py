import numpy as np

"""
ndarry缺失值填充均值
"""


def fill_ndarray(t1):
    """
    缺失值填充均值
    :param t1:
    :return: t1
    """
    for i in range(t1.shape[1]): # shape[1]表示遍历每一列，shape（行，列），取第二个元素
        temp_col = t1[:, i]  # 当前这一列，用行遍历
        nan_num = np.count_nonzero(temp_col != temp_col)
        if nan_num != 0:  # 说明当前这一列有nan存在
            temp_not_nan_col = temp_col[temp_col == temp_col]  # 提取出这一列不为nan的元素
            # 选中当前为nan的位置，把值赋值给原来是nan的位置
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()
    return t1


if __name__ == '__main__':
    t1 = np.arange(12).reshape((3, 4)).astype("float")

    t1[1, 2:] = np.nan
    print(t1)

    t1 = fill_ndarray(t1)
    print(t1)