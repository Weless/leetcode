class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        result = ''
        first = 0
        for v in str_num:
            if v == "6" and first == 0:
                result += "9"
                first = 1
                continue
            result += v

        return int(result)



s = Solution()
num = 9669
print(s.maximum69Number(num))


## simple answer
class Solution:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace("6", "9", 1))

