from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        i = 0
        while i < n:
            res.append(nums[i])
            res.append(nums[n+i])
            i+=1
        return res

s = Solution()
nums = [2,5,1,3,4,7]
n = 3
print(s.shuffle(nums,n))