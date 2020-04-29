# 非递归
def binarySearch(nums,target):
    left,right = 0,len(nums) -1
    while left <= right:
        mid = (left+right) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid -1
        elif nums[mid] <= target:
            left = mid + 1
    return -1

# 递归
def binarySearch2(nums,target):
    if len(nums) == 0:
        return -1
    mid = len(nums)//2
    if nums[mid] == target:
        return mid
    if target < nums[mid]:
        return binarySearch2(nums[:mid],target)
    else:
        return binarySearch2(nums[mid+1:],target)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch2(testlist, 3))
print(binarySearch2(testlist, 13))