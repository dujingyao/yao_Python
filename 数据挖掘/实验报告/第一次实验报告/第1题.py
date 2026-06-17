import random

my_list = [10, 20, 30, 40, 50]
my_set = {1, 2, 3, 4, 5}

print(f"原始列表: {my_list}")
print(f"原始集合: {my_set}")

shuffled_list = my_list[:]
random.shuffle(shuffled_list)
print(f"乱序输出列表: {shuffled_list}")

popped_val = my_set.pop()
print(f"集合弹出元素: {popped_val}")
print(f"弹出后的集合: {my_set}")

dict1 = {'name': '张三', 'age': 20}
dict2 = {'age': 21, 'major': 'BigData'}
print(f"更新前字典1: {dict1}")
dict1.update(dict2)
print(f"更新后字典1: {dict1}")
