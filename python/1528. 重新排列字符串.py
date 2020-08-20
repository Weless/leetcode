from typing import List
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0] * len(s)
        j = 0
        for i in indices:
            res[i] = s[j]
            j+=1
        return ''.join(res)
