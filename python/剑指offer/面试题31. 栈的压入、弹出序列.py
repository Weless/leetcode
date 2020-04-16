from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []

        for i in popped:
            for j in pushed:
                if j != i and i != stack[-1]:
                    stack.append(j)
                elif
