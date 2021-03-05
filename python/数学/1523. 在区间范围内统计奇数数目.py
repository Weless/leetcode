class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low & 1 or high & 1:
            return 1 + (high-low)//2
        else:
            return (high-low)//2
