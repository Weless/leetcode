class Solution:
    def reverseBits(self, n: int) -> int:
        r = reversed("{:0>32s}".format(bin(n)[2:]))
        return int(''.join(r),2)

class Solution2:
    def reverseBits(self, n: int) -> int:
        i = 0
        res = 0
        while i<32:
            res<<=1
            res = n&1|res
            n>>=1
            i+=1
        return res

s = Solution2()
n = 43261596
print(s.reverseBits(43261596))