from typing import List
import collections
from functools import reduce
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(x,y):
            return y if x == 0 else gcd(y%x,x)
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2


s = Solution()
deck = [1,2,3,4,4,3,2,1]
print(s.hasGroupsSizeX(deck))