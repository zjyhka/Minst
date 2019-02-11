from number_class import mnist_load
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from matplotlib import font_manager
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn import svm
import time

# 导入数据集
train_images = mnist_load.load_train_images()
train_labels = mnist_load.load_train_labels()
test_images = mnist_load.load_test_images()
test_labels = mnist_load.load_test_labels()

# 对数据集进行处理，将训练集和测试集的图片数组进行转置，与标签数组行向量能够一一对应
train_images = np.transpose(train_images)
train_labels = train_labels.reshape((train_labels.shape[0], 1))
test_images = np.transpose(test_images)
test_labels = test_labels.reshape((test_labels.shape[0], 1))


def classify_svm(c, train_data, train_label, test_data, test_label, t):

    # PCA主成分分析，进行特征降维
    # n_components设为分数时，选择特征值占总特征值大于n的，作为主成分
    # whiten=True表示做白化处理，白化处理主要是为了使处理后的数据方差都一致
    pca = PCA(n_components=0.8, whiten=True)
    train_x = pca.fit_transform(train_data)
    test_x = pca.transform(test_data)

    # 使用多项式核函数，训练SVM支持向量机
    svc = svm.SVC(kernel='poly', degree=3, C=c)
    svc.fit(train_x, train_label)
    spend_time = time.time() - t
    test_pre = svc.predict(test_x)
    acc = accuracy_score(test_label, test_pre)

    return acc, spend_time


if __name__ == "__main__":
    train_data = train_images[0:, 0:]
    train_label = train_labels[0:, 0]
    test_data = test_images[0:, 0:]
    test_label = test_labels[0:, 0]

    result_list = []

    for i in range(1, 11):
        t = time.time()
        result = list(classify_svm(i, train_data, train_label, test_data, test_label, t))
        result_list.append(result)

    result_show = pd.DataFrame(result_list, index=list(range(1, 11)), columns=list(["accuracy", "spend_time"]))
    print(result_show)

    my_font = font_manager.FontProperties(fname='C:/Windows/Fonts/simhei.ttf')
    # 绘图
    plt.figure(figsize=(40, 10), dpi=80)
    ax1 = plt.subplot(1, 2, 1)
    ax2 = plt.subplot(1, 2, 2)

    plt.sca(ax1)
    plt.plot(list(range(1, 11)), result_show["accuracy"], color="red", label="测试准确率")

    plt.xticks(list(range(1, 11)))
    plt.legend(prop=my_font)
    plt.sca(ax2)
    plt.plot(list(range(1, 11)), result_show["spend_time"], color="cyan", label="花费时间")
    plt.xticks(list(range(1, 11)))

    plt.legend(prop=my_font)
    # 展示
    plt.show()
