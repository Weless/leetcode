from typing import List
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        count = 0
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                count +=1
        return count
s = Solution()
print(s.game([1,2,3],[1,2,3]))