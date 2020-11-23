from typing import List
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0
        i,j = 0,1
        res = 0
        while i < len(nums) and j < len(nums):
            if nums[j] > nums[i]: j+=1
            else:
                res = max(res,j-i)
                i = j
                j +=1
        if res == 0:
            res = max(res,j-i)
        return res


s = Solution()
nums = [1,3,5,4,7]
print(s.findLengthOfLCIS(nums))
