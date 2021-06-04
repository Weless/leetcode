import functools
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return functools.reduce(lambda x,y:x^y,(start + 2*i for i in range(n)))

s = Solution()
print(s.xorOperation(4,3))