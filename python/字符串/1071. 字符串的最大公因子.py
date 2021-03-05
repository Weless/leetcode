class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i = 1
        while i < len(str1):
            t = str1[0:i]
            len(str1)