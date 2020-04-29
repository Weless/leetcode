class Solution:
    def isUnique(self, astr: str) -> bool:
        astr = sorted(astr)
        for i in range(len(astr)-1):
            if astr[i] == astr[i+1]:
                return False
        return True


# 位运算

class Solution:
    def isUnique(self, astr: str) -> bool:
        mark = 0
        for char in astr:
            move_bit = ord(char) - ord('a')
            if (mark & (1 << move_bit)) != 0:
                return False
            else:
                mark |= (1 << move_bit)
        return True
