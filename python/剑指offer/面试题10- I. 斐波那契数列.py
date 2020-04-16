class Solution:
    def fib(self, n: int) -> int:
        result = [0,1]
        if n >= 2:
            for i in range(2,n+1):
                result.append(result[i-1]+result[i-2])
        # print(result)
        return result[n] % 1000000007

s = Solution()
n = 45
print(s.fib(n))