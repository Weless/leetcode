class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s1 = s[:n]
        s2 = s[n:]
        return s2 + s1
s = Solution()
a = "lrloseumgh"
k = 6
print(s.reverseLeftWords(a,k))