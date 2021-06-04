from typing import List
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not nums: return nums
        if r*c > len(nums)*len(nums[0]):
            return nums
        res = []
        matrix = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                res.append(nums[i][j])
        print(res)
        x = 0
        for i in range(r):
            for j in range(c):
                matrix[i][j] = res[x]
                x+=1
        return matrix


s = Solution()
nums = [[1,2],
 [3,4]]
r = 2
c = 4
print(s.matrixReshape(nums,r,c))