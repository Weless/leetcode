class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        tmp = ''
        for i in s:
            tmp += i
            if tmp*(len(s)//len(tmp)) == s:
                return True
        return False
