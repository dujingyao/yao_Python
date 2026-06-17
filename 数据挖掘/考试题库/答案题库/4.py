'''
4、加载葡萄酒数据集，按7.5:2.5划分训练集和测试集，构建随机森林分类模型（n_estimators=100, max_depth=5）。输出测试集的分类准确率，并绘制特征重要性条形图（按重要性从高到低排序）。
要求：
计算并输出每个特征的重要性分数
条形图标题为 "葡萄酒数据集特征重要性"
x轴为特征名称，y轴为重要性分数
'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# import load_datasets

plt.rcParams['font.sans-serif'] = ['SimHei']

# 1. 拿数据
from sklearn.datasets import load_wine
wine = load_wine()
X, y, feature_names = wine.data, wine.target, wine.feature_names
# 如果老师的脚本不带特征名，自己捏造一个：
# X, y = load_datasets.get_wine()
# feature_names = [f"特征{i}" for i in range(X.shape[1])]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 2. 训练与预测
rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
print(f"准确率: {accuracy_score(y_test, y_pred):.4f}")

# 3. 提取重要性并排序
importances = rf.feature_importances_
indices = np.argsort(importances)[::-1] # 倒序排好

# 4. 画条形图
plt.figure(figsize=(10, 6))
# x轴放 0到12，y轴放排好序的分数
plt.bar(range(X.shape[1]), importances[indices])
# 替换 x 轴数字为文字，倾斜防重叠
plt.xticks(range(X.shape[1]), [feature_names[i] for i in indices], rotation=45, ha='right')

plt.title("葡萄酒数据集特征重要性")
plt.tight_layout() # 防止文字被切断
plt.show()