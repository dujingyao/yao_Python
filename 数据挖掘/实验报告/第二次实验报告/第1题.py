import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
try:
	plt.rcParams.pop('font.sans-serif')
except Exception:
	pass
plt.rcParams['axes.unicode_minus'] = True


def main():
	# 1. 导入鸢尾花数据集
	iris = load_iris(as_frame=True)
	df = iris.frame

	# 将列名简化为 petal_length 和 petal_width
	df = df.rename(columns={
		'petal length (cm)': 'petal_length',
		'petal width (cm)': 'petal_width'
	})

	# 2. 随机采样展示10行数据
	sample10 = df[['petal_length', 'petal_width']].sample(n=10, random_state=42)
	print("随机采样的10行数据:\n", sample10)

	# 3. 预处理：选择两列，去除缺失，确保为浮点数
	data = df[['petal_length', 'petal_width']].dropna().astype(float)

	X = data[['petal_length']].values  # 形状 (n_samples, 1)
	y = data['petal_width'].values     # 形状 (n_samples,)

	# 4. 一元线性回归建模
	model = LinearRegression()
	model.fit(X, y)

	intercept = model.intercept_
	slope = model.coef_[0]
	print(f"回归方程: petal_width = {intercept:.4f} + {slope:.4f} * petal_length")
	print(f"截距(intercept): {intercept}")
	print(f"斜率(slope): {slope}")

	# 5. 根据回归模型预测 petal_length=4.0 时的 petal_width
	x_pred = np.array([[4.0]])
	y_pred = model.predict(x_pred)[0]
	print(f"当 petal_length=4.0 时, 预测的 petal_width = {y_pred:.4f}")

	# 6. 绘制散点图与回归线
	plt.figure(figsize=(8, 6))
	plt.scatter(X, y, color='blue', label='samples')

	x_line = np.linspace(X.min(), X.max(), 200).reshape(-1, 1)
	y_line = model.predict(x_line)
	plt.plot(x_line, y_line, color='red', linewidth=2, label='regression line')

	# English labels and title
	plt.xlabel('petal_length (cm)')
	plt.ylabel('petal_width (cm)')
	plt.title('Univariate Linear Regression: petal_length vs petal_width')
	plt.legend()
	plt.grid(True)
	plt.tight_layout()
	# save English-version image
	out_png = r"e:/Desktop/yao_Python/数据挖掘/实验报告/第二次实验报告/第1题_result.png"
	plt.savefig(out_png, dpi=150)


if __name__ == '__main__':
	main()

