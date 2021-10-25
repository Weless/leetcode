class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter
        c = Counter(s)
        n = 0
        for v in c.values():
            if n == 0:
                n = v
            if n != v:
                return False
        return True