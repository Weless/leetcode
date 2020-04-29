from typing import List
class Solution:
    def findDiagonalOrder(self, A: List[List[int]]) -> List[int]:
        stack = []
        for i, r in enumerate(A):
            for j, a in enumerate(r):
                if len(stack) <= i + j:
                    stack.append([])
                stack[i + j].append(a)
        res = []

        for i,r in enumerate(stack):
            if i % 2 == 0:
                res.extend(r[::-1])  # 数组相加
            else:
                res.extend(r)
        return res