from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if nums == [] or k == 0:
            return []
        result = []
        i = 0
        while i < len(nums)-k+1:
            # print(nums[i:i+k])
            result.append(max(nums[i:i+k]))
            i+=1
        return result

s = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(s.maxSlidingWindow(nums,k))