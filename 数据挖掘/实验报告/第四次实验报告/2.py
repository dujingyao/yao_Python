import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# 1. 准备表 8-1 中的 5 个一维属性样本数据
X = np.array([[10], [7], [28], [20], [35]])
labels = [1, 2, 3, 4, 5]  # 样本的 ID 标签

# 2. 进行凝聚层次聚类 (AGNES)
Z = linkage(X, method='single', metric='euclidean')

print("聚类合并过程 (Z矩阵):")
print(Z)

# 3. 绘制最终生成的树状图 (对应课本图 8-1)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

plt.figure(figsize=(8, 5))
# 绘制树状图
dendrogram(Z, labels=labels)

plt.title('凝聚层次聚类 (AGNES) 树状图 - 例8-2')
plt.xlabel('样本 ID')
plt.ylabel('簇间距离 (欧式距离)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
