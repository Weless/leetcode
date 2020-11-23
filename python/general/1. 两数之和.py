from typing import List

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for index in range(len(nums)):
            for index2 in range(index+1,len(nums)):
                if nums[index] + nums[index2] == target:
                    result.extend([index,index2])
        return result


s = Solution()
nums = [3,2,4]
target = 6
print(s.twoSum(nums,target))