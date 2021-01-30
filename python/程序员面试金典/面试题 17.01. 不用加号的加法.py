class Solution:
    def add(self, a: int, b: int) -> int:
        carry = a&b
        return a^b^carry

        