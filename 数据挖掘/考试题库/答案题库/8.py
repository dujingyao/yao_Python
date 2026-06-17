'''
8、加载手写数字数据集（digits），仅使用特征进行聚类。使用高斯混合模型（GMM）进行聚类，簇数设为10。输出聚类后的标签（前20个），计算轮廓系数和调整兰德系数（与真实标签对比）。同时绘制BIC曲线，帮助选择最佳簇数（尝试簇数2-15）。
要求：
使用 sklearn.mixture.GaussianMixture
BIC曲线以簇数为横轴，BIC值为纵轴
标注BIC最小时对应的簇数
'''
import matplotlib.pyplot as plt
import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score, adjusted_rand_score
# import load_datasets

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

from sklearn.datasets import load_digits
X, y_true = load_digits(return_X_y=True)
# X, y_true = load_datasets.get_digits()

# --- 第一问：跑 10 簇并算分 (必须 fit_predict 出成绩单) ---
gmm_10 = GaussianMixture(n_components=10, random_state=42)
y_pred_10 = gmm_10.fit_predict(X) 
print("前20个标签:", y_pred_10[:20])
print(f"轮廓系数: {silhouette_score(X, y_pred_10):.4f}")
print(f"调整兰德系数: {adjusted_rand_score(y_true, y_pred_10):.4f}")

# --- 第二问：寻优并画图 (只需 fit 算代价) ---
n_range = range(2, 16)
bic_scores = []

for n in n_range:
    gmm = GaussianMixture(n_components=n, random_state=42)
    gmm.fit(X) 
    bic_scores.append(gmm.bic(X)) # 记下当前的罚单分数

# 找最低点
best_idx = np.argmin(bic_scores)
best_n = n_range[best_idx]
min_bic = bic_scores[best_idx]

plt.figure(figsize=(8, 6))
plt.plot(n_range, bic_scores, marker='o', label='BIC 曲线')
# 砸一个红点
plt.scatter([best_n], [min_bic], color='red', s=150, zorder=5, label='最佳簇数')

plt.title("GMM聚类的BIC曲线")
plt.xlabel("簇数")
plt.ylabel("BIC值")
plt.legend()
plt.show()