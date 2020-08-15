from typing import List
class Solution:
    directions = [(1,0),(-1,0),(0,-1),(0,1),(1,-1),(1,1),(-1,1),(-1,-1)]
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i,j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        m,n = len(board),len(board[0])

        def cal(i,j):
            res = 0
            for direction in self.directions:
                new_x = i + direction[0]
                new_y = j + direction[1]
                if 0<=new_x<m and 0<=new_y<n and board[new_x][new_y] == 'M':
                    res+=1
            return res

        def bfs(i,j):
            from collections import deque
            queue = deque()
            queue.appendleft((i,j))
            board[i][j] = 'B'
            while queue:
                x,y = queue.pop()
                num = cal(x,y)
                if num >0:
                    board[x][y] = str(num)
                    continue
                for direction in self.directions:
                    new_x = x + direction[0]
                    new_y = y + direction[1]
                    if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == 'E':
                        queue.appendleft((new_x,new_y))
                        board[new_x][new_y] = 'B'
        bfs(i,j)
        return board

class Solution2:
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, 1), (-1, -1)]
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        def cal(i,j):
            res = 0
            for direction in self.directions:
                new_x = i + direction[0]
                new_y = j + direction[1]
                if 0<=new_x<len(board) and 0<=new_y<len(board[0]) and board[new_x][new_y] == 'M':
                    res+=1
            return res
        def dfs(i,j):
            if not 0<=i<len(board) or not 0<=j<len(board[0]):
                return
            if board[i][j] == 'E':
                num = cal(i,j)
                if num>0:
                    board[i][j] = str(num)
                else:
                    board[i][j] = 'B'
                    # 如果当前为'B'，才进行递归
                    for direction in self.directions:
                        dfs(i+direction[0],j+direction[1])
            else:
                return
        dfs(i,j)
        return board

s = Solution2()
board = [
    ['E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'M', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E']
]
click = [3,0]
print(s.updateBoard(board,click))