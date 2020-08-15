class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n &= (n-1)  # 每次可以消去最右边的1
        return count

s = Solution()
print(s.hammingWeight(9))