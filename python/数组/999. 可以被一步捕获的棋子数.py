from typing import List
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        m,n = len(board),len(board[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'R':
                    t = i
                    # up
                    while t>=0:
                        if board[t][j] == 'B':
                            break
                        if board[t][j] == 'p':
                            ans+=1
                            break
                        t-=1
                    t = i
                    # down
                    while t<m:
                        if board[t][j] == 'B':
                            break
                        if board[t][j] == 'p':
                            ans += 1
                            break
                        t+=1
                    # left
                    t = j
                    while t>=0:
                        if board[i][t] == 'B':
                            break
                        if board[i][t] == 'p':
                            ans += 1
                            break
                        t-=1
                    # right
                    t = j
                    while t<n:
                        if board[i][t] == 'B':
                            break
                        if board[i][t] == 'p':
                            ans += 1
                            break
                        t+=1
        return ans

