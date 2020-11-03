from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        def solve(node):
            if node == N - 1: return [[N - 1]]
            ans = []
            for nei in graph[node]:
                for path in solve(nei):
                    ans.append([node] + path)
            return ans
        return solve(0)



s = Solution()
graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(s.allPathsSourceTarget(graph))




