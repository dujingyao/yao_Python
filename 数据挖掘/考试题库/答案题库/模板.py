import matplotlib.pyplot as plt

# 解决中文显示问题 (每次画图必写)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 铺画布
plt.figure(figsize=(8, 6))

# 2. 画图形 (选其一)
plt.scatter(x, y, label='散点')   # 散点图
plt.plot(x, y, label='折线')      # 折线图
plt.bar(x, y, label='柱状')       # 柱状图

# 3. 加装饰
plt.title("这是标题")
plt.xlabel("X轴标签")
plt.ylabel("Y轴标签")
plt.legend() # 显示图例 (很重要，经常要求加)

# 4. 展示
plt.show()