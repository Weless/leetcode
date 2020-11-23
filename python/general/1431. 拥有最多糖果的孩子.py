
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        i = 0
        while i< len(candies):
            candies[i] += extraCandies
            if candies[i] >= max(candies):
                res.append(True)
            else:
                res.append(False)
            candies[i] -= extraCandies
            i+=1
        return res


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = max(candies)
        i = 0
        res = []
        while i < len(candies):
            if max_value - candies[i] <= extraCandies:
                res.append(True)
            else:
                res.append(False)
            i+=1
        return res

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = max(candies)
        res = [max_value-candies[i]<=extraCandies for i in range(len(candies))]

        return res