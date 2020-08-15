class Solution:
    directions = [(1,0),(0,1)] # 该题只需要两个方向即可
    def movingCount(self, m: int, n: int, k: int) -> int:
        from collections import deque
        queue = deque()
        queue.appendleft((0,0))
        marked = [[False for _ in range(n)] for _ in range(m)]
        marked[0][0] = True
        count = 1
        while queue:
            x,y = queue.pop()
            for direction in self.directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if 0<=new_x<=m-1 and 0<=new_y<=n-1 and self.check(new_x)+ self.check(new_y) <= k and marked[new_x][new_y] == False:
                    queue.appendleft((new_x,new_y))
                    marked[new_x][new_y] = True
                    count +=1
        return count

    def check(self,n):
        ans = 0
        while n:
            ans += n % 10
            n //= 10
        return ans





s = Solution()
print(s.movingCount(m = 10, n = 10, k = 8))