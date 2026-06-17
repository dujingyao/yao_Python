'''
2、使用NumPy随机生成一个5×5的数组，数据服从均值为50、标准差为15的正态分布。对该数组进行Z-score标准化（即减去均值后除以标准差），分别输出标准化前和标准化后每行的均值、方差。
要求：
随机种子固定为 123
输出格式清晰，区分标准化前后的结果
使用 NumPy 实现标准化，不使用 sklearn
'''
import numpy as np

# 固定随机种子
np.random.seed(123)
data = np.random.normal(loc=50, scale=15, size=(5, 5))

print("=== 标准化前 ===")
print("每行均值:\n", np.mean(data, axis=1)) # axis=1 算行
print("每行方差:\n", np.var(data, axis=1))

# --- 安全分步计算标准化 (针对列 axis=0) ---
mean_cols = np.mean(data, axis=0)  # 第一步：算列均值
std_cols = np.std(data, axis=0)    # 第二步：算列标准差
data_scaled = (data - mean_cols) / std_cols  # 第三步：套公式

print("=== 标准化后 ===")
print("每行均值:\n", np.mean(data_scaled, axis=1))
print("每行方差:\n", np.var(data_scaled, axis=1))
