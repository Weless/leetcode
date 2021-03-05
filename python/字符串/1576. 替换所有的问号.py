class Solution:
    def modifyString(self, s: str) -> str:
        tmp = list(s.split(''))
        for i in range(len(tmp)):
            if i == 0:
                if i+1 < len(tmp) and tmp[i] == "?":

            if tmp[i] == '?':
