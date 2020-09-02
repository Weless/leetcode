class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        res = m
        for i in range(m,n+1):
            res &= i
        return res

s = Solution()
m = 5
n = 7
print(s.rangeBitwiseAnd(5,7))