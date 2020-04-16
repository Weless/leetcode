class Solution:
    def reverseWords(self, s: str) -> str:
        alist = [i for i in s.strip().split(" ") if i != ""]
        return " ".join(alist[::-1])

s = Solution()
test = "a good   example"
print(s.reverseWords(test))