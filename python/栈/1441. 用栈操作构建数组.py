from typing import List
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        stack = []
        idx = 0
        for i in range(1,n+1):
            if idx == len(target):
                break
            res.append("Push")
            stack.append(i)
            if stack[-1] != target[idx]:
                res.append("Pop")
                stack.pop()
            else:
                idx+=1
        return res
s = Solution()
target = []
n = 4
print(s.buildArray(target,n))