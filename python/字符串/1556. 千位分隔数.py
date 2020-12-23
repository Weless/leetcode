class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n<1000:
            return str(n)
        str_n = str(n)

