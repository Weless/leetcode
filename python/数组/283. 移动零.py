from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = nums.count(0)
        i = 0
        while i < len(nums):
            if i < len(nums)-c:
                for n in nums:
                    print(i,n)
                    if n != 0:
                        nums[i] = n
                        i+=1
            else:
                nums[i] = 0
                i+=1
        return nums

s = Solution()
nums = [0,1,0,3,12]
print(s.moveZeroes(nums))