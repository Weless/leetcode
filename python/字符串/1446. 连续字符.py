class Solution:
    def maxPower(self, s: str) -> int:
        res = 1
        i = 1
        while i<len(s):
            tmp = 1
            while i<len(s) and s[i]==s[i-1]:
                tmp+=1
                i+=1
            if tmp>res:
                res = tmp
            i+=1
        return res
