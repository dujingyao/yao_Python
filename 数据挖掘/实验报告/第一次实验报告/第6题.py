import pandas as pd

data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['张三', '李四', '王五', '赵六', '田七'],
    'sex': ['M', 'F', 'M', 'F', 'M'],
    'score': [85, 92, 78, 88, 90]
}
df = pd.DataFrame(data)
print(f"原始数据框:\n{df}")

# 修改引入新索引major，填充值为bigdata
# 通常在 DataFrame 中添加一列即为添加新列索引
df['major'] = 'bigdata'
print(f"添加 major 后的数据框:\n{df}")

# 按性别对其分组并统计每组score的平均值
grouped_avg = df.groupby('sex')['score'].mean()
print(f"按性别分组 score 平均值:\n{grouped_avg}")
