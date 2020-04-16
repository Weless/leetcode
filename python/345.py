class Solution:
    def reverseVowels(self, s: str) -> str:
        result = ''
        tmp = [i for i in s[::-1] if i.lower() in "aeiou"]
        j = 0
        for i in s:
            if i.lower() not in "aeiou":
                result += i
            else:
                result += tmp[j]
                j+=1
        return result

s = Solution()
test = "aA"
print(s.reverseVowels(test))