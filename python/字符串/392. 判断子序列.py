class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        while i<len(s)