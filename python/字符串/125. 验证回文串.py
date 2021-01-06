class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''
        for i in s:
            if i.isdigit():
                t+=i
            elif i.isalpha():
                t+=i.lower()
        return t == t[::-1]
s = Solution()
test = "A man, a plan, a canal: Panama"
print(s.isPalindrome(test))
