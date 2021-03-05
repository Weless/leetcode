class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s)-1:
            if abs(ord(s[i]) - ord(s[i+1])) == 32:
                s = s[0:i] + s[i+2:]
                i = 0
                continue
            i +=1
        return s
s = Solution()
s_str = "abBAcC"
print(s.makeGood(s_str))
