import sys

def matrix_chain_order(p):
    n = len(p) - 1  # 矩阵的总个数
    
    # m[i][j] 记录计算矩阵 A[i..j] 所需的最少乘法次数，初始为0
    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    # s[i][j] 记录子问题 A[i..j] 的最优划分点 k
    s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # L 是矩阵链的长度，从2个矩阵连乘一直算到n个矩阵连乘
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i][j] = sys.maxsize  # 初始化当前子问题的结果为无穷大
            
            # 尝试在 i 到 j 之间找一个划分点 k，将问题分为 A[i..k] 和 A[k+1..j]
            for k in range(i, j):
                # q = 左半部分代价 + 右半部分代价 + 两部分相乘的代价
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                
                # 如果当前花费 q 更小，记录最优解和最佳切割点
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
                    
    return m, s

def print_optimal_parens(s, i, j):
    """递归打印最优括号化方案"""
    if i == j:  # 基本情况：单个矩阵无需加括号
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])      # 打印左边括号组合
        print_optimal_parens(s, s[i][j] + 1, j)  # 打印右边括号组合
        print(")", end="")

if __name__ == '__main__':
    # 数组 p 存储矩阵维数。例如：6个矩阵 
    # A1(30x35), A2(35x15), A3(15x5), A4(5x10), A5(10x20), A6(20x25)
    p = [30, 35, 15, 5, 10, 20, 25]
    
    m, s = matrix_chain_order(p)
    n = len(p) - 1
    
    print(f"最少乘法次数为: {m[1][n]}")
    print("最优连乘括号化方案: ", end="")
    print_optimal_parens(s, 1, n)
    print()