from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque, defaultdict
        d = defaultdict(list) # 邻接表
        m = [0]*numCourses # 入度表
        for i,j in prerequisites:
            d[j].append(i)
            m[i]+=1
        q = deque([i for i in range(numCourses) if m[i]==0])
        res = []
        count = 0
        while q:
           count += 1
           t = q.popleft()
           res.append(t)
           for i in d[t]:
               m[i] -= 1
               if m[i] == 0:
                   q.append(i)
        return res if count == numCourses else []
s = Solution()
numCourses = 3
prerequisites = [[1,0],[1,2],[0,1]]
print(s.findOrder(numCourses,prerequisites))

