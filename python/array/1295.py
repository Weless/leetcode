class Solution:
    def findNumbers(self, nums):
        return list(map(lambda x:len(str(x))&1,nums)).count(0)


s = Solution()
print(s.findNumbers([12,345,2,6,7896]))