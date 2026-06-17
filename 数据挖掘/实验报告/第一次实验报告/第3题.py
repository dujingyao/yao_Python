import numpy as np

# 第3题
# 使用numpy随机生成一个长度为12的乱序数组,更改其维度为3行4列
arr1 = np.arange(12)
np.random.shuffle(arr1)
arr1 = arr1.reshape(3, 4)
print(f"数组1 (3x4):\n{arr1}")

# 在随机生成一个长度为16的，满足正态分布的乱序数组，更改其维度为4行4列
arr2 = np.random.randn(16).reshape(4, 4)
print(f"数组2 (4x4, 正态分布):\n{arr2}")

arr1_t = arr1.T                      # (4,3)
new_col = np.zeros((arr1_t.shape[0], 1))  # (4,1)
arr1_expanded = np.hstack([arr1_t, new_col])  # (4,4)
result = arr1_expanded + arr2
print(result)