from typing import List
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score,reverse=True)
        first = (sorted_score[0],"Gold Medal")
        second = (sorted_score[1],"Silver Medal")
        for i in range(len(score)):
            score[i] =
