class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        str_N = list(str(N))
        i = len(str_N)-1
        while i-1 >= 0:
            if str_N[i-1] > str_N[i]:
                str_N[i] = '9'
                if str_N[i-1] == '0':
                    str_N[i-1] = '9'
                else:
                    str_N[i-1]= str(int(str_N[i-1]) - 1)
            i-=1
        return int(''.join(str_N))

s = Solution()
N = 332
print(s.monotoneIncreasingDigits(N))