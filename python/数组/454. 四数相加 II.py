from typing import List
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        res = 0
        for i in A:
            for j in B:
                for h in C:
                    tmp = -1*(i + j + h)
                    res+=D.count(tmp)
        return res
A = [0,1,-1]
B = [-1,1,0]
C = [0,0,1]
D = [-1,1,1]
s = Solution()
print(s.fourSumCount(A,B,C,D))