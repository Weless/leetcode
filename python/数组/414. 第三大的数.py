from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        MIN = float('-inf')
        a,b,c = MIN,MIN,MIN
        for i in nums:
            if i == a or i == b or i == c:
                continue
            if i > a:
                a,b,c=i,a,b
            elif i > b:
                b,c = i,b
            elif i > c:
                c = i
        if c == MIN:
            return a
        return c