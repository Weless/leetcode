class Solution:
    def judgeCircle(self, moves: str) -> bool:
        tmp_dict = {"U":0,"D":0,"L":0,"R":0}
        for i in moves:
            tmp_dict[i] += 1
        if tmp_dict["U"] == tmp_dict["D"] and tmp_dict["L"] == tmp_dict["R"]:
            return True
        else:
            return False

class Solution2:
    def judgeCircle(self, moves: str) -> bool:
        upDown = 0
        leftRight = 0
        for i in moves:
            if i == 'U':
                upDown +=1
            elif i == "D":
                upDown -=1
            elif i == "L":
                leftRight +=1
            else:
                leftRight -=1
        if upDown == 0 and leftRight == 0:
            return True
        else:
            return False

class Solution3:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count("D") and moves.count("L") == moves.count("R")

s = Solution()
print(s.judgeCircle("UD"))

### other answers

'''
def judgeCircle(self, moves):
    c = collections.Counter(moves)
    return c['L'] == c['R'] and c['U'] == c['D']
'''