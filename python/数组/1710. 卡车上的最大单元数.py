from typing import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:(x[1],x[0]),reverse=True)
        print(boxTypes)
        res = 0
        for x,y in boxTypes:
            if truckSize>=x:
                res+=x*y
                truckSize-=x
            else:
                res+=truckSize*y
                truckSize=0
            if truckSize == 0:
                break
        return res

s = Solution()
boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
print(s.maximumUnits(boxTypes,truckSize))