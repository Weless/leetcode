from typing import List
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for x,y in queries:
            if res:
                t = res[-1]
                if (A[y] % 2 == 0 and x % 2 == 0) or (A[y]%2!=0 and x % 2 != 0):
                    t+=x
                res.append(t)
            A[y]+=x
            if not res:
                res.append(sum(x for x in A if x % 2 == 0))
        return res
s = Solution()
A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
print(s.sumEvenAfterQueries(A,queries))
