from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 0:
            return 0
        import random
        result = random.sample(range(0,1000),n-1)
        result.append(-1*sum(result))
        return result

s = Solution()
print(s.sumZero(4))