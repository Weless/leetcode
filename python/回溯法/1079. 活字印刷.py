class Solution:
    count = 0
    def numTilePossibilities(self, tiles: str) -> int:
        if not tiles:
            return 0
        res = []
        def dfs(path,choice,start,n):

            if len(path) == n:
                res.append(path)
                return
            for i in range(start,len(choice)):
                path += choice[i]
                dfs(path,choice,i+1,n)
                path = path[:-1]
        for i in range(1,len(tiles)+1):
            dfs('',tiles,0,i)
        print(res)
        return self.count

s = Solution()
tiles = "AAB"
print(s.numTilePossibilities(tiles))