from typing import List
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        A = [0] * (N+1) # 入度
        B = [0] * (N+1) # 出度
        for i,j in trust:
            A[j]+=1
            B[i]+=1
        i = 1
        while i<N+1:
            if A[i] == N-1 and B[i] == 0:
                return i
            i+=1
        return -1

s = Solution()
N = 3
trust = [[1,3],[2,3],[3,1]]
print(s.findJudge(N,trust))

