from typing import List

# 解法1：
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j=0,0
        while j<len(nums):
            if nums[j] == val:
                j+=1
            else:
                nums[i] = nums[j]
                i+=1
                j+=1
        return len(nums)

# 解法2：
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,n=0,len(nums)
        while i<n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n-=1
            else:
                i+=1
        return n