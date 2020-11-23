# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

def getResult(n):
    if not n:
        return []
    res = [[1]*i for i in range(1,n+1)]
    for i in range(len(res)):
        for j in range(len(res[i])):
            if j == 0 or j == len(res[i])-1:
                continue
            res[i][j] = res[i-1][j-1] + res[i-1][j]
    return res

print(getResult(5))