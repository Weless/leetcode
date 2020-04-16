class Solution:
    def add(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b:
            carry = a & b
            a ^= b
            b = ((carry) << 1) & 0xFFFFFFFF
            # print((a, b))
        return a if a < 0x80000000 else ~(a^0xFFFFFFFF)

# 投机取巧法
# class Solution:
#     def add(self, a: int, b: int) -> int:
#         return sum([a, b])


#
# class Solution(object):
#     def getSum(self, a, b):
#         """
#         :type a: int
#         :type b: int
#         :rtype: int
#         """
#         # 2^32
#         MASK = 0x100000000
#         # 整型最大值
#         MAX_INT = 0x7FFFFFFF
#         MIN_INT = MAX_INT + 1
#         while b != 0:
#             # 计算进位
#             carry = (a & b) << 1
#             # 取余范围限制在 [0, 2^32-1] 范围内
#             a = (a ^ b) % MASK
#             b = carry % MASK
#         return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)


s = Solution()
a = -1
b = 2
print(s.add(a,b))