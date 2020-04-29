from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [],0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i+=1
        return not stack


s = Solution()
pushed = [2,1,0]
popped = [1,2,0]
print(s.validateStackSequences(pushed,popped))