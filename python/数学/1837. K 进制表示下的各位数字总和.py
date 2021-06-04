class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        while n:
            res += n%k
            n =  n // k
        return res
s = Solution()
n = 34
k = 6
print(s.sumBase(34,6))