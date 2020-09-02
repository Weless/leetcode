# 单个列表
def getResult(nums):
    d = dict()
    res = []
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] +=1
    res = sorted(d.items(),key=lambda x:x[1],reverse=True)
    return res
nums = [1,2,3,1,3,2,4,1,1,1]
print(getResult(nums))


# 多个列表
def getResult2(nums2):
    d = dict()
    for num in nums2:
        d1 = dict()
        for i in num:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
        for key,value in d1.items():
            if key not in d:
                d[key] = value
            else:
                d[key] = max(d[key],value)
    res = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return res

nums2 = [[1,2,3,1,3,2,4,1,1,1],[1,2,3,1,1,1,1],[3,1,3,2,4,1,1,1]]
print(getResult2(nums2))


