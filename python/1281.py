class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        mul = 1
        for i in str(n):
            sum +=int(i)
            mul*=int(i)
        return mul - sum






s = Solution()
print(s.subtractProductAndSum(4421))