class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(n).count('1')

s = Solution()
n = 1011
print(s.hammingWeight(n))