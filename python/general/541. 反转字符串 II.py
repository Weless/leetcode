class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ''
        i,j,l= 0,1,len(s)
        while i < l:
            if j % 2 != 0:
                result += s[i:k*j][::-1]
            else:
                result += s[i:k*j]
            j+=1
            i+=k
        return result

s = Solution()
s1 = "abcdefg"
k = 2
print(s.reverseStr(s1,k))


### 双指针
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s, slen = list(s), len(s)

        for global_ptr in range(0, slen, 2 * k):
            left = global_ptr
            right = min(left + k - 1, slen - 1)
            while left < right:
                s[right], s[left] = s[left], s[right]
                left += 1
                right -= 1

        return ''.join(s)
