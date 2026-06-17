import sys  # 导入sys模块，用于获取系统中的最大值（代表无穷大）

def prim_algorithm(graph, start_vertex):  # 定义Prim算法函数，接收邻接矩阵代表的网和起始遍历顶点
    num_vertices = len(graph)  # 获取图中顶点的总数量
    mst_edges = []  # 定义一个空列表，用于存储最终构成最小生成树的边
    visited = [False] * num_vertices  # 初始化一个布尔数组，记录每个顶点是否已经被加入到了最小生成树中
    
    visited[start_vertex] = True  # 将传入的起始顶点标记为已访问（加入到最小生成树的集合中）
    edges_count = 0  # 初始化已找到的边数计数器，最小生成树最终要包含 顶点数-1 条边

    while edges_count < num_vertices - 1:  # 循环条件：当收集到的边数小于 顶点数-1 时继续执行
        min_weight = sys.maxsize  # 初始化当前寻找的最小边权值为系统最大整数（充当正无穷）
        u = 0  # 初始化待添加边的起始顶点标识
        v = 0  # 初始化待添加边的目标顶点标识

        for i in range(num_vertices):  # 遍历所有的顶点，寻找目前已经在最小生成树集合中的顶点
            if visited[i]:  # 如果顶点i已经被包含在最小生成树的集合中
                for j in range(num_vertices):  # 再次遍历所有顶点，寻找不在集合中且与i相连的顶点
                    # 如果顶点j尚未加入集合，并且i到j之间存在边（假设graph[i][j]为0代表自身不用管）
                    if not visited[j] and graph[i][j]:  
                        if min_weight > graph[i][j]:  # 如果发现当前边(i,j)的权值比目前记录的最小权值还要小
                            min_weight = graph[i][j]  # 将最小权值更新为当前边(i,j)的权值
                            u = i  # 记录下这条最小权值边的起始点
                            v = j  # 记录下这条最小权值边的终点

        mst_edges.append((u, v, min_weight))  # 在内部双层循环结束后，将找到的权值最小的那条边存入结果列表
        visited[v] = True  # 将刚找到的这条最小边的目标顶点v标记为已访问（加入最小生成树集合）
        edges_count += 1  # 成功找到一条边，边数计数器加1

    return mst_edges  # 循环结束（所有的顶点均被连通），返回包含所有最小生成树边的列表

if __name__ == '__main__':  # 如果当前脚本是作为主程序运行
    INF = sys.maxsize  # 定义一个INF变量表示两点间不可达的无穷大距离
    
    # 定义测试图的邻接矩阵二维数组（0表示自身，INF表示无边连接，其他数字代表权重）
    # 该图共有5个顶点（索引0到4）
    example_graph = [  # 开始定义邻接矩阵
        [0, 2, 3, 3, INF],  # 顶点0到其他点(0,1,2,3,4)的边的权重
        [2, 0, 4, INF, 3],  # 顶点1到其他点(0,1,2,3,4)的边的权重
        [3, 4, 0, 5, 1],    # 顶点2到其他点(0,1,2,3,4)的边的权重
        [3, INF, 5, 0, 6],  # 顶点3到其他点(0,1,2,3,4)的边的权重
        [INF, 3, 1, 6, 0]   # 顶点4到其他点(0,1,2,3,4)的边的权重
    ]  # 结束定义邻接矩阵

    result_mst = prim_algorithm(example_graph, 0)  # 调用prim算法，以节点0作为起始构建最小生成树
    
    print("Edge \tWeight")  # 打印表头：边和对应的权重
    for edge in result_mst:  # 遍历上面返回的最小生成树边列表
        print(f"{edge[0]} - {edge[1]} \t{edge[2]}")  # 格式化输出： 起点 - 终点    权重