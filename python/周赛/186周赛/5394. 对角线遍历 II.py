class Solution(object):
    directions = [1,-1]
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if not nums:
            return []
        n = 0
        for col in nums:
            count = 0
            for i in col:
                count +=1
            n = max(n,count)
        m = len(nums)
        isAppeared = [[False for _ in range(n)] for _ in range(m)]


        res = []
        for i in range(m):
            for j in range(n):
                try:
                    nums[i][j]
                except:
                    continue
                if isAppeared[i][j] == True:
                    continue
                tmp = (i,j)
                stack = []
                stack.append(tmp)
                while True:
                    new_x = self.directions[0] + tmp[0]
                    new_y = self.directions[1] + tmp[1]

                    if new_y <0 or new_x >= m:
                        break
                    else:
                        try:
                            nums[new_x][new_y]
                        except:
                            tmp = (new_x,new_y)
                        else:
                            tmp = (new_x,new_y)
                            stack.append(tmp)
                while stack:
                    x,y = stack.pop()
                    res.append(nums[x][y])
                    isAppeared[x][y] = True
        return res

s = Solution()
nums = [[6],[8],[6,1,6,16]]
print(s.findDiagonalOrder(nums))
