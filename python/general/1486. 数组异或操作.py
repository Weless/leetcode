class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= start + 2*i
        return res
s = Solution()
n = 10
start = 5
print(s.xorOperation(n,start))