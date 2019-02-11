from number_class import mnist_load
from matplotlib import pyplot as plt
import numpy as np

train_images = mnist_load.load_train_images()
train_labels = mnist_load.load_train_labels()
print(np.shape(train_images))

"""
测试看测试集中的数据，从0-9的样子，随机取一个
"""

fig, ax = plt.subplots(
    nrows=2,
    ncols=5,
    sharex=True,
    sharey=True, )

ax = ax.flatten()
for i in range(10):
    img = train_images[:, train_labels == i]
    img = img[:, 0].reshape((28, 28))
    ax[i].imshow(img, cmap='Greys', interpolation='nearest')

ax[0].set_xticks([])
ax[0].set_yticks([])
plt.tight_layout()
plt.show()

