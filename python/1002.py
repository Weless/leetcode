from typing import List
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        A.sort(key=lambda x:len(x))
        print(A)

        