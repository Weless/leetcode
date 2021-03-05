from typing import List
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] *(num+1)
        for i in range(num+1):
            res[i] = self.count(i)
        return res
    def count(self, a):
        n = 0
        while a:
            a = a & (a-1)
            n+=1
        return n
s = Solution()
print(s.countBits(5))