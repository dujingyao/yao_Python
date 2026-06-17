def quick_sort(arr, low, high):  # 定义快速排序主函数
    if low < high:  # 如果当前区间长度大于1（即low不等于high）
        pivot_idx = partition(arr, low, high)  # 进行分区操作，获取基准元素最终位置
        quick_sort(arr, low, pivot_idx - 1)  # 对基准左侧区间进行递归排序
        quick_sort(arr, pivot_idx + 1, high)  # 对基准右侧区间进行递归排序

def partition(arr, low, high):  # 定义核心的分区函数
    pivot = arr[high]  # 选取区间内最后一个元素作为基准值(pivot)
    i = low - 1  # i用于记录小于基准值的区域边界
    for j in range(low, high):  # 从low遍历到high-1
        if arr[j] < pivot:  # 如果当前元素小于基准值
            i += 1  # 边界i向右扩展一位
            arr[i], arr[j] = arr[j], arr[i]  # 交换元素，将其放入小于基准值的区域
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # 将基准值放到正确的分界位置
    return i + 1  # 返回基准值的最终正确索引位置

# ================= 测试代码 =================  # 测试分隔线
if __name__ == '__main__':  # 如果当前是被直接运行的主程序
    test_arr = [38, 27, 43, 3, 9, 82, 10]  # 初始化一个待排序测试数组
    print("原始数组:", test_arr)  # 打印输出原始数组的内容
    quick_sort(test_arr, 0, len(test_arr) - 1)  # 传入数组本身、起始索引0、结束索引(长度-1)执行排序
    print("排序后数组:", test_arr)  # 打印输出排序完成后的数组内容