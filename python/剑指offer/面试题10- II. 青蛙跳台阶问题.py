class Solution:
    def numWays(self, n: int) -> int:
        result = [1]

        for i in range(1,n+1):
            if i == 1:
                result.append(1)
            elif i == 2:
                result.append(2)
            else:
                result.append(result[i-1]+result[i-2])
        return result[n] % 1000000007

s = Solution()
n = 7
print(s.numWays(n))