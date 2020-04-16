class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        result = ''
        for i,v in enumerate(s):
            if i< k:
                continue
            else:
                result+=s[i:]
                result+=s[:i]
                return result
s = Solution()
a = "lrloseumgh"
k = 6
print(s.reverseLeftWords(a,k))