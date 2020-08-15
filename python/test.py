arr = [54,26,93,17,77,31,44,55,20]
def fast_sort(l, r):
    if l>r: return
    i,j = l,r
    pivot = arr[l]
    while i < j:
        while i < j and arr[j]>=pivot: j-=1
        while i < j and arr[i]<=pivot: i+=1
        arr[i],arr[j] = arr[j],arr[i]
    arr[j],arr[l] = arr[l],arr[j]
    fast_sort(l,i-1)
    fast_sort(i+1,r)

fast_sort(0,len(arr)-1)
print(arr)