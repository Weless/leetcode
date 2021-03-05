from typing import List
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        i = 1
        while True:
            if not self.haveZero(i) and not self.haveZero(n-i):
                return [i,n-i]
            i+=1
    def haveZero(self,A):
        return str(A).count("0")



