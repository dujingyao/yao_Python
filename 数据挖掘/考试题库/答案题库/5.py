'''
5、使用鸢尾花数据集（仅特征），采用层次聚类算法（AGNES）进行聚类，簇数设为3。使用ward连接方法，绘制树状图（dendrogram），并计算聚类结果的轮廓系数和调整兰德系数（与真实标签对比）。
要求：
使用 scipy.cluster.hierarchy 进行层次聚类
树状图设置合适的图形大小
在树状图上用红色虚线标出聚类为3的位置
'''
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score, adjusted_rand_score
# import load_datasets

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 拿数据
from sklearn.datasets import load_iris
X, y_true = load_iris(return_X_y=True)
# X, y_true = load_datasets.get_iris()

# 2. 画树状图 (Scipy登场)
plt.figure(figsize=(10, 6))
Z = sch.linkage(X, method='ward') # 算族谱
sch.dendrogram(Z)                 # 画树
plt.axhline(y=10, color='r', linestyle='--', label='截断线')
plt.title("鸢尾花数据集层次聚类树状图")
plt.legend()
plt.show()

# 3. 聚类并算分 (Sklearn登场)
agnes = AgglomerativeClustering(n_clusters=3, linkage='ward')
y_pred = agnes.fit_predict(X) # 终极偷懒二合一

print(f"轮廓系数: {silhouette_score(X, y_pred):.4f}")
print(f"调整兰德系数: {adjusted_rand_score(y_true, y_pred):.4f}")