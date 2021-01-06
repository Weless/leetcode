class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        from collections import defaultdict
        d1 = defaultdict(str)
        d2 = defaultdict(str)
        for i in range(len(s)):
            d1[s[i]] = t[i]
            d2[t[i]] = s[i]
        if len(d1) != len(d2):
            return False
        for k,v in d1.items():
            if k != d2[v]:
                return False
        return True