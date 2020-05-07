from typing import List

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = []
        if not A:
            return res
        key = set(A[0])
        for k in key:
            minimum = min(a.count(k) for a in A)
            res += minimum * k
        return res

s = Solution()
A = ["bella","label","roller"]
print(s.commonChars(A))
        