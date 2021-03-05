from typing import List
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_A = sum(A)
        sum_B = sum(B)
        avg_sum = (sum(A)+sum(B))//2
        # tag == 0, B的值大于A的值
        # tag == 1, A的值大于B的值
        tag = 0
        gap = 0
        if sum_B < sum_A:
            gap = sum_A - avg_sum
            tag = 1
        else:
            gap = avg_sum - sum_A
            tag = 0

        if tag == 1:
            for a in A:
                if a-gap in B:
                    return [a,a-gap]
        else:
            for a in A:
                if a+gap in B:
                    return [a,a+gap]
s = Solution()
A = [1,2,5]
B = [2,4]
print(s.fairCandySwap(A,B))



