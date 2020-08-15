arr = [54,26,93,17,77,31,44,55,20]
def fast_sort(l, r):
    if l >= r: return
    i, j = l, r
    pivot = arr[l]
    while i < j:
        # 找到右边第一个比pivot小的元素
        while i < j and arr[j] >= pivot : j -= 1
        # 找到左边第一个比pivot大的元素
        while i < j and arr[i] <= pivot : i += 1
        # 交换两元素
        arr[i], arr[j] = arr[j], arr[i]
    # 把pivot移到最终位置，此时，pivot左边的元素都比它小，右边的元素都比它大
    arr[i], arr[l] = arr[l], arr[i]
    # 递归处理剩余部分
    fast_sort(l, i - 1)
    fast_sort(i + 1, r)
fast_sort(0,len(arr)-1)
print(arr)

