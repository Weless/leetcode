class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = [0 for _ in range(26)]
        for i in t:
            ans[ord(i)-ord('a')]+=1
        for i in s:
            ans[ord(i)-ord('a')]-=1
            if ans[ord(i)-ord('a')] == -1:
                return i
