'''
11、已知某电商平台2025年四个季度的销售额数据（单位：万元）：
电子产品：[120, 145, 168, 192]
服装：[85, 92, 108, 125]
家居用品：[63, 71, 89, 104]
绘制面积填充图（stackplot），展示三类商品销售额的季度变化趋势及累计贡献。x轴为季度（Q1, Q2, Q3, Q4），y轴为销售额。
要求：
三类商品使用不同颜色填充，设置透明度0.6
添加图例，位置为左上角
标题为 "2025年各品类季度销售额趋势"
在图表上方标注每个季度的总销售额
'''
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']

quarters = ['Q1', 'Q2', 'Q3', 'Q4']
electronics = [120, 145, 168, 192]
clothing = [85, 92, 108, 125]
home_goods = [63, 71, 89, 104]

# 一秒钟求出四个季度的各自总和
data_matrix = np.array([electronics, clothing, home_goods])
totals = data_matrix.sum(axis=0) 

plt.figure(figsize=(9, 6))
plt.stackplot(quarters, electronics, clothing, home_goods, 
              labels=['电子产品', '服装', '家居用品'], alpha=0.6)

# 拉高天花板，防止最上面的数字被砍头
plt.ylim(0, max(totals) + 50) 

# 在每个季度色块最顶端写字
for i in range(len(quarters)):
    plt.text(quarters[i], totals[i] + 5, str(totals[i]), ha='center')

plt.title("2025年各品类季度销售额趋势")
plt.legend(loc='upper left')
plt.show()