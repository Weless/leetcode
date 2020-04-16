from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        n = 0
        tag = False
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                n = i
                tag =True
                break

        import collections
        d = collections.deque(numbers)

        if tag == True:
            d.rotate(-(n+1))
        # print(d)
        return d.popleft()

s = Solution()
test = [3,4,5,1,2]
test2 = [1,3,5]
print(s.minArray(test2))