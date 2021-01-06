class Solution:
    def checkRecord(self, s: str) -> bool:
        from collections import Counter
        d = dict(Counter(s))
        if 'A' in d and d.get('A')>1:
            return False
        c = 0
        for i in s:
            if i == 'L':
                c+=1
                if c>2:
                    return False
            else:
                c = 0
        return True