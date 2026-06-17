import pandas as pd

# 5. 创建两个索引长度为 4 的字典，使用字典 1 和字典 2 创建 Series 序列 S1 和 S2, 并对 S1 和 S2 做加法运算，解释结果。
print("--- 第5题 ---")
dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
dict2 = {"b": 10, "c": 20, "d": 30, "e": 40}
s1 = pd.Series(dict1)
s2 = pd.Series(dict2)
s3 = s1 + s2
print(f"S1:\n{s1}")
print(f"S2:\n{s2}")
print(f"S1 + S2 结果:\n{s3}")
# 解释：对齐索引，相同索引做加法，不同索引产生缺失值 NaN。

# 6. 创建数据框，索引为 id, name, sex 和 score，用此索引描述 5 名学生的信息。修改引入新索引 major，填充值为 bigdata。按性别对其分组并统计每组 score 的平均值。
print("\n--- 第6题 ---")
# 创建数据框
data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'sex': ['F', 'M', 'M', 'M', 'F'],
    'score': [85, 90, 78, 92, 88]
}
df = pd.DataFrame(data)
print(f"原始数据框:\n{df}")

# 修改引入新索引 major, 填充值为 bigdata
df['major'] = 'bigdata' # 这里通常指添加新列
# 如果题目指的是修改列索引
print(f"添加 major 列后的数据框:\n{df}")

# 按性别对其分组并统计每组 score 的平均值
grouped_mean = df.groupby('sex')['score'].mean()
print(f"按性别分组的 score 平均值:\n{grouped_mean}")
