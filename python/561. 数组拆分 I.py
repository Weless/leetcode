class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        result = 0
        while nums:
            a, b = nums.pop(), nums.pop()
            result += min(a,b)
        return result

class Solution2:
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])

            

s = Solution2()
print(s.arrayPairSum([3,8,6,2,7,3]))
