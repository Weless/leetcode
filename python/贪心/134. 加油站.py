from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        j = 0
        while j < len(gas):
            left = gas[j]
            i = j
            start = -1
            while True:
                if left >= cost[i]:
                    if start == -1:
                        start = i
                    if i+1<len(gas):
                        left = left - cost[i] + gas[i+1]
                        i+=1
                    else:
                        left = left - cost[i] + gas[0]
                        i=0
                    if i == start:
                        return i
                else:
                    j+=1
                    left = 0
                    start = -1
                    break
        return -1
s = Solution()
gas = [2,3,4]
cost = [3,4,3]
print(s.canCompleteCircuit(gas,cost))