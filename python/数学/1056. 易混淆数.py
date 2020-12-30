class Solution:
    def confusingNumber(self, N: int) -> bool:
        items = '23457'
        str_N = str(N)
        for i in items:
            if i in str_N:
                return False
        res = ''
        for i in str_N[::-1]:
            if i == '0':
                res+='0'
            elif i == '1':
                res+='1'
            elif i == '6':
                res+='9'
            elif i == '8':
                res+='8'
            elif i == '9':
                res+='6'
        return res == str_N