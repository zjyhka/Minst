from number_class import mnist_load
from matplotlib import pyplot as plt
import numpy as np

"""
测试看测试集中的数据，同是7的手写数字图片展示25个
"""

train_images = mnist_load.load_train_images()
train_labels = mnist_load.load_train_labels()
print(np.shape(train_images))

fig, ax = plt.subplots(
    nrows=5,
    ncols=5,
    sharex=True,
    sharey=True, )

ax = ax.flatten()
for i in range(25):
    img = train_images[:, train_labels == 7]
    img = img[:, i].reshape((28, 28))
    ax[i].imshow(img, cmap='Greys', interpolation='nearest')

ax[0].set_xticks([])
ax[0].set_yticks([])
plt.tight_layout()
plt.show()


