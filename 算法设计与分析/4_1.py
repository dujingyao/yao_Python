import sys

class TSP_Backtrack:
    def __init__(self, graph):
        self.graph = graph          # 图的邻接矩阵
        self.n = len(graph)         # 城市（节点）数量
        
        self.current_path = [0] * self.n  # 记录当前探索的路径
        self.best_path = [0] * self.n     # 记录历史最优路径
        self.visited = [False] * self.n   # 记录节点是否已被访问
        
        self.current_cost = 0             # 当前路径的总花费
        self.min_cost = sys.maxsize       # 最小总花费（初始为无穷大）
        
        # 初始化起点：默认从城市0出发
        self.visited[0] = True
        self.current_path[0] = 0

    def backtrack(self, step):
        """
        step 表示当前正在决定第 step 个要访问的城市 (从1开始)
        """
        # 1. 递归终止条件：所有城市都已访问过
        if step == self.n:
            last_city = self.current_path[step - 1]
            first_city = self.current_path[0]
            
            # 判断最后一个城市是否能回到起点
            if self.graph[last_city][first_city] != sys.maxsize:
                total_cost = self.current_cost + self.graph[last_city][first_city]
                # 更新最优解
                if total_cost < self.min_cost:
                    self.min_cost = total_cost
                    self.best_path = self.current_path.copy()
            return

        # 2. 遍历所有可能的下一个城市
        for i in range(1, self.n):
            last_visited = self.current_path[step - 1]
            
            # 检查条件：城市未被访问过 且 与上一个城市连通
            if not self.visited[i] and self.graph[last_visited][i] != sys.maxsize:
                
                # 3. 剪枝策略（核心）：如果当前开销已经大于已知最小开销，则无需继续向下探索
                if self.current_cost + self.graph[last_visited][i] < self.min_cost:
                    
                    # 4. 记录状态，进入下一层搜索
                    self.current_path[step] = i
                    self.visited[i] = True
                    self.current_cost += self.graph[last_visited][i]
                    
                    self.backtrack(step + 1)  # 递归探索
                    
                    # 5. 回溯操作：恢复上一个状态，尝试其他分支
                    self.current_cost -= self.graph[last_visited][i]
                    self.visited[i] = False
                    self.current_path[step] = 0

if __name__ == '__main__':
    INF = sys.maxsize
    
    # 定义一个带有4个城市的连通图的邻接矩阵（0表示自身，INF表示无直达路径）
    example_graph = [
        [0, 30, 6, 4],
        [30, 0, 5, 10],
        [6, 5, 0, 20],
        [4, 10, 20, 0]
    ]
    
    tsp = TSP_Backtrack(example_graph)
    # 从第1步（第二个城市）开始搜索，因为第0步固定为城市0
    tsp.backtrack(1) 
    
    print(f"旅行商问题最小开销: {tsp.min_cost}")
    
    # 组装最终闭合回路并输出
    best_route = tsp.best_path + [tsp.best_path[0]]
    print(f"最优旅行路线为: {' -> '.join(map(str, best_route))}")