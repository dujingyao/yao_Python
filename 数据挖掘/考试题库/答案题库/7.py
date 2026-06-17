'''
7、加载波士顿房价数据集，按8:2划分训练集和测试集，使用岭回归（Ridge）建模。通过交叉验证选择最优的正则化参数α（候选值：[0.01, 0.1, 1, 10, 100]），输出最优α值及对应的测试集均方误差（MSE）。绘制预测值与真实值的散点对比图。
要求：
使用 RidgeCV 进行交叉验证
预测值与真实值散点图中添加 y=x 参考线
计算并输出 R² 分数
'''
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import RidgeCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
# import load_datasets

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

from sklearn.datasets import fetch_openml
boston = fetch_openml(data_id=531, as_frame=True, parser='auto')
X, y = boston.data, boston.target
# X, y = load_datasets.get_boston()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 标准化不能忘
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 自动挑选最佳参数并预测
ridge_cv = RidgeCV(alphas=[0.01, 0.1, 1, 10, 100], cv=5)
ridge_cv.fit(X_train_scaled, y_train)
y_pred = ridge_cv.predict(X_test_scaled)

print(f"最优 α: {ridge_cv.alpha_}")
print(f"MSE: {mean_squared_error(y_test, y_pred):.4f}")
print(f"R²: {r2_score(y_test, y_pred):.4f}")

# 画图与辅助线
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, label='预测点')

# 提取极小极大值，连成一条 y=x 直线
min_val = min(y_test.min(), y_pred.min())
max_val = max(y_test.max(), y_pred.max())
plt.plot([min_val, max_val], [min_val, max_val], 'r--', label='y=x 参考线')

plt.title("波士顿房价预测对比")
plt.xlabel("真实房价")
plt.ylabel("预测房价")
plt.legend()
plt.show()