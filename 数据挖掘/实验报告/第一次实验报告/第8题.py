import matplotlib.pyplot as plt
import numpy as np

# 第8题
# 创建2*2大小的子图，共享x轴和y轴，取消子图之间的间隔。
# 对四个子图生成500个标准正态分布数，绘制频数分布直方图，颜色黑色，透明度50%

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)

# 移除子图之间的间隔 (wspace=0, hspace=0)
fig.subplots_adjust(wspace=0, hspace=0)

for ax in axes.flatten():
    # 生成 500 个标准正态分布数
    data = np.random.randn(500)
    # 绘制直方图，黑色，透明度 50%
    ax.hist(data, bins=30, color='black', alpha=0.5)

plt.show()
