import numpy as np

print("=" * 50)
print("第3题：NumPy数组运算")
print("=" * 50)
# ===== 第3题内容 =====
# 使用numpy随机生成一个长度为12的乱序数组，更改其维度为3行4列
arr1 = np.arange(12)
np.random.shuffle(arr1)
arr1 = arr1.reshape(3, 4)
print(f"数组1 (3x4):\n{arr1}")

# 随机生成一个长度为16的，满足正态分布的乱序数组，更改其维度为4行4列
arr2 = np.random.randn(16).reshape(4, 4)
print(f"\n数组2 (4x4, 正态分布):\n{arr2}")

# 对数组1转置后再扩充一列变为 (4x4)
arr1_t = arr1.T  # (4,3)
new_col = np.zeros((arr1_t.shape[0], 1))  # (4,1)
arr1_expanded = np.hstack([arr1_t, new_col])  # (4,4)
print(f"\n数组1转置并扩充一列后(4x4):\n{arr1_expanded}")

# 与数组2做ufunc加法运算
result_3 = arr1_expanded + arr2
print(f"\nufunc 加法运算结果 (第3题输出):\n{result_3}")

print("\n" + "=" * 50)
print("第4题：对第3题结果进行处理")
print("=" * 50)
# ===== 第4题内容：直接使用第3题的 result_3 =====
# 将第3题中的结果按列进行重复输出结果 (重复2次)
repeated_result = np.repeat(result_3, 2, axis=1)
print(f"按列重复后的结果 (2次重复) - shape {repeated_result.shape}:\n{repeated_result}")

# 将输出的结果拉平为一维数组后去除重复元素并输出
flattened = repeated_result.flatten()
unique_values = np.unique(flattened)
print(f"\n拉平并去重后的结果:\n{unique_values}")
print(f"去重后共 {len(unique_values)} 个唯一元素")
