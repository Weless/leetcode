from typing import List
# class Solution:
#     def decompressRLElist(self, nums: List[int]) -> List[int]:
#         l = len(nums)
#         i = 1
#         result = []
#         while i <= l:
#            result += [nums[i]] * nums[i-1]
#            i+=2
#         return result




s = Solution()
nums = [1,1,2,3]
print(s.decompressRLElist(nums))


### better answer

class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)//2):
            temp = []
            freq = nums.pop(0)
            value = nums.pop(0)
            temp = [value] * freq
            res.extend(temp)
        return res