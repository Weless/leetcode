from typing import List

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        result = []
        arr.sort()
        count = 0

        for i in arr:

            result.append(i)
            count +=1
            if count == k:
                break
        return result

s = Solution()
arr = [3,2,1]
k = 2
print(s.getLeastNumbers(arr,k))