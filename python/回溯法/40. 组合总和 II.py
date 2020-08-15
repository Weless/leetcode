from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start,path,target):
            if target == 0:
                res.append(path[:])
                return
            for i in range(start,len(candidates)):
                if candidates[i] > target:
                    break
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                path.append(candidates[i])
                dfs(i+1,path,target-candidates[i])
                path.pop()
        if not candidates:
            return []
        res = []
        candidates.sort()
        dfs(0,[],target)
        return res
s = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(s.combinationSum2(candidates,target))