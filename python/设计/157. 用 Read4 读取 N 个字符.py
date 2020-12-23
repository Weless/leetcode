    class Solution:
        def read(self, buf, n):
            count=0
            while count<n:
                temp = [''] * 4
                cur = read4(temp)
                if cur == 0 :
                    break
                i = 0
                while i < cur and count <n:
                    buf[count] = temp[i]
                    count += 1
                    i+=1
            return count
