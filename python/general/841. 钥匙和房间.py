from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        from collections import deque
        if not rooms: return False
        l = len(rooms)
        res = [False] * l
        res[0] = True
        q = deque()
        q.append(rooms[0])
        while q:
            room = q.popleft()
            for j in room:
                if res[j]: continue
                res[j] = True
                q.append(rooms[j])
        return True if all(res) else False


s = Solution()
rooms = [[1,3],[3,0,1],[2],[0]]
print(s.canVisitAllRooms(rooms))