#Traditional binary_search

def binary_search(lst,target):
    n = len(lst)
    l = 0
    r = n-1

    #In this function, I have returned the index but we can also return True or False
    while l<=r:
        m = l + ((r-l)//2)
        if lst[m]==target:
            return m #return True
        elif lst[m]<target:
            l = m+1
        else:
            r = m-1

    return m #return False

lst = [-2,-1,0,4,6,9]
target = -2
print(binary_search(lst,target))

#Under and Over

def binarysearch2(arr):
    n = len(arr)
    l = 0
    r = n-1

    while l<r:
        m = (l+r)//2
        if arr[m]:
            r = m
        else:
            l = m+1
    return l #return r

arr = [False,False,True,True,True,True]
print(binarysearch2(arr))
