from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(index,path,target):
            if target == 0:
                res.append(path[:])
                return
            if target < 0:
                return
            for i in range(index,len(candidates)):
                path.append(candidates[i])
                dfs(i,path,target-candidates[i]) # 每次递归的索引不能比当前小，否则会产生重复
                path.pop()
        if not candidates:
            return []
        candidates.sort() # 排序为了提速
        res = []
        dfs(0,[],target)
        return res

s = Solution()
candidates = [2,3,6,7]
target = 7
print(s.combinationSum(candidates,target))