'''
1、在区间 [-3, 3] 上生成200个均匀分布的随机数作为 x，基于函数 y = 0.5x³ - 2x² + 3x + 5 生成对应的 y 值，并添加均值为0、标准差为2的正态噪声。绘制散点图，并用红色曲线绘制真实的函数曲线（无噪声版本）。
要求：
x轴标签为 "X 值"，y轴标签为 "Y 值"
标题为 "带噪声的三次函数散点图"
散点用蓝色圆点表示，真实曲线用红色实线表示
添加图例区分数据点和真实曲线
'''
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 生成自变量 x 并【务必排序】
x = np.random.uniform(-3, 3, 200)
x.sort() 

# 2. 生成真实 y 和 带噪声的 y
y_true = 0.5 * x**3 - 2 * x**2 + 3 * x + 5
# 均值0，标准差2，200个点
noise = np.random.normal(loc=0.0, scale=2.0, size=200) 
y_noisy = y_true + noise

# 3. 极简画图
plt.figure(figsize=(8, 6))
plt.scatter(x, y_noisy, color='blue', label='数据点')
plt.plot(x, y_true, color='red', label='真实曲线')

plt.title("带噪声的三次函数散点图")
plt.xlabel("X 值")
plt.ylabel("Y 值")
plt.legend()
plt.show()