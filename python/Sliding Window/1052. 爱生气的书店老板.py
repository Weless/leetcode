from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        left,right = 0,X
        n = sum(customers[left:right])
        i = right
        while i < len(grumpy):
            if grumpy[i] == 0:
                n += customers[i]
            i+=1
        max_num = n
        while right < len(grumpy):
            if grumpy[right] == 1:
                n+=customers[right]
            if grumpy[left] == 1:
                n-=customers[left]
            max_num = max(max_num,n)
            right+=1
            left+=1
        return max_num

s = Solution()
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
X = 3
print(s.maxSatisfied(customers,grumpy,X))