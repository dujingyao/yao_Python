import matplotlib.pyplot as plt
import numpy as np

# 第9题
# 自定义数据，绘制折线图，散点图，饼图，箱图和直方图。

x = np.arange(10)
y = np.random.randint(10, 100, 10)

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.subplot(2, 3, 1)
plt.plot(x, y, marker='o')
plt.title('Line Chart')

# 绘制散点图
plt.subplot(2, 3, 2)
plt.scatter(x, y, color='red')
plt.title('Scatter Plot')

# 绘制饼图
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
plt.subplot(2, 3, 3)
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')

# 绘制箱图
data_box = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.subplot(2, 3, 4)
plt.boxplot(data_box)
plt.title('Box Plot')

# 绘制直方图
data_hist = np.random.randn(1000)
plt.subplot(2, 3, 5)
plt.hist(data_hist, bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram')

plt.tight_layout()
plt.show()
