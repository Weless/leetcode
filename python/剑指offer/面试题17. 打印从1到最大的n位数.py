from typing import List

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        import itertools
        bit = 1
        for _ in range(n):
            bit *= 10

        return list(range(1,bit))

s =  Solution()
print(s.printNumbers(1))
