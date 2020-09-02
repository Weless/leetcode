class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        tag = 0
        s = ''
        if x < 0 :
            tag = 1
            s = str(x)[1:]
        else:
            s = str(x)
        res = s[::-1]
        i = 0
        while i < len(res):
            if res[i] == '0':
                i+=1
            else:
                break
        res = res[i:]
        if not tag:
            tmp = int(res)
            if tmp > 2**31 -1 :
                return 0
            else:
                return tmp
        else:
            tmp = int(res) * -1
            print(tmp)
            if tmp < -2**31:
                return 0
            else:
                return int(res) * -1

s = Solution()
x = -123
print(s.reverse(x))