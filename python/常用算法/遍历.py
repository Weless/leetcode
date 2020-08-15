
def fun1(nums):
    n = len(nums)
    l = 2
    i = 0
    while l <=n:
        while i<=n-l:
            j = l+i-1
            i+=1
            print(j)
        l+=1

nums = [[1,2,3],[4,5,6],[7,8,9]]
fun1(nums)