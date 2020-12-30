from typing import List
class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s)-1:
            tmp = list(s)
            if s[i] == '+' and s[i+1] == '+':
                tmp[i]= '-'
                tmp[i+1] = '-'
                res.append(''.join(tmp))
            i+=1
        return res
s = Solution()
test = "++++"
print(s.generatePossibleNextMoves(test))