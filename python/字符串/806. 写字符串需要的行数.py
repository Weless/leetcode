from typing import List
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        total = 0
        for i in S:
            total += widths[ord(i)-ord('a')]
        return [total//100,total%100]