import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 加载数据集
iris = datasets.load_iris()
# 为了方便可视化二维决策边界，选取前两个特征
X = iris.data[:, :2] 
y = iris.target

# 2. 划分训练集和测试集（90%训练，10%测试）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# 3. 建立KNN模型，K=3
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# 4. 预测与评估
y_pred = knn.predict(X_test)
print("KNN分类准确率:", accuracy_score(y_test, y_pred))
print("\n测试集相关评分:\n", classification_report(y_test, y_pred, target_names=iris.target_names))

# 5. 可视化
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

# 生成网格点
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

# 预测网格点的分类
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(12, 5))

# 图1：决策边界
plt.subplot(1, 2, 1)
plt.pcolormesh(xx, yy, Z, cmap=cmap_light, shading='auto')
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=20)
plt.title("KNN (K=3) 决策边界")
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

# 图2：预测结果图
plt.subplot(1, 2, 2)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cmap_bold, edgecolor='k', s=50, label='真实值')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, marker='x', cmap=cmap_bold, s=50, label='预测值')
plt.title("测试集预测结果")
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.legend()

plt.tight_layout()
plt.show()