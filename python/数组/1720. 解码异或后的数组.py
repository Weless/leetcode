from typing import List
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        i = 0
        res = [first]
        before = first
        while i<len(encoded):
            t = before^encoded[i]
            res.append(t)
            before = t
            i+=1
        return res