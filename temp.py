arr = [3,34,4,12,5,2]

def dp_subset(arr,S):
    subset = [[0 for _ in range(S+1)] for _ in range(len(arr))]

    for i in range(0,len(arr)):
        for s in range(0,S+1):
            if i == 0:
                subset[i][s] = False
            elif s == 0:
                subset[i][s] = True

    for i in range(1,len(arr)):
        for s in range(1,S+1):

            if arr[i] > S:
                subset[i][s]=subset[i-1][s]
            else:
                A = subset[i-1][s-arr[i]]
                B = subset[i-1][s]
                subset[i][s] = A or B
    # print(subset)
    return subset[-1][-1]

print(dp_subset(arr,13))
