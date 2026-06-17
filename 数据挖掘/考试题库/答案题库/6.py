'''
6、加载乳腺癌数据集，使用PCA将特征降维至2维。绘制散点图，x轴为第一主成分，y轴为第二主成分，不同类别使用不同颜色和标记区分。计算并输出前两个主成分的解释方差比（累计贡献率）。
要求：
标题为 "乳腺癌数据PCA降维可视化"
添加图例（良性/恶性）
输出累计贡献率，格式为 "前2个主成分累计贡献率：XX.XX%"
'''
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
# import load_datasets

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

from sklearn.datasets import load_breast_cancer
X, y = load_breast_cancer(return_X_y=True)
# X, y = load_datasets.get_breast_cancer()

# 1. 生死线：必须标准化！
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. 降成两维
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# 3. 算累计贡献率
ratio = sum(pca.explained_variance_ratio_) * 100
print(f"前2个主成分累计贡献率：{ratio:.2f}%")

# 4. 画图：布尔索引强行挑人，干掉 for 循环
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[y==0, 0], X_pca[y==0, 1], color='red', marker='o', label='恶性')
plt.scatter(X_pca[y==1, 0], X_pca[y==1, 1], color='green', marker='s', label='良性')

plt.title("乳腺癌数据PCA降维可视化")
plt.xlabel("第一主成分")
plt.ylabel("第二主成分")
plt.legend()
plt.show()