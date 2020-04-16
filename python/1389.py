from typing import List
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i in range(len(index)):
            res.insert(index[i],nums[i])
        return res

s = Solution()
nums = [0,1,2,3,4]
index = [0,1,2,2,1]
print(s.createTargetArray(nums,index))


# better answer

# class Solution:
#     def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
#         res = []
#         for i, v in zip(index, nums):
#             res.insert(i, v)
#         return res