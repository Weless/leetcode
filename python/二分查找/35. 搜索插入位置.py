from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i,j = 0,len(nums)-1
        while i<=j:
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target: i = mid + 1
            else: j = mid -1
        # 找不到的位置即为插入位置
        return i