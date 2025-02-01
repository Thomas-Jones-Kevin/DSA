#sorting

#Bubble sort

def bubble(lst):
    n = len(lst)
    flag = True

    while flag:
        flag = False
        for i in range(1,n):
            if lst[i-1]>lst[i]:
                flag = True
                lst[i],lst[i-1] = lst[i-1],lst[i]

    return lst

lst = [-2,4,6,2,-9,7,-3]
print(bubble(lst))


#Insertion sort

def insert(lst):
    n = len(lst)
    for i in range(1,n):
        for j in range(i,0,-1):
            if lst[j-1]>lst[j]:
                lst[j],lst[j-1] = lst[j-1],lst[j]
            else:
                break
    return lst

lst = [-2,4,6,2,-9,7,-3]
print(insert(lst))


#Selection sort

def select(lst):
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if lst[j]<lst[min_index]:
                min_index = j

        lst[i],lst[min_index] = lst[min_index],lst[i]
    return lst

lst = [-2,4,6,2,-9,7,-3]
print(select(lst))


#Merge sort

def merge(lst):
    if len(lst)<=1:
        return lst
    
    
    m = len(lst)//2
    left = merge(lst[:m])
    right = merge(lst[m:])
    
    lst1 =[0]*len(lst)
    i=j=k=0


    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            lst1[k] = right[j]
            j+=1
            
        else:
            lst1[k] = left[i]
            i+=1

        k+=1

    while i<len(left):
        lst1[k] = left[i]
        i+=1
        k+=1

    while j<len(right):
        lst1[k] = right[j]
        j+=1
        k+=1
    return lst1

lst = [-2,4,6,2,-9,7,-3]
print(merge(lst))

#Quick sort

def quick(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[-1]
    left = [i for i in arr[:-1] if i<=pivot]
    right = [i for i in arr[:-1] if i>pivot]

    left = quick(left)
    right = quick(right)

    return left+[pivot]+right

lst = [-2,4,6,2,-9,7,-3]
print(quick(lst))


#Counting sort(Use for lists with positive values)
def counting(lst):
    maxx = max(lst)
    count = [0]*(maxx+1)

    for i in lst:
        count[i]+=1

    
    index = 0
    for i in range(len(count)):
        while count[i]>0:
            lst[index] = i
            count[i]-=1
            index+=1
        

    return lst

lst = [3,4,2,1,5,7,3,2,4]
print(counting(lst))

#Heap sort
import heapq
def heap(lst):
    heapq.heapify(lst)
    lst1 = [0]*len(lst)
    for i in range(len(lst)):
        lst1[i] = heapq.heappop(lst)

    return lst1

lst = [-2,4,6,2,-9,7,-3]
print(heap(lst))   

#Heap sort with heapify

def heap2(lst):
    lst2 = []
    for i in lst:
        heapq.heappush(lst2,i)

    return lst2

lst = [-2,4,6,2,-9,7,-3]
print(heap2(lst))



    


        