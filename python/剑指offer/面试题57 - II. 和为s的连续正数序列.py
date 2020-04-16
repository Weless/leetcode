from typing import List
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        import itertools
        result = []
        for i in itertools.count(1):
            j = i+1
            sum = i+j
            if sum > target:
                break
            while sum < target:
                j = j+ 1
                sum += j
            if sum == target:
                result.append(list(range(i,j+1)))
        return result

s = Solution()
target = 15
print(s.findContinuousSequence(target))