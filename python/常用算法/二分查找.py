from bisect import bisect_right,bisect_left

# 非递归, 常规做法
def binarySearch(nums,target):
    left,right = 0,len(nums) -1
    while left <= right:
        mid = (left+right) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid -1
        elif nums[mid] < target:
            left = mid + 1
    return -1

# 非递归, 返回左边界
def binarySearch2(nums,target):
    left,right = 0,len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return right

# 非递归, 返回右边界
def binarySearch3(nums,target):
    left,right = 0,len(nums)- 1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# 递归
def binarySearch4(nums,target):
    if len(nums) == 0:
        return -1
    mid = len(nums)//2
    if nums[mid] == target:
        return mid
    if target < nums[mid]:
        return binarySearch2(nums[:mid],target)
    else:
        return binarySearch2(nums[mid+1:],target)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 32, 32, 32, 32, 32, 42,]
testlist2 = [5,7,8,8,10]
# print(binarySearch(testlist, 3))
print(binarySearch2(testlist2, 8))
print(bisect_left(testlist2,32))
print(bisect_right(testlist2,32))