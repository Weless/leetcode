class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        result = []
        for i in range(left,right+1):
            if self.isSelfDividingNumber(i):
                result.append(i)
        return result

    def isSelfDividingNumber(self, num):
        tmp = num
        while num:
            digit = num % 10
            if digit == 0 or tmp % digit != 0:
                return False
            num = num // 10
        return True

class Solution2:
    def selfDividingNumbers(self, left, right):
        result = []
        for num in range(left, right+1):
            tag = 0
            for i in str(num):
                i = int(i)
                if i == 0 or num % i != 0:
                    tag = 1
                    break
            if tag == 0:
                result.append(num)
        return result



s = Solution2()
print(s.selfDividingNumbers(left=1,right=22))

### other answer

'''
answer1:
return [x for x in range(left, right+1) if all((i and (x % i==0) for i in map(int, str(x))))]

answer2:
class Solution(object):
    def selfDividingNumbers(self, left, right):
        is_self_dividing = lambda num: '0' not in str(num) and all(num % int(digit) == 0 for digit in str(num))
        return filter(is_self_dividing, range(left, right + 1))
'''