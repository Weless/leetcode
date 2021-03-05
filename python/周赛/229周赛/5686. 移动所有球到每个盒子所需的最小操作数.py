from typing import List
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        index = 0
        res = [0]*len(boxes)
        while index < len(boxes):
            n = 0
            for i in range(len(boxes)):
                if boxes[i] == "1":
                    n+=abs(index-i)
            res[index] = n
            index+=1
        return res
s = Solution()
boxes = "001011"
print(s.minOperations(boxes))

