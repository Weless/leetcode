# 合并两个有序数组
def merge(nums, start, mid, end):
    i, j, temp = start, mid + 1, []
    while i <= mid and j <= end:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1
    while i <= mid:
        temp.append(nums[i])
        i += 1
    while j <= end:
        temp.append(nums[j])
        j += 1
    for i in range(len(temp)):
        nums[start + i] = temp[i]


def mergeSort(nums, start, end):
    if start >= end: return
    mid = (start + end) >> 1 # mid = (start+end)//2
    mergeSort(nums, start, mid)
    mergeSort(nums, mid + 1, end)
    merge(nums, start, mid, end)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist,0,len(alist)-1)
print(alist)