from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left,right=0,k-1
        t = sum(nums[left:k])
        max_num = t
        start = True
        while right < len(nums):
            if not start:
                t = t-nums[left-1]+nums[right]
            max_num = max(max_num,t)
            right += 1
            left += 1
            start = False
        return max_num/k
s = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
print(s.findMaxAverage(nums,k))