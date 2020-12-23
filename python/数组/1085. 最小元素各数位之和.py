from typing import List
class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        min_num = min(A)
        ans = 0
        for i in str(min_num):
            ans += int(i)
        return 1 if ans % 2 == 0 else 0