from typing import List
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                d[nums[i]*nums[j]]+=1
                j+=1
            i+=1
        # print(d.items())
        res = 0
        for v in d.values():
            res += v * (v-1) //2
        return res * 8

s = Solution()
nums = [2,3,4,6,8,12]
print(s.tupleSameProduct(nums))