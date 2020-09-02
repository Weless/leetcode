from typing import List
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0
        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1
        # peak can't be first or last
        if i == 0 or i == N-1:
            return False
        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1
        return i == N-1



s = Solution()
A = [9,8,7,6,5,4,3,2,1,0]
print(s.validMountainArray(A))

