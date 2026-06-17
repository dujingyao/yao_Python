def knapsack_01(W, wt, val, n):  # 定义0/1背包主函数（容量，重量表，价值表，物品数）
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]  # 初始化二维DP表并全置为0

    for i in range(1, n + 1):  # 遍历考虑前i个物品
        for w in range(1, W + 1):  # 遍历从小到大的背包容量w
            if wt[i - 1] <= w:  # 判断第i个物品（索引i-1）是否能装入当前容量w
                # 如果能装入，在“装”与“不装”之间取价值最大者
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:  # 如果当前容量w装不下第i个物品
                dp[i][w] = dp[i - 1][w]  # 只能选择不装，继承前i-1个物品最优解

    return dp[n][W]  # DP表右下角也就是所有物品在最大容量下的最大价值

# ================= 测试代码 =================  # 测试部分分隔线
if __name__ == '__main__':  # 如果作为主文件直接运行
    val_list = [60, 100, 120]  # 初始化各个物品的价值
    wt_list = [10, 20, 30]  # 初始化各个物品对应的重量
    max_weight = 50  # 初始化背包的最大承重限制
    item_count = len(val_list)  # 计算给定的物品总数量

    max_value = knapsack_01(max_weight, wt_list, val_list, item_count)  # 调用DP函数求解
    print(f"背包能装入的最大价值为: {max_value}")  # 打印最终计算出的最大价值结果