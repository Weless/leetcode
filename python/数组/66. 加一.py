from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        addOne = True
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9 and addOne == True:
                res.append(0)
            elif addOne:
                res.append(digits[i]+1)
                addOne = False
            else:
                res.append(digits[i])
        if addOne:
            res.append(1)
        return res[::-1]

s = Solution()
digits = [9,9,9]
print(s.plusOne(digits))