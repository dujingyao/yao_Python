import random

# 1. 列表、集合、字典操作
print("--- 第1题 ---")
# 构建列表和集合
my_list = [1, 2, 3, 4, 5]
my_set = {10, 20, 30, 40, 50}
print(f"原始列表: {my_list}")
print(f"原始集合: {my_set}")

# 将列表乱序输出
shuffled_list = my_list[:]
random.shuffle(shuffled_list)
print(f"乱序后的列表: {shuffled_list}")

# 将集合头部元素弹出 (集合无序，pop 弹出任意一个元素)
popped_element = my_set.pop()
print(f"弹出的集合元素: {popped_element}")
print(f"弹出后的集合: {my_set}")

# 创建两个字典，用字典2内容更新字典1内容
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(f"更新前的 dict1: {dict1}")
dict1.update(dict2)
print(f"更新后的 dict1: {dict1}")

# 2. 递归阶乘运算和5层汉诺塔递归
print("\n--- 第2题 ---")

def factorial(n):
    """递归阶乘"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def hanoi(n, a, b, c):
    """5层汉诺塔递归"""
    if n == 1:
        print(f"{a} -> {c}")
    else:
        hanoi(n - 1, a, c, b)
        print(f"{a} -> {c}")
        hanoi(n - 1, b, a, c)

print(f"5的阶乘: {factorial(5)}")
print("5层汉诺塔步骤 (A 为起始, B 为辅助, C 为目标):")
hanoi(5, 'A', 'B', 'C')
