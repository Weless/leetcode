from typing import List
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for direction,amount in shift:
            if amount == 0:
                continue
            if direction == 0:
                s = s[amount:]+s[:amount]
            else:
                s = s[len(s)-amount:]+s[:-amount]
        return s

S = Solution()
s = "joiazl"
shift = [[1,1],[1,6],[0,1],[1,3],[1,0],[0,3]]
print(S.stringShift(s,shift))