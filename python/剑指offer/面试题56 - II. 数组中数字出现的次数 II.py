from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        c = Counter(nums)
        # print(c.most_common()[-1][0])
        return c.most_common()[-1][0]

s = Solution()
nums = [3,4,3,3]
print(s.singleNumber(nums))