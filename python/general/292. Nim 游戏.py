class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4

s = Solution()
print(s.canWinNim(7))