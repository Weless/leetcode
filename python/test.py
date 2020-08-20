class Solution(object):
    directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    def updateBoard(self, board, click):
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        def cal(x,y):
            count = 0
            for direction in self.directions:
                new_x = direction[0] + x
                new_y = direction[1] + y
                if 0<=new_x<len(board) and 0<=new_y<len(board[0]) and board[new_x][new_y] == 'M':
                    count+=1
            return count
        from collections import deque
        marked = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        q = deque()
        q.append(click)
        while q:
            x,y = q.popleft()
            num = cal(x,y)
            if num > 0:
                board[x][y] = str(num)
                continue
            for direction in self.directions:
                new_x = direction[0] + x
                new_y = direction[1] + y
                if 0<=new_x<=len(board)-1 and 0<=new_y<=len(board[0])-1 and marked[new_x][new_y] == False:
                    marked[new_x][new_y] = True
                    q.append((new_x,new_y))
            board[x][y] = 'B'
        return board
s = Solution()
board = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
click = [3,0]
print(s.updateBoard(board,click))