from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        balance = 0
        for i in bills:
            t = i - 5
            if t > balance:
                return False
            balance -= t
            balance += 5
        return True
s = Solution()
bills = [5,5,10,10,20]
print(s.lemonadeChange(bills))