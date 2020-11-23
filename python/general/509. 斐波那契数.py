class Solution:
    def fib(self, N: int) -> int:
        import itertools
        result = []
        num = itertools.count(0)
        for i in num:
            if i == 0:
                result.append(0)
            elif i == 1:
                result.append(1)
            else:
                result.append(result[i-2]+result[i-1])
            if i == N:
                return result[N]


s = Solution()
print(s.fib(4))