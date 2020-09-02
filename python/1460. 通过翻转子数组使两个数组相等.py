from typing import List
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        A = dict()
        B = dict()
        for i in target:
            if i not in A:
                A[i] = 1
            else:
                A[i]+=1
        for i in arr:
            if i not in B:
                B[i] = 1
            else:
                B[i]+=1
        return A==B