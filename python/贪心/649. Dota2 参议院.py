class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque
        n = len(senate)
        radiant = deque()
        dire = deque()

        for i, ch in enumerate(senate):
            if ch == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            radiant.popleft()
            dire.popleft()

        return "Radiant" if radiant else "Dire"
s = Solution()
senate = "RDDDRR"
print(s.predictPartyVictory(senate))