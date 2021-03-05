from typing import List
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        tag = 0
        up,down = True,True
        for i in range(1,len(A)):
            if A[i] < A[i-1]:
                up = False
                break
        if up:
            return True
        for i in range(1,len(A)):
            if A[i] > A[i-1]:
                down = False
                break
        if down:
            return True
        return False

# 两次遍历
class Solution(object):
    def isMonotonic(self, A):
        return (all(A[i] <= A[i+1] for i in range(len(A) - 1)) or
                all(A[i] >= A[i+1] for i in range(len(A) - 1)))


# 一次遍历
class Solution(object):
    def isMonotonic(self, A):
        store = 0
        for i in range(len(A) - 1):
            c = self.cmp(A[i], A[i+1])
            if c:
                if c != store != 0:
                    return False
                store = c
        return True
    def cmp(self,A,B):
        if A < B: return -1
        elif A > B : return 1
        else: return 0
