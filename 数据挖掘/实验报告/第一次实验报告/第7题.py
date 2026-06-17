import pandas as pd
import numpy as np
import os

# 第7题
# 创建excel文件并读取其内容至jupyter,对其各行求和后导出为csv文件
# 这里我们在本地模拟这个过程。
file_path_excel = "student_scores.xlsx"
df_data = pd.DataFrame({
    'id': [1, 2, 3],
    'math': [90, 80, 70],
    'english': [85, 95, 75]
})

# 保存为 excel 文件
df_data.to_excel(file_path_excel, index=False)
print(f"Excel文件 {file_path_excel} 已创建。")

# 读取其内容
df_read = pd.read_excel(file_path_excel)
print(f"读取到的数据:\n{df_read}")

# 对其各行求和（假设对 math 和 english 求和）
df_read['total'] = df_read[['math', 'english']].sum(axis=1)
print(f"求和后的结果:\n{df_read}")

# 导出为 csv 文件
file_path_csv = "student_scores_sum.csv"
df_read.to_csv(file_path_csv, index=False)
print(f"CSV文件 {file_path_csv} 已导出。")
