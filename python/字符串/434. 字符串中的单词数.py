class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0
        words = s.strip().split()
        if len(words) == 0:
            return 0
        return len(words)
