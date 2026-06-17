import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

# 1. 加载数据集
iris = datasets.load_iris()
X = iris.data[:, :2]

# 2. 构建KMeans模型并进行训练
# iris数据集已知有3个类别，故n_clusters设为3
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# 3. 获取聚类结果和聚类中心
label = kmeans.labels_
centroids = kmeans.cluster_centers_

# 4. 可视化聚类结果
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

plt.figure(figsize=(8, 6))

# 绘制不同类别的数据点
plt.scatter(X[:, 0], X[:, 1], c=label, cmap='viridis', marker='o', edgecolors='k', alpha=0.8)
# 绘制聚类中心
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=200, linewidths=3, label='聚类中心')

plt.title('KMeans 聚类结果 (Iris 数据集)')
plt.xlabel('萼片长度 (Sepal Length)')
plt.ylabel('萼片宽度 (Sepal Width)')
plt.legend()
plt.grid(True)
plt.show()