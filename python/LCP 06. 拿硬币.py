from typing import List
class Solution:
    def minCount(self, coins: List[int]) -> int:
        import math
        count = 0
        for item in coins:
            count += math.ceil(item/2)
        return count