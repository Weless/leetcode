from typing import List
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        from collections import Counter
        def f(s):
            if not s:
                return 0
            d = dict(Counter(s))
            return sorted(d.items(),key=lambda x:(x[0],[1]))[0][1]
        queries = list(map(f,queries))
        words = list(map(f,words))
        res = []
        for i in queries:
            c = 0
            for j in words:
                if i<j:
                    c+=1
            res.append(c)
        return res
