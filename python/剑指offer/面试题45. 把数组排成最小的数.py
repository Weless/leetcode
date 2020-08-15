from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        import functools
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        strs = [str(num) for num in nums]
        strs.sort(key=lambda x,y: int(x+y)>int(y+x))
        return ''.join(strs)

s = Solution()
nums = [3,30,34,5,9]
print(s.minNumber(nums))