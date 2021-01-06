from typing import List
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        d = defaultdict(list)
        for i,v in items:
            d[i].append(v)

        res = []
        for i in d.keys():
            t = sorted(d[i])[-5:]
            res.append([i,sum(t)//5])
        res.sort(key=lambda x:x[0])
        return res