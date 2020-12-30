from typing import List
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        # s = set()
        res = []
        for x in A:
            for i,y in enumerate(B):
                if x == y:
                    res.append(i)
        return res
