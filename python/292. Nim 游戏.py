class Solution:
    def canWinNim(self, n: int) -> bool:
        if n ==1 or n == 2 or n ==3 :
            return True
        if n ==4 or n == 5 or n==6:
            return False
        return self.canWinNim(n-1) or self.canWinNim(n-2) or self.canWinNim(n-3)

s = Solution()
print(s.canWinNim(7))