from typing import List

# 双指针法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j = 0,len(nums)-1
        while i<j:
            if nums[j] > target:
                j-=1
                continue
            if nums[i] + nums[j] > target:
                j-=1
            elif nums[i] + nums[j] < target:
                i+=1
            else:
                return [nums[i],nums[j]]
        return []


# python 集合
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums = set(nums) #集合的好处在此，此处是列表就会超时，O(n)和O(n**2)
#         if len(nums) <= 1:
#             return []
#         for i in nums:
#             if target - i in nums:
#                 return [i, target - i]
#         return []

s = Solution()
nums = [2,7,11,15]
target = 9
print(s.twoSum(nums,target))
