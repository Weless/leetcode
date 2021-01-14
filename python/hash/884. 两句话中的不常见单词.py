from typing import List
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        from collections import defaultdict
        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for word in A.split(" "):
            d1[word]+=1
        for word in B.split(" "):
            d2[word]+=1

        res = []
        for k,v in d1.items():
            if v == 1 and k not in d2:
                res.append(k)

        for k,v in d2.items():
            if v == 1 and k not in d1:
                res.append(k)
        return res

