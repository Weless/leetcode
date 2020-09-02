class Solution:
    def exchangeBits(self, num: int) -> int:
        res = ''
        num = bin(num).split('b')[1]
        res += num[-1] + num[1:-1] + num[0]
        return int(res,2)

s = Solution()
num = 1
print(s.exchangeBits(num))

