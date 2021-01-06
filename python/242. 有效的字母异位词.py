class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        from collections import defaultdict
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in s:
            d1[i]+=1
        for i in t:
            d2[i]+=1
        for i in s:
            if d1[i] != d2[i]:
                return False
        return True