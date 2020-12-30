class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n != 1:
            if n % 2 == 0:
                n//=2
                ans+=n
            else:
                n = (n-1)//2
                ans+=n
                n+=1
        return ans