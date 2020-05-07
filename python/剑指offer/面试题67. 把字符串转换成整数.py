class Solution:
    def strToInt(self, str: str) -> int:
        if not str:
            return 0
        str2 = str.strip()
        if str2 == "" :
            return 0
        if str2[0] not in "+-0123456789":
            return 0
        import sys
        INT_MIN = -2147483648
        INT_MAX = 2**31 -1

        singal = "+"
        if str2[0] == "-":
            singal = "-"
            if len(str2) == 1:
                return 0
            str2=str2[1:]
        elif str2[0] == "+":
            if len(str2) == 1:
                return 0
            str2=str2[1:]
        if not str2[0].isdigit():
            return 0
        digit = ''
        for i in str2:
            if i.isdigit():
                digit += i
            else:
                break
        result = 1
        if singal == "-":
            result *= -1
        result *= self.strToInt2(digit)
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result
    def strToInt2(self,digit):
        sum = 0
        for i in digit:
            sum*=10
            sum+=(ord(i)-48)
        return sum
s = Solution()
print(s.strToInt("-+1"))