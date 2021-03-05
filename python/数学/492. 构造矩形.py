from typing import List
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        i = 1
        res = []
        while i*i <= area:
            a,b = divmod(area,i)
            if b == 0:
                if i < a:
                    res.append([a,i])
                else:
                    res.append([i,a])
            i+=1

        res.sort(key=lambda x: abs(x[0]-x[1]))
        return res[0]
s = Solution()
area = 4
print(s.constructRectangle(area))