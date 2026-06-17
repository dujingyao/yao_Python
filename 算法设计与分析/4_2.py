import heapq  # 导入堆模块，用于实现优先队列
import sys  # 导入sys模块，获取最大值常量

def get_bound(graph, path, n):  # 定义计算下界的辅助函数
    bound = 0  # 初始化预测的额外路费为0
    for i in range(n):  # 遍历所有的城市
        if i not in path[:-1]:  # 如果城市属于未访问节点或是当前终点
            min_edge = sys.maxsize  # 初始化最小出边为无穷大
            for j in range(n):  # 遍历相邻的目标城市
                if i != j and graph[i][j] < min_edge:  # 寻找连通且权值最小的出边
                    min_edge = graph[i][j]  # 更新该城市的最小出边记录
            bound += min_edge  # 累加这些城市的最小出边作为估算下界
    return bound  # 返回这部分预测的最低额外路费

def tsp_bab(graph):  # 定义分支限界法求TSP主函数
    n = len(graph)  # 获取总城市数量
    min_cost = sys.maxsize  # 初始化最小总花费为无穷大
    best_path = []  # 初始化最优路径为空列表

    pq = []  # 创建一个空列表用于做优先队列
    init_bound = get_bound(graph, [0], n)  # 计算仅包含起点时的下界预测
    heapq.heappush(pq, (init_bound, 0, 1, [0]))  # 插入初始状态：(下界, 花费, 层数, 路径)

    while pq:  # 当队列中还有状态未探索完时循环
        bound, cost, level, path = heapq.heappop(pq)  # 弹出目前下界最小的状态优先探索

        if bound >= min_cost:  # 如果当前分支最优情况都不及已知的最小花费
            continue  # 剪枝操作，直接跳过并丢弃该分支

        if level == n:  # 如果路径层数达到了城市总数（已经走完所有城市）
            last_city = path[-1]  # 获取最后停留的那个城市
            return_cost = graph[last_city][0]  # 获取直接回起点的路费
            if return_cost != sys.maxsize:  # 如果最后那个城市有路能回起点
                if cost + return_cost < min_cost:  # 且加上回程路费后刷新了最小纪录
                    min_cost = cost + return_cost  # 更新最小花费的新纪录
                    best_path = path + [0]  # 记录对应的具体闭环路线
            continue  # 结束当前分支，继续评估队列里的其他分支

        curr_city = path[-1]  # 获取此时所在的最新一步城市
        for next_city in range(n):  # 尝试往其他所有城市走
            if next_city not in path:  # 要求目标城市在此前还没去过
                edge_cost = graph[curr_city][next_city]  # 查询当前城市前往目的地的路费
                if edge_cost != sys.maxsize:  # 如果两地直接相连（有路）
                    new_cost = cost + edge_cost  # 累加得出新一条路的总花费
                    new_path = path + [next_city]  # 追加新城市组成新的路线方案
                    new_bound = new_cost + get_bound(graph, new_path, n)  # 预测新路线的理论底线
                    if new_bound < min_cost:  # 如果新预测底线还存在破纪录的潜力
                        heapq.heappush(pq, (new_bound, new_cost, level + 1, new_path))  # 压入队列等待日后探索

    return min_cost, best_path  # 全部队列评估完毕，返回确定的全局最优解

if __name__ == '__main__':  # 如果此文件作为主程序启动
    INF = sys.maxsize  # 定义无穷大变量表示两地断路
    test_graph = [  # 构建测试用的距离邻接矩阵
        [0, 30, 6, 4],     # 城市0距离其余城市的里程
        [30, 0, 5, 10],    # 城市1距离其余城市的里程
        [6, 5, 0, 20],     # 城市2距离其余城市的里程
        [4, 10, 20, 0]     # 城市3距离其余城市的里程
    ]  # 数组数据输入完毕
    
    ans_cost, ans_path = tsp_bab(test_graph)  # 执行分支限界函数并获取结果
    print(f"最小开销: {ans_cost}")  # 输出最低路费开销
    print(f"最优路线: {ans_path}")  # 输出这趟路费对应的走法