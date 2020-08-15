arr = [54,26,93,17,77,31,44,55,20]
def quick_sort(left, right):
    if left >= right: return
    low, high = left, right
    target = arr[left]

    while left < right:
        # 找到右边第一个比pivot小的元素
        while left < right and target <= arr[right]: right -= 1
        arr[left] = arr[right]
        # 找到左边第一个比pivot大的元素
        while left < right and target >= arr[left]: left += 1
        arr[right] = arr[left]
    # 把pivot移到最终位置，此时，pivot左边的元素都比它小，右边的元素都比它大
    arr[left] = target
    # 递归处理剩下的元素
    quick_sort(low, left - 1)
    quick_sort(right + 1, high)

quick_sort(0,len(arr)-1)
print(arr)