def merge_sort(arr):
    # 基本情况：如果数组长度小于等于1，则认为是有序的，直接返回
    if len(arr) <= 1:
        return arr

    # 1. 拆分：找到数组的中点，将数组分为左右两半
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 对左右两半分别递归调用合并排序
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # 2. 合并：将两个已排序的子数组合并为一个有序数组
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    # 比较左右两个子数组的元素，将较小的元素加入结果数组
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # 将左边或右边剩余的元素（如果有）全部追加到结果数组末尾
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

# ================= 测试代码 =================
if __name__ == '__main__':
    test_arr = [38, 27, 43, 3, 9, 82, 10]
    print("原始数组:", test_arr)
    
    sorted_result = merge_sort(test_arr)
    print("排序后数组:", sorted_result)