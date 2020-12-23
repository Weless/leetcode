from typing import List
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set()
        for i in allowed:
            s.add(i)
        ans = 0
        for word in words:
            ok = True
            for i in word:
                if i not in s:
                    ok = False
                    break
            if ok:
                ans += 1
        return ans