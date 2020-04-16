class Solution:
    def myAtoi(self, str: str) -> int:

        trip_str = str.strip()

        if trip_str == "":
            return 0

        if not trip_str[0].isdigit():
            if trip_str[0] != "+" :
                if trip_str[0] != "-":
                    return 0

        result = ''

        # 判断符号，默认为加号
        default = "+"

        if trip_str[0].isdigit():
            result += trip_str[0]
        elif trip_str[0] == "-":
            default = "-"


        for s in trip_str[1:]:
            if not s.isdigit():
                break
            else:
                result += s

        result = result.lstrip('0')

        if not result.isdigit():
            return 0

        int_result = int(result)
        if default == "-" and int_result > 2147483648:
            return -2147483648
        elif default == "+" and int_result > 2147483647:
            return 2147483647

        if default == "+":
            return int_result
        else:
            return int_result * -1

s =Solution()

# for i in ["4193 with words","     -42","words and 987","-91283472332","  0000000000012345678"]:
i = "  0000000000012345678"
print(s.myAtoi(i))


## better result


import re
class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        str = str.lstrip()      #清除左边多余的空格
        num_re = re.compile(r'^[\+\-]?\d+')   #设置正则规则
        num = num_re.findall(str)   #查找匹配的内容
        num = int(*num) #由于返回的是个列表，解包并且转换成整数
        return max(min(num,INT_MAX),INT_MIN)    #返回值