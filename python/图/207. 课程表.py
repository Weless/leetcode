
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        import collections
        # 创建邻接表
        edges = collections.defaultdict(list)
        # 创建入度表
        indeg = [0] * numCourses
        for i,j in prerequisites:
            edges[j].append(i)
            # 计算入度
            indeg[i]+=1
        q = collections.deque([u for u in range(numCourses) if indeg[u]==0])
        visited = 0
        while q:
            visited +=1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -=1
                if indeg[v] == 0:
                    q.append(v)
        return visited == numCourses
