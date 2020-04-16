# 递归的二分查找优化
def binarySearch(alist, start, end, item):
    if start >= end:
        return False
    else:
        midpoint = (start + end) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item <  alist[midpoint]:
                end = midpoint - 1
                return binarySearch(alist,start,end,item)
            else:
                start = midpoint + 1
                return binarySearch(alist,start,end,item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 0,len(testlist)-1,13))
print(binarySearch(testlist, 0,len(testlist)-1,20))