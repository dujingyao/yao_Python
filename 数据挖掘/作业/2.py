import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']   # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False     # 正常显示负号

# 数据准备
x = [1, 2, 3, 4, 5, 6, 7]
y1 = [71, 73, 52, 66, 74, 82, 71]
y2 = [68, 70, 69, 72, 71, 70, 66]
y3 = [82, 83, 82, 76, 84, 92, 81]

# 创建画布
plt.figure(figsize=(10, 6))

# 绘制多条折线图，指定不同颜色 (color) 和不同点标记 (marker)
plt.plot(x, y1, color='red', marker='o', label='商品 1')
plt.plot(x, y2, color='green', marker='s', label='商品 2')
plt.plot(x, y3, color='blue', marker='^', label='商品 3')

# 添加标题和坐标轴标签
plt.title('三种商品不同月份的销售量走势')
plt.xlabel('月份')
plt.ylabel('销售量')

# 添加图例，自动识别 label
plt.legend()

# 开启网格线，使图表更加美观
plt.grid(True, linestyle='--', alpha=0.6)

# 显示图表
plt.show()
