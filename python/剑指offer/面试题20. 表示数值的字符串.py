class Solution:
    def isNumber(self, s: str) -> bool:
        import re
        if s == '.':
            return False
        reExr = ''
        if 'e' in s or 'E' in s:
            reExr = r'^[\+\-]?\d+[eE][\+\-]?\d+$'
        else:
            reExr = r'^[\+\-]?\d*\.?\d*$'

        return True if re.match(reExr,s) else False
s = Solution()
for i in ["+100","5e2","-123","3.1416","0123","-1E-16","0","e9"]:
    print(i,s.isNumber(i))
for i in ["12e","1a3.14","1.2.3","+-5","12e+5.4","."]:
    print(i,s.isNumber(i))