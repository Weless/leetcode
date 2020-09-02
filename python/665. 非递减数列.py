from typing import List
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            A = nums[:i]
            B = nums[i+1:]
            if self.isSorted(A) and self.isSorted(B):
                if len(A) == 0 and len(B) == 0:
                    return True
                if len(A) == 0 or len(B) == 0:
                    return True
                if A[-1] <= B[0]:
                    return True
        return False

    def isSorted(self,nums):
        if not nums or len(nums) == 1:
            return True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
        return True

s = Solution()
nums = [5,7,1,8]
print(s.checkPossibility(nums))