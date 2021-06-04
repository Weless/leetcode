from typing import List
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        s = 0 # 负数
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                s+=1
        return 1 if s%2==0 else -1