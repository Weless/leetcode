class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        def dfs(val, idx):
            nonlocal res
            if idx == n:
                # 终止递归
                res += val
                return
            # 考虑选择当前数字
            dfs(val ^ nums[idx], idx + 1)
            # 考虑不选择当前数字
            dfs(val, idx + 1)

        dfs(0, 0)
        return res
