class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        for i in s:
            d[i]+=1
        for i,v in enumerate(s):
            if d[v] == 1:
                return i
        return -1