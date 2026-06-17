# 第2题

def factorial_recursive(n):
    """递归阶乘运算"""
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def hanoi_recursive(n, source, auxiliary, target):
    """5层汉诺塔递归"""
    if n == 1:
        print(f"移动盘子 1: {source} -> {target}")
        return
    hanoi_recursive(n - 1, source, target, auxiliary)
    print(f"移动盘子 {n}: {source} -> {target}")
    hanoi_recursive(n - 1, auxiliary, source, target)

if __name__ == "__main__":
    n_fact = 5
    print(f"{n_fact} 的阶乘是: {factorial_recursive(n_fact)}")
    
    print("\n5层汉诺塔递归步骤:")
    hanoi_recursive(5, 'A', 'B', 'C')
