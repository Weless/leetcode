class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        temp = [[0]*n for _ in range(m)]
        temp[0][0] = 1
        # 不可达
        for x in range(m):
            for y in range(n):
                if self.judge(x,y) > k :
                    temp[x][y] = -1

        for x in range(m):
            for y in range(n):

                if temp[x][y] == 1:
                    try:
                        if temp[x+1][y] == 0 and self.judge(x+1,y):
                            temp[x+1][y] = 1
                    except:
                        pass
                    try:
                        if temp[x-1][y] == 0 and self.judge(x-1,y):
                            temp[x-1][y] = 1
                    except:
                        pass
                    try:
                        if temp[x][y+1] == 0 and self.judge(x,y+1):
                            temp[x][y+1] = 1
                    except:
                        pass
                    try:
                        if temp[x][y-1] == 0 and self.judge(x, y-1):
                            temp[x][y-1] = 1
                    except:
                        pass
        return [temp[x][y] for x in range(m) for y in range(n)].count(1)

    def judge(self,x,y):
        x,y = str(x),str(y)
        aSum = 0
        for i in x:
            aSum += int(i)
        for i in y:
            aSum += int(i)
        return aSum


s = Solution()
print(s.movingCount(m = 2, n = 3, k = 1))