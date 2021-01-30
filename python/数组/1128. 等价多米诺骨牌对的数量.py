from typing import List
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        nums = [0] * 100
        res = 0
        for x,y in dominoes:
            val = x*10+y if x < y else y*10+x
            res += nums[val]
            nums[val]+=1
        return res

