import pandas as pd

# 第5题
# 创建两个索引长度为4的字典
dict1 = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
dict2 = {'b': 1, 'c': 2, 'd': 3, 'e': 4}

# 使用字典1和字典2创建Series序列S1和S2
s1 = pd.Series(dict1)
s2 = pd.Series(dict2)

# 并对S1和S2做加法运算
result_4 = s1 + s2
print(f"S1:\n{s1}")
print(f"S2:\n{s2}")
print(f"S1 + S2 结果:\n{result_4}")

# 解释结果：
# pandas 的 Series 加法是基于索引对齐的。
# 只有当两个 Series 中都存在该索引（如 b, c, d）时，才会相加。
# 只有一个 Series 存在的索引（如 a, e）加法结果为 NaN (Not a Number)。
