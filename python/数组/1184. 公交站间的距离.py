from typing import List
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start,destination = destination,start
        i = 0
        total,res = 0,0
        while i < len(distance):
            total+=distance[i]
            if i>=start and i<=destination-1:
                res += distance[i]
            i+=1
        return min(total-res,res)

s = Solution()
distance = [3,6,7,2,9,10,7,16,11]
start = 6
destination = 2
print(s.distanceBetweenBusStops(distance,start,destination))