from typing import List
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        res = [-1] * len(S)
        visited = [False] * len(S)
        from collections import deque
        q = deque()
        for i,v in enumerate(S):
            if v == C:
                q.appendleft(i)
                visited[i] = True
        level = 0
        while q:
            for _ in range(len(q)):
                x = q.pop()
                res[x] = level
                new_x1 = x+1
                new_x2 = x-1
                if new_x1<len(S) and not visited[new_x1]:
                    q.appendleft(new_x1)
                    visited[new_x1] = True
                if new_x2>=0 and not visited[new_x2]:
                    q.appendleft(new_x2)
                    visited[new_x2] = True
            level+=1
        return res

class Solution2(object):
    def shortestToChar(self, S, C):
        prev = float('-inf')
        ans = []
        for i, x in enumerate(S):
            if x == C: prev = i
            ans.append(i - prev)
        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C: prev = i
            ans[i] = min(ans[i], prev - i)

        return ans


s = Solution2()
S = "loveleetcode"
C = 'e'
print(s.shortestToChar(S,C))
