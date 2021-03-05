class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        max_len = 0
        max_str = ""
        for i in range(len(s)):
            j = i+1
            while j < len(s)+1:
                tmp = s[i:j]
                if self.checkBeautifulStr(tmp):
                    if len(tmp) > max_len:
                        max_len = len(tmp)
                        max_str = tmp
                j+=1
        return max_str

    def checkBeautifulStr(self,s:str):
        for i in s:
            if i.isupper():
                if i.lower() not in s:
                    return False
            else:
                if i.upper() not in s:
                    return False
        return True

s = Solution()
s_str = "Bb"
print(s.longestNiceSubstring(s_str))