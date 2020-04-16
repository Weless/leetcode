class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return 'a'*n
        else:
            m,n = 1,n-1
            return 'a'+'b'*n

s = Solution()
print(s.generateTheString(4))