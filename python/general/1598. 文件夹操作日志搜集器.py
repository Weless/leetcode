from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        n = 0
        for log in logs:
            if log == './':
                continue
            elif log == '../':
                if n == 0: continue
                else: n-=1
            else:
                n+=1
        return n