from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 非递归, 常规做法
        def binarySearch(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
            return -1

        # 非递归, 返回左边界
        def binarySearchLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        # 非递归, 返回右边界
        def binarySearchRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        left = binarySearchLeft(nums, target)
        right = binarySearchRight(nums, target)
        if right - left == 1:
            return [-1, -1]
        return [left + 1, right - 1]

s = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(s.searchRange(nums,target))