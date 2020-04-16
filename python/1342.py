import itertools

class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while num !=0:
            if num % 2 == 0:
                num /= 2
            else:
                num-=1
            count+=1
        return count

s = Solution()
num = 8
print(s.numberOfSteps(num))


class Solution2:
    def numberOfSteps (self, num: int) -> int:

        for ans in itertools.count():
            if not num:
                return ans
            num = num - 1 if num & 1 else num // 2

s2 = Solution2()

print(s2.numberOfSteps(num))