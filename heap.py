import heapq
A = [3,45,8,3,-2,-9,4,31]

#Build a heap(min)
heap = heapq.heapify(A)
print(A)

#push 
heapq.heappush(A,-10)
print(A)

#pop
print(heapq.heappop(A))
print(A)

#peek
print("Minimum")
print(A[0])

#Heap sort
lst = [0]*len(A)
heapq.heapify(A)
for i in range(len(A)):
    lst[i] = heapq.heappop(A)

print(lst)

#pushpop(complicated)
B = [-8,-9,45,3,-2,3,4,31]
heapq.heappushpop(B,42)
print(B)

#Max heap
C = [3,45,8,3,-2,-9,4,31]
for i in range(len(C)):
    C[i] = -C[i]

heapq.heapify(C)
print(C)

#max heap pop
maxi = -heapq.heappop(C)
print(maxi)

#max heap push
heapq.heappush(C,-57)
print(C)

#build heap without heapify
D = [3,45,8,3,-2,-9,4,31]
heap = []
for i in D:
    heapq.heappush(heap,i)
print("Without heapify")
print(heap)