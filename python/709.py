class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()


class Solution2:
    def toLowerCase(self, str: str) -> str:
        newStr = ''
        for i in range(len(str)):
            if ord(str[i]) < 97 and str[i].isalpha():
                newStr += chr(ord(str[i])+32)
            else:
                newStr += str[i]
        return newStr


s = Solution2()
print(s.toLowerCase("Hello"))


#### other answer
'''
class Solution:
    def toLowerCase(self, str): 
        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)
class Solution:
    def toLowerCase(self, str): 
        return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str)
'''